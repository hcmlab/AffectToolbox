import numpy as np
import webrtcvad

class VoiceActivity:
    
    # Voice Activity Detection based on WebRTC (https://webrtc.org/)
    # I prefer this solution in order to keep Windows compatibility and not to use GPU resources
    # (WebRTC might not perform well in noisy environments, however, it fast enough.)
    # https://github.com/wiseman/py-webrtcvad.git
    
    def __init__(self, segment_length=480, sample_rate=16000, threshold=0.6):
        
        # This class takes longer segments (i.e., 1 second), and averages the output and return speeh activity (True/False).
        # Input configurations:
        # segment_length: in frame number. the input should be an audio segment of 10, 20 or 30 milliseconds (i.e., in 16Khz, 160, 320, 480)
        # sample_rate   : a sample rate of 8, 16, 32 or 48 KHz 
        model = webrtcvad.Vad()
        model.set_mode(1)
        self.model = model

        assert(sample_rate in [8000, 16000, 32000, 48000])
        assert(segment_length in [160, 320, 480])
        self.segment_length = segment_length
        self.sample_rate = sample_rate
        self.threshold = threshold

    def process(self, signal):

        # 1-d input waveform as int array
        signal = signal.squeeze() if len(signal.shape)>1 else signal

        # apply forward pass for each segment and average 
        indices = [i for i in range(0, signal.shape[0], self.segment_length) if (i+self.segment_length)<signal.shape[0]]
        predictions = np.zeros(shape=(len(indices),))
        # for i, frame_index in enumerate(indices):
        #     input = signal[frame_index:frame_index+self.segment_length].tobytes()
        #     predictions[i] = self.model.is_speech(input, self.sample_rate)
        #     print(frame_index)
        input = signal[self.segment_length:self.segment_length+self.segment_length].tobytes()
        prediction = self.model.is_speech(input, self.sample_rate)
        #is_speech = True if np.sum(predictions)/len(indices)>=self.threshold else False
        #print(prediction)
        is_speech = prediction
        return is_speech