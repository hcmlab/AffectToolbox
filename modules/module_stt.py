import math
import numpy as np
from faster_whisper import WhisperModel
from scipy.signal import resample_poly


class SpeechToText:
    def __init__(self, sample_rate=16000, model='base', min_signal_threshold=0.0):
        self.model = WhisperModel(model, device='cpu', compute_type='int8')
        self.sample_rate = sample_rate
        self.min_signal_threshold = min_signal_threshold

    def process(self, signal):
        signal = np.asarray(signal, dtype=np.float32).reshape(-1)
        if signal.size == 0 or np.max(np.abs(signal)) <= self.min_signal_threshold:
            return ''

        if self.sample_rate != 16000:
            divisor = math.gcd(self.sample_rate, 16000)
            signal = resample_poly(signal, 16000 // divisor, self.sample_rate // divisor)

        segments, _ = self.model.transcribe(signal, language='en', beam_size=1,
                                            condition_on_previous_text=False)
        return ''.join(segment.text for segment in segments).strip()
