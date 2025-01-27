import numpy as np
import audonnx

class SpeechEmotion:
    '''
    Pretrained model for dimensional speech emotion recognition based on wav2vec 2.0. 
    - Model link: https://zenodo.org/record/6221127#.YtWX73ZBxD8
    - Pretrained wav2vec2-large-robust model pruned from 24 to 12 transformer layers, and finetuned for V-A-D task on MSP-Podcast (v1.7)
    '''
    def __init__(self, sample_rate=16000, ser_valence_offset=0.0, ser_arousal_offset=0.0, ser_dominance_offset=0.0):

        # load trained model 
        self.model = audonnx.load('./res/ser_model/')
        self.sample_rate = sample_rate
        self.ser_valence_offset = ser_valence_offset
        self.ser_arousal_offset = ser_arousal_offset
        self.ser_dominance_offset = ser_dominance_offset

    def process(self, signal, extract_embeddings=False):

        # apply forward pass and get V-A-D predictions
        output = self.model(signal.astype(np.float32), self.sample_rate)
        vad_output = output['logits'].squeeze()

        prediction_valence = ((float(vad_output[2]) * 2.0) - 1.0) + self.ser_valence_offset
        if prediction_valence > 1.0:
            prediction_valence = 1.0
        elif prediction_valence < -1.0:
            prediction_valence = -1.0

        prediction_arousal = ((float(vad_output[0]) * 2.0) - 1.0) + self.ser_arousal_offset
        if prediction_arousal > 1.0:
            prediction_arousal = 1.0
        elif prediction_arousal < -1.0:
            prediction_arousal = -1.0

        prediction_dominance = ((float(vad_output[1]) * 2.0) - 1.0) + self.ser_dominance_offset
        if prediction_dominance > 1.0:
            prediction_dominance = 1.0
        elif prediction_dominance < -1.0:
            prediction_dominance = -1.0

        predictions = [prediction_valence, prediction_arousal, prediction_dominance] # valence - arousal - dominance
        # predictions = [vad_output[2], vad_output[0], vad_output[1]]

        # extract embeddings
        features = output['hidden_states'] if extract_embeddings==True else None

        return predictions, features




'''
sample_rate = 16000
signal = np.random.normal(size=sample_rate).astype(np.float32)

ser = SpeechEmotion(sample_rate)
predictions, features = ser.process(signal, extract_embeddings=True)

print(predictions, features.shape)
'''