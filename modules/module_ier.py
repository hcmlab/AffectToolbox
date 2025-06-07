import numpy as np

import tensorflow as tf
import cv2
import os

class EmotionFromCam():
    def __init__(self):

        #cv2.imwrite("test_out.jpg", res)
        ## Load TFLite model and allocate tensors.
        self.interpreter = tf.lite.Interpreter(model_path=os.path.join("res","ier_model","valence_arousal_model.tflite"))
        self.interpreter.allocate_tensors()

        # Get input and output tensors.
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()


    def predict(self, img):
    # Test model on random input data.
        input_shape = self.input_details[0]['shape']
        input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
        #print(img)
        res = cv2.resize(img, dsize=(224, 224))
        input_data = res.astype(np.float32)
        #print(input_data.shape)
        x = []
        x.append(input_data)
        input_data = np.asarray(x)
        #print(input_data.shape)
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)

        self.interpreter.invoke()

    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
        #print(input_shape)
        #print(output_data)
        return output_data

if __name__ == "__main__":
    image = cv2.imread("t3.png")
    ier = EmotionFromCam()
    ier.predict(image)