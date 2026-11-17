import inspect
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import numpy as np
import torch

from modules.module_sentiment import Sentiment
from modules.module_stt import SpeechToText
from modules.module_vad import VoiceActivity
from modules.AffectPipeline import AffectPipeline
import modules.QueueSystem as qs


class ModelInterfaceTests(unittest.TestCase):
    def test_cardiff_label_order_preserves_positive_and_negative_fusion_polarity(self):
        sentiment = Sentiment.__new__(Sentiment)
        sentiment.config = SimpleNamespace(id2label={0: 'negative', 1: 'neutral', 2: 'positive'})
        sentiment.tokenizer = Mock(return_value={})
        sentiment.model = Mock()
        sentiment.predict_func = sentiment._process_cardiff_multilingual
        options = {name: False for name in inspect.signature(AffectPipeline).parameters
                   if name.startswith('enable_')}
        with patch('modules.AffectPipeline.socket.socket'):
            pipeline = AffectPipeline(**options)
        self.addCleanup(pipeline.stop)
        pipeline.SENTIMENT_MODULE = sentiment
        pipeline._schedule_loop = Mock()
        qs.TRANSCRIPT_SPEECH.append('test sentence')
        for logits, sign in [([0., 0., 5.], 1), ([5., 0., 0.], -1)]:
            with self.subTest(sign=sign):
                sentiment.model.return_value = SimpleNamespace(logits=torch.tensor([logits]))
                result = sentiment.process('test sentence')[0]
                self.assertEqual([item[0] for item in result], ['positive', 'negative', 'neutral'])
                self.assertAlmostEqual(sum(item[1] for item in result), 1., places=6)
                pipeline.sentiment_loop()
                self.assertGreater(sign * qs.VALENCE_SENTIMENT[-1], 0.9)
                self.assertGreaterEqual(qs.VALENCE_SENTIMENT[-1], -1.)
                self.assertLessEqual(qs.VALENCE_SENTIMENT[-1], 1.)

    def test_german_sentiment_returns_the_same_shape_and_order(self):
        sentiment = Sentiment.__new__(Sentiment)
        sentiment.model = Mock()
        sentiment.model.predict_sentiment.return_value = (
            ['positive'], [[['neutral', .1], ['positive', .8], ['negative', .1]]])
        sentiment.predict_func = sentiment._process_german_sentiment
        self.assertEqual(sentiment.process('gut'),
                         [[['positive', .8], ['negative', .1], ['neutral', .1]]])
        self.assertEqual(sentiment.process(''),
                         [[['positive', 0], ['negative', 0], ['neutral', 1]]])

    def test_transcription_resamples_and_consumes_segments(self):
        stt = SpeechToText.__new__(SpeechToText)
        stt.sample_rate = 8000
        stt.min_signal_threshold = .1
        stt.model = Mock()
        stt.model.transcribe.return_value = (
            iter([SimpleNamespace(text=' Hello'), SimpleNamespace(text=' world')]), None)
        self.assertEqual(stt.process(np.full(8000, .2, dtype=np.float32)), 'Hello world')
        audio = stt.model.transcribe.call_args.args[0]
        self.assertEqual(audio.shape, (16000,))
        self.assertEqual(audio.dtype, np.float32)

    def test_transcription_skips_empty_and_quiet_audio(self):
        stt = SpeechToText.__new__(SpeechToText)
        stt.min_signal_threshold = .1
        stt.model = Mock()
        for audio in (np.array([]), np.zeros(16000)):
            self.assertEqual(stt.process(audio), '')
        stt.model.transcribe.assert_not_called()

    def test_silero_silence_and_overlapping_windows(self):
        vad = VoiceActivity(sample_rate=16000, threshold=.25)
        for _ in range(2):
            self.assertFalse(vad.process(np.zeros(1024, dtype=np.float32)))
        self.assertFalse(vad.process(np.array([], dtype=np.float32)))


if __name__ == '__main__':
    unittest.main()
