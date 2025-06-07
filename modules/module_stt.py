import torch
import whisper
from torchaudio import transforms as audio_transforms


class SpeechToText:
    """Includes all the necessary files to run this script"""

    def __init__(self, sample_rate=16000, model='base', min_signal_threshold=0.1):
        self.model = whisper.load_model(model)
        self.data = None
        self.predictions = None
        self.resample = audio_transforms.Resample(sample_rate, 16000)
        self.min_signal_threshold = min_signal_threshold

    def process(self, signal):

        # if signal is empty - return empty text
        if not signal.any() or abs(signal.min()) < self.min_signal_threshold and abs(signal.max()) < self.min_signal_threshold:
            return ''

        # to tensor
        signal_tensor = torch.from_numpy(signal)

        # resample audio
        signal_resampled = self.resample(signal_tensor)

        # load audio and pad/trim it to fit 30 seconds
        signal_pad = whisper.pad_or_trim(signal_resampled)

        # make log-Mel spectrogram and move to the same device as the model
        signal_mel = whisper.log_mel_spectrogram(signal_pad).to(self.model.device)

        # decode the audio
        options = whisper.DecodingOptions(fp16=False,language="en")
        result = whisper.decode(self.model, signal_mel, options)

        return result.text

