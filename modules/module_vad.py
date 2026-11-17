import math
import numpy as np
import torch
from scipy.signal import resample_poly
from silero_vad import load_silero_vad


class VoiceActivity:
    # Silero probabilities are averaged over 32 ms frames of the current window.
    def __init__(self, sample_rate=16000, threshold=0.6):
        self.model = load_silero_vad(onnx=True)
        self.sample_rate = sample_rate
        self.threshold = threshold

    def process(self, signal):
        signal = np.asarray(signal, dtype=np.float32).reshape(-1)
        if signal.size == 0:
            return False
        if self.sample_rate != 16000:
            divisor = math.gcd(self.sample_rate, 16000)
            signal = resample_poly(signal, 16000 // divisor, self.sample_rate // divisor)

        # Windows overlap, so recurrent state must not carry into the next call.
        self.model.reset_states()
        predictions = []
        for start in range(0, len(signal), 512):
            frame = signal[start:start + 512]
            frame = np.pad(frame, (0, 512 - len(frame)))
            predictions.append(self.model(torch.from_numpy(frame), 16000).item())
        return bool(np.mean(predictions) >= self.threshold)
