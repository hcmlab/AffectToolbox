import inspect
import threading
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

from modules.AffectPipeline import AffectPipeline


class PipelineShutdownTests(unittest.TestCase):
    def make_pipeline(self):
        options = {
            name: False
            for name in inspect.signature(AffectPipeline).parameters
            if name.startswith("enable_")
        }
        with patch("modules.AffectPipeline.socket.socket"):
            pipeline = AffectPipeline(**options)
        self.addCleanup(pipeline.stop)
        return pipeline

    def test_stop_cancels_pending_callbacks_and_is_repeatable(self):
        pipeline = self.make_pipeline()
        callback = Mock()
        pipeline._schedule_loop("print_loop_thread", 60.0, callback)
        pending = pipeline.print_loop_thread

        pipeline.stop()
        pipeline.stop()
        pipeline._schedule_loop("print_loop_thread", 0.0, callback)

        callback.assert_not_called()
        self.assertFalse(pending.is_alive())
        self.assertFalse(pipeline._workers)
        self.assertTrue(all(getattr(pipeline, name) is None for name in pipeline._LOOP_THREADS))

    def test_stop_waits_for_running_callback_and_prevents_rescheduling(self):
        pipeline = self.make_pipeline()
        entered = threading.Event()
        finish = threading.Event()
        self.addCleanup(finish.set)
        events = []
        errors = []
        next_callback = Mock()
        pipeline.capture = Mock(release=lambda: events.append("released"))

        def callback():
            entered.set()
            finish.wait(2.0)
            events.append("finished")
            pipeline._schedule_loop("face_record_loop_thread", 0.0, next_callback)

        def stop():
            try:
                pipeline.stop()
            except Exception as error:
                errors.append(error)

        pipeline._schedule_loop("face_record_loop_thread", 0.0, callback)
        self.assertTrue(entered.wait(1.0))
        stopper = threading.Thread(target=stop, daemon=True)
        stopper.start()
        self.assertTrue(pipeline._stop_event.wait(1.0))
        self.assertEqual(events, [])
        finish.set()
        stopper.join(2.0)

        self.assertFalse(stopper.is_alive())
        self.assertEqual(errors, [])
        self.assertEqual(events, ["finished", "released"])
        next_callback.assert_not_called()

    def test_busy_worker_keeps_its_resources_for_a_cleanup_retry(self):
        pipeline = self.make_pipeline()
        entered = threading.Event()
        finish = threading.Event()
        self.addCleanup(finish.set)
        capture = Mock()
        pipeline.capture = capture

        def callback():
            entered.set()
            finish.wait(2.0)

        pipeline._schedule_loop("face_record_loop_thread", 0.0, callback)
        self.assertTrue(entered.wait(1.0))
        worker = pipeline.face_record_loop_thread
        # Exhaust the shutdown deadline without spending five seconds in this test.
        with patch("modules.AffectPipeline.time.monotonic", side_effect=[0.0, 5.0]):
            with self.assertRaisesRegex(RuntimeError, "still busy"):
                pipeline.stop()
        capture.release.assert_not_called()
        self.assertIs(pipeline.capture, capture)

        finish.set()
        worker.join(2.0)
        pipeline.stop()
        capture.release.assert_called_once()
        self.assertIsNone(pipeline.capture)

    def test_all_resources_close_once_including_after_repeated_stop(self):
        pipeline = self.make_pipeline()
        names = (
            "capture", "stream", "audio", "face_detection", "mp_face_mesh",
            "POSE_MODULE", "_KAFKA_PRODUCER", "_SOCKET",
        )
        resources = {name: Mock() for name in names}
        for name, resource in resources.items():
            setattr(pipeline, name, resource)

        pipeline.stop()
        pipeline.stop()

        resources["capture"].release.assert_called_once()
        resources["stream"].stop_stream.assert_called_once()
        resources["stream"].close.assert_called_once()
        resources["audio"].terminate.assert_called_once()
        for name in ("face_detection", "mp_face_mesh", "POSE_MODULE", "_SOCKET"):
            resources[name].close.assert_called_once()
        resources["_KAFKA_PRODUCER"].flush.assert_called_once_with(timeout=5.0)
        resources["_KAFKA_PRODUCER"].close.assert_called_once_with(timeout=5.0)
        self.assertTrue(all(getattr(pipeline, name) is None for name in names))

    def test_cleanup_failure_does_not_skip_other_resources(self):
        pipeline = self.make_pipeline()
        capture = Mock()
        capture.release.side_effect = [OSError("release failed"), None]
        audio = Mock()
        pipeline.capture = capture
        pipeline.audio = audio

        with self.assertRaisesRegex(RuntimeError, "capture.release"):
            pipeline.stop()
        audio.terminate.assert_called_once()
        self.assertIs(pipeline.capture, capture)
        pipeline.stop()
        self.assertIsNone(pipeline.capture)

    def test_microphone_wait_is_interruptible_before_cleanup(self):
        pipeline = self.make_pipeline()
        stream = Mock()
        stream.get_read_available.return_value = 0
        pipeline.stream = stream
        pipeline.microphone_loop()
        worker = pipeline.microphone_loop_thread

        pipeline.stop()

        self.assertFalse(worker.is_alive())
        stream.read.assert_not_called()
        stream.stop_stream.assert_called_once()
        stream.close.assert_called_once()

    def test_late_callbacks_do_not_access_closed_resources(self):
        pipeline = self.make_pipeline()
        pipeline.stop()
        for name in pipeline._LOOP_THREADS:
            if name != "microphone_loop_thread":
                getattr(pipeline, name.removesuffix("_thread"))()
        with self.assertRaisesRegex(RuntimeError, "new pipeline instance"):
            pipeline.start(SimpleNamespace())

    def test_constructor_failure_closes_resources_already_acquired(self):
        options = {
            name: False
            for name in inspect.signature(AffectPipeline).parameters
            if name.startswith("enable_")
        }
        with patch("modules.AffectPipeline.socket.socket") as socket_factory:
            resource = socket_factory.return_value
            resource.setsockopt.side_effect = OSError("socket setup failed")
            with self.assertRaisesRegex(OSError, "socket setup failed"):
                AffectPipeline(**options)
            resource.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
