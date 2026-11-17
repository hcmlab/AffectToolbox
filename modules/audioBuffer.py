"""Rolling audio history and pause-based utterances, all at 16 kHz."""
from collections import deque
import math
import threading

import numpy as np


class AudioBuffer:
    sample_rate = 16000
    frame_size = 512

    def __init__(self, emotion_window=3.0, min_speech=0.5, max_segment=10.0,
                 silence=0.6, pre_roll=0.2):
        if not all(math.isfinite(x) for x in (emotion_window, min_speech, max_segment, silence, pre_roll)):
            raise ValueError('Audio window settings must be finite.')
        if emotion_window < 0.032 or not 0 <= min_speech <= emotion_window:
            raise ValueError('Emotion window must be positive; minimum speech must fit inside it.')
        if max_segment < 0.032 or silence < 0.032 or not 0 <= pre_roll < max_segment:
            raise ValueError('Segment and silence lengths must be positive; pre-roll must fit inside the segment.')
        self.emotion_samples = round(emotion_window * self.sample_rate)
        self.min_speech_samples = round(min_speech * self.sample_rate)
        self.max_segment_samples = round(max_segment * self.sample_rate)
        self.silence_samples = round(silence * self.sample_rate)
        capacity = math.ceil((max(emotion_window, max_segment + pre_roll) + 2) * self.sample_rate)
        self.samples = deque(maxlen=capacity)
        self.speech_frames = deque(maxlen=math.ceil(capacity / self.frame_size) + 1)
        self.pre_roll = deque(maxlen=round(pre_roll * self.sample_rate))
        self.lock = threading.Lock()
        self.sample_count = 0
        self.segment = None
        self.segment_has_speech = False
        self.last_speech_sample = 0

    def append(self, frame, is_speech):
        """Append one new frame and return completed audio segments."""
        with self.lock:
            start = self.sample_count
            self.sample_count += len(frame)
            self.samples.extend(frame.tolist())
            self.speech_frames.append((start, self.sample_count, is_speech))
            if self.segment is None and is_speech:
                self.segment = list(self.pre_roll)
            if self.segment is not None:
                self.segment.extend(frame.tolist())
                if is_speech:
                    self.segment_has_speech = True
                    self.last_speech_sample = self.sample_count
            self.pre_roll.extend(frame.tolist())

            completed = []
            while self.segment is not None and len(self.segment) >= self.max_segment_samples:
                remainder = self.segment[self.max_segment_samples:]
                if self.segment_has_speech:
                    completed.append(np.asarray(self.segment[:self.max_segment_samples], dtype=np.float32))
                self.segment = remainder
                self.segment_has_speech = bool(remainder) and is_speech
            if self.segment is not None and self.sample_count - self.last_speech_sample >= self.silence_samples:
                if self.segment_has_speech:
                    completed.append(np.asarray(self.segment, dtype=np.float32))
                self.segment = None
                self.segment_has_speech = False
            return completed

    def emotion_window(self):
        with self.lock:
            if len(self.samples) < self.emotion_samples:
                return None
            start = self.sample_count - self.emotion_samples
            speech = sum(max(0, end - max(begin, start))
                         for begin, end, active in self.speech_frames if active and end > start)
            if speech < self.min_speech_samples:
                return None
            audio = np.asarray(list(self.samples)[-self.emotion_samples:], dtype=np.float32)
            return audio, self.sample_count
