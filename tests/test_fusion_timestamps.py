import inspect
import unittest
from unittest.mock import Mock, patch

import numpy as np

from modules.AffectPipeline import AffectPipeline
from modules.QueueSystem import AffectDeque
import modules.QueueSystem as qs
import modules.module_fusion as fusion


INPUTS = (
    ('FUSION_USE_FACE_V', 'VALENCE_FACE', 'EVENTS_VALENCE', 0),
    ('FUSION_USE_FACE_A', 'AROUSAL_FACE', 'EVENTS_AROUSAL', 1),
    ('FUSION_USE_FACE_D', 'DOMINANCE_FACE', 'EVENTS_DOMINANCE', 2),
    ('FUSION_USE_PARA_V', 'VALENCE_SPEECH', 'EVENTS_VALENCE', 0),
    ('FUSION_USE_PARA_A', 'AROUSAL_SPEECH', 'EVENTS_AROUSAL', 1),
    ('FUSION_USE_PARA_D', 'DOMINANCE_SPEECH', 'EVENTS_DOMINANCE', 2),
    ('FUSION_USE_SENTIMENT_V', 'VALENCE_SENTIMENT', 'EVENTS_VALENCE', 0),
    ('FUSION_USE_POSE_D', 'DOMINANCE_POSE', 'EVENTS_DOMINANCE', 2),
)


class FusionTimestampTests(unittest.TestCase):
    def histories(self):
        return {name: AffectDeque(100) for _, name, _, _ in INPUTS}

    def events(self):
        return {name: fusion.EventDeque(500)
                for name in ('EVENTS_VALENCE', 'EVENTS_AROUSAL', 'EVENTS_DOMINANCE')}

    def pipeline(self):
        options = {name: False for name in inspect.signature(AffectPipeline).parameters
                   if name.startswith('enable_')}
        with patch('modules.AffectPipeline.socket.socket'):
            pipeline = AffectPipeline(**options)
        self.addCleanup(pipeline.stop)
        pipeline._schedule_loop = Mock()
        return pipeline

    def test_all_inputs_accept_slow_processing_and_expire_from_completion(self):
        for flag, name, event_name, dimension in INPUTS:
            with self.subTest(input=name), \
                    patch.multiple(qs, start_time=0, **self.histories()), \
                    patch.multiple(fusion, **self.events()), \
                    patch('time.time', return_value=1.) as clock:
                module = fusion.FusionModule()
                setattr(module, flag, True)
                # Processing takes 9 seconds, longer than the 5-second fusion lifetime.
                clock.return_value = 10.
                getattr(qs, name).append(.4)
                clock.return_value = 10.5
                self.assertGreater(module.update_fusion()[dimension], 0.)
                events = getattr(fusion, event_name)
                self.assertEqual(list(events.time), [10000])
                module.update_fusion()
                self.assertEqual(len(events), 1)
                clock.return_value = 14.999
                self.assertGreater(module.update_fusion()[dimension], 0.)
                clock.return_value = 15.
                self.assertEqual(module.update_fusion(), [0., 0., 0.])
                self.assertFalse(events.q)

    def test_results_completed_in_same_millisecond_are_each_consumed_once(self):
        with patch.multiple(qs, start_time=0, **self.histories()), \
                patch.multiple(fusion, **self.events()), \
                patch('time.time', return_value=10.):
            module = fusion.FusionModule()
            module.FUSION_USE_FACE_V = True
            qs.VALENCE_FACE.append(.2)
            module.update_fusion()
            qs.VALENCE_FACE.append(.3)
            module.update_fusion()
            module.update_fusion()
            self.assertEqual(len(fusion.EVENTS_VALENCE), 2)
            self.assertEqual(list(fusion.EVENTS_VALENCE.time), [10000, 10000])

    def test_time_waiting_after_completion_is_not_refreshed_by_fusion(self):
        with patch.multiple(qs, start_time=0, **self.histories()), \
                patch.multiple(fusion, **self.events()), \
                patch('time.time', return_value=1.) as clock:
            module = fusion.FusionModule()
            module.FUSION_USE_SENTIMENT_V = True
            clock.return_value = 2.
            qs.VALENCE_SENTIMENT.append(.5)
            clock.return_value = 8.
            self.assertEqual(module.update_fusion(), [0., 0., 0.])
            self.assertFalse(fusion.EVENTS_VALENCE.q)

    def test_sentiment_timestamp_is_after_sentiment_not_transcription(self):
        with patch.multiple(qs, start_time=0, TRANSCRIPT_SPEECH=AffectDeque(100), **self.histories()), \
                patch.multiple(fusion, **self.events()), \
                patch('time.time', return_value=1.) as clock:
            pipeline = self.pipeline()
            pipeline.SENTIMENT_LOOP = True
            module = fusion.FusionModule()
            module.FUSION_USE_SENTIMENT_V = True
            def transcribe(audio):
                clock.return_value = 10.
                return 'good'
            def sentiment(text):
                clock.return_value = 20.
                return [[['positive', .8], ['negative', .1], ['neutral', .1]]]
            pipeline.STT_MODULE = Mock(process=transcribe)
            pipeline.SENTIMENT_MODULE = Mock(process=sentiment)
            pipeline._segments.put(np.ones(512, dtype=np.float32))
            pipeline.stt_loop()
            self.assertEqual(qs.TRANSCRIPT_SPEECH.time[-1], 10000)
            pipeline.sentiment_loop()
            self.assertEqual(qs.VALENCE_SENTIMENT.time[-1], 20000)
            clock.return_value = 20.1
            self.assertGreater(module.update_fusion()[0], 0.)
            self.assertEqual(list(fusion.EVENTS_VALENCE.time), [20000])

    def test_emotion_face_and_pose_publish_after_their_processing(self):
        with patch.multiple(qs, start_time=0, **self.histories()), \
                patch('time.time', return_value=1.) as clock:
            pipeline = self.pipeline()
            for _ in range(94):
                pipeline.audio_buffer.append(np.ones(512, dtype=np.float32), True)
            def speech(audio, **kwargs):
                clock.return_value = 10.
                return [.2, .3, .4], None
            pipeline.SER_MODULE = Mock(process=speech)
            pipeline.ser_loop()
            for history in (qs.VALENCE_SPEECH, qs.AROUSAL_SPEECH, qs.DOMINANCE_SPEECH):
                self.assertEqual(history.time[-1], 10000)
            def face(image):
                clock.return_value = 20.
                return np.array([[.2, .3]])
            pipeline.IER_MODULE = Mock(predict=face)
            with patch.object(qs, 'FACE_ACTIVITY', [1]), \
                    patch.object(qs, 'IMAGE_FACE_PREPROCESSED', [np.zeros((20, 20, 3), dtype=np.uint8)]):
                pipeline.face_er_loop()
            for history in (qs.VALENCE_FACE, qs.AROUSAL_FACE, qs.DOMINANCE_FACE):
                self.assertEqual(history.time[-1], 20000)
            def pose(image):
                clock.return_value = 30.
            pipeline.POSE_MODULE = Mock(predict=pose, dominance=.4, facing_cam=1, tracking=True)
            with patch.object(qs, 'IMAGE_FACE_RAW', [np.zeros((20, 20, 3), dtype=np.uint8)]):
                pipeline.pose_loop()
            self.assertEqual(qs.DOMINANCE_POSE.time[-1], 30000)


if __name__ == '__main__':
    unittest.main()
