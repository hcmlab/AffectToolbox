import inspect
import threading
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import numpy as np

from modules.audioBuffer import AudioBuffer
from modules.AffectPipeline import AffectPipeline
from modules.QueueSystem import AffectDeque
import modules.QueueSystem as qs


class AudioFlowTests(unittest.TestCase):
    def pipeline(self, **settings):
        options = {name: False for name in inspect.signature(AffectPipeline).parameters
                   if name.startswith('enable_')}
        options.update(settings)
        with patch('modules.AffectPipeline.socket.socket'):
            pipeline = AffectPipeline(**options)
        self.addCleanup(pipeline.stop)
        pipeline._schedule_loop = Mock()
        return pipeline

    def test_fractional_window_is_exact_and_waits_for_real_audio(self):
        buffer = AudioBuffer(emotion_window=.07, min_speech=0)
        audio = np.arange(1536, dtype=np.float32)
        for i in range(2):
            buffer.append(audio[i*512:(i+1)*512], True)
            self.assertIsNone(buffer.emotion_window())
        buffer.append(audio[1024:], True)
        window, count = buffer.emotion_window()
        np.testing.assert_array_equal(window, audio[-1120:])
        self.assertEqual(count, 1536)

    def test_emotion_gate_uses_speech_in_whole_window(self):
        buffer = AudioBuffer(emotion_window=.128, min_speech=.064)
        for active in (True, True, False, False):
            buffer.append(np.ones(512, dtype=np.float32), active)
        self.assertIsNotNone(buffer.emotion_window())
        buffer.append(np.zeros(512, dtype=np.float32), False)
        self.assertIsNone(buffer.emotion_window())

    def test_pause_segment_preserves_pre_roll(self):
        buffer = AudioBuffer(max_segment=1., silence=.064, pre_roll=.064)
        completed = []
        for i, active in enumerate((False, False, True, True, False, False)):
            completed += buffer.append(np.full(512, i, dtype=np.float32), active)
        self.assertEqual(len(completed), 1)
        audio = completed[0]
        np.testing.assert_array_equal(audio, np.repeat(np.arange(6, dtype=np.float32), 512))
        self.assertIsNone(buffer.segment)
        self.assertFalse(buffer.append(np.zeros(512, dtype=np.float32), False))

    def test_maximum_segments_do_not_drop_or_duplicate_speech(self):
        buffer = AudioBuffer(max_segment=.1, silence=.064, pre_roll=0)
        original = np.arange(4096, dtype=np.float32)
        completed = []
        for i in range(8):
            completed += buffer.append(original[i*512:(i+1)*512], True)
        for i in range(2):
            completed += buffer.append(np.zeros(512, dtype=np.float32), False)
        self.assertTrue(all(len(audio) <= 1600 for audio in completed))
        combined = np.concatenate([audio for audio in completed])
        np.testing.assert_array_equal(combined[:len(original)], original)

    def test_history_capacity_follows_configured_windows(self):
        buffer = AudioBuffer(emotion_window=15., max_segment=20., pre_roll=.25)
        self.assertEqual(buffer.samples.maxlen, round(22.25 * 16000))
        self.assertFalse(buffer.samples)
        for kwargs in ({'max_segment': 0}, {'emotion_window': .001}, {'pre_roll': 10},
                       {'silence': float('nan')}, {'min_speech': 4}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                AudioBuffer(**kwargs)

    def test_capture_reads_small_chunks_in_order_and_only_once(self):
        pipeline = self.pipeline(microphone_chunks=16000)
        self.assertEqual(pipeline.MICROPHONE_CHUNKS, 512)
        samples = np.arange(1024, dtype=np.float32)
        stream = Mock()
        pipeline.stream = stream
        stream.read.side_effect = [samples[:512].tobytes(), samples[512:].tobytes()]
        def available():
            if stream.read.call_count == 2:
                pipeline._stop_event.set()
                return 0
            return 512
        stream.get_read_available.side_effect = available
        pipeline.microphone_loop_func()
        frames = [pipeline._audio_frames.get_nowait() for _ in range(2)]
        np.testing.assert_array_equal(np.concatenate(frames), samples)
        self.assertTrue(pipeline._audio_frames.empty())

    def test_vad_consumes_consecutive_frames_without_resetting(self):
        pipeline = self.pipeline()
        pipeline.VAD_LOOP = True
        pipeline.VAD_MODULE = Mock()
        pipeline.VAD_MODULE.speech_probability.side_effect = [.9, .1, .8]
        for i in range(3):
            pipeline._audio_frames.put(np.full(512, i, dtype=np.float32))
        worker = threading.Thread(target=pipeline.vad_loop)
        worker.start()
        self.addCleanup(worker.join, 1)
        for _ in range(100):
            if pipeline.audio_buffer.sample_count == 1536:
                break
            threading.Event().wait(.01)
        pipeline._stop_event.set()
        worker.join(1)
        self.assertEqual(pipeline.VAD_MODULE.speech_probability.call_count, 3)
        self.assertEqual(pipeline.audio_buffer.sample_count, 1536)
        self.assertFalse(worker.is_alive())

    def test_completed_transcript_is_sent_to_sentiment_once(self):
        pipeline = self.pipeline()
        pipeline.SENTIMENT_LOOP = True
        pipeline.STT_MODULE = Mock()
        pipeline.STT_MODULE.process.return_value = 'A new sentence'
        pipeline.SENTIMENT_MODULE = Mock()
        pipeline.SENTIMENT_MODULE.process.return_value = [[['positive', .8], ['negative', .1], ['neutral', .1]]]
        pipeline._segments.put(np.ones(512, dtype=np.float32))
        with patch.object(qs, 'TRANSCRIPT_SPEECH', AffectDeque(100)), \
                patch.object(qs, 'VALENCE_SENTIMENT', AffectDeque(100)):
            pipeline.stt_loop()
            pipeline.stt_loop()
            pipeline.sentiment_loop()
            pipeline.sentiment_loop()
            pipeline.STT_MODULE.process.assert_called_once()
            pipeline.SENTIMENT_MODULE.process.assert_called_once_with('A new sentence')
            self.assertEqual(len(qs.VALENCE_SENTIMENT), 1)
            self.assertAlmostEqual(qs.VALENCE_SENTIMENT[-1], .7)

    def test_emotion_does_not_reprocess_unchanged_audio(self):
        pipeline = self.pipeline(ser_window_length=.064, ser_min_speech=.032)
        pipeline.SER_MODULE = Mock()
        pipeline.SER_MODULE.process.return_value = ([.2, .3, -.4], None)
        for i in range(2):
            pipeline.audio_buffer.append(np.ones(512, dtype=np.float32), True)
        pipeline.ser_loop()
        pipeline.ser_loop()
        pipeline.SER_MODULE.process.assert_called_once()
        self.assertEqual(qs.DOMINANCE_SPEECH[-1], -.4)

    def test_wrong_capture_sample_rate_fails_before_opening_devices(self):
        with self.assertRaisesRegex(ValueError, '16000'):
            self.pipeline(sample_rate=48000)

    def test_audio_preview_alone_opens_input_without_loading_analysis_models(self):
        with patch('modules.AffectPipeline.pyaudio.PyAudio') as audio:
            pipeline = self.pipeline(enable_audio_loop=True)
        self.assertTrue(pipeline._needs_audio)
        self.assertFalse(hasattr(pipeline, 'VAD_MODULE'))
        self.assertEqual(audio.return_value.open.call_args.kwargs['rate'], 16000)
        self.assertEqual(audio.return_value.open.call_args.kwargs['frames_per_buffer'], 512)
        self.assertFalse(audio.return_value.open.call_args.kwargs['output'])

    def test_new_run_resets_history_without_synthetic_audio(self):
        pipeline = self.pipeline()
        qs.AUDIO_QUEUE.extend([.3] * 1000)
        qs.TRANSCRIPT_SPEECH.append('old session')
        qs.VALENCE_SPEECH.append(.9)
        with patch.object(pipeline._stop_event, 'wait', return_value=False):
            pipeline.start(SimpleNamespace())
        self.assertIs(qs.AUDIO_QUEUE, pipeline.audio_buffer.samples)
        self.assertFalse(qs.AUDIO_QUEUE)
        self.assertEqual(list(qs.TRANSCRIPT_SPEECH.q), [''])
        self.assertEqual(list(qs.VALENCE_SPEECH.q), [0.])
        self.assertFalse(qs.VALENCE_SPEECH.records)

if __name__ == '__main__':
    unittest.main()
