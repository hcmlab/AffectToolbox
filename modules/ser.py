import numpy as np
import audonnx

class SpeechEmotion:
    '''
    Pretrained model for dimensional speech emotion recognition based on wav2vec 2.0. 
    - Model link: https://zenodo.org/record/6221127#.YtWX73ZBxD8
    - Pretrained wav2vec2-large-robust model pruned from 24 to 12 transformer layers, and finetuned for V-A-D task on MSP-Podcast (v1.7)
    '''
    def __init__(self, sample_rate=16000):

        # load trained model 
        self.model = audonnx.load('./res/ser_model/')
        self.sample_rate = sample_rate

    def process(self, signal, extract_embeddings=False):

        # apply forward pass and get V-A-D predictions
        output = self.model(signal.astype(np.float32), self.sample_rate)
        vad_output = output['logits'].squeeze()
        predictions = [vad_output[2], vad_output[0], vad_output[1]] # valence - arousal - dominance

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