import cv2
import numpy as np
from scipy.signal import butter, filtfilt


class HeartRateEstimation():
    def __init__(self, fps, lowcut=2/3, highcut=4):
        self.prop_sm = {
                            "lower_cut": np.array([0, 133, 77], dtype=np.uint8),
                            "upper_cut": np.array([255, 173, 127], dtype=np.uint8)
                        }
        self.prop_csm = {
                            "avg": "median"
                        }
        self.prop_bem = {
                            "N": 2048
                        } 
        self.fps = fps
        self.lowcut = lowcut
        self.highcut = highcut
        self.b, self.a = self._butter_bandpass() 


    def predict(self, clip, step_size):
        ippg_raw = np.zeros(len(clip)) 

        clip_seg = self._threshold(clip, self.prop_sm["lower_cut"], self.prop["upper_cut"])
        for idx, img in enumerate(clip_seg):
            ippg_raw[idx] = self._chrom(img)
        signal = filtfilt(self.b, self.a, ippg_raw)
        hr = self.fftpeak(signal)
        return hr
    

    '''
    Could be a faster version for development
        if np.all(self.ippg_raw==0):
            clip_seg = self._threshold(clip, self.prop_sm["lower_cut"], self.prop["upper_cut"])
            for idx, img in enumerate(clip_seg):
                self.ippg_raw[idx] = self._chrom(img)
            signal = filtfilt(self.b, self.a, self.ippg_raw)
            hr = self.fftpeak(signal)
            return hr
        
        else:
            clip_seg = self._threshold(clip, self.prop_sm["lower_cut"], self.prop["upper_cut"])
            self.ippg_raw[step_size:] = self.ippg_raw[:-step_size]
            for idx, img in enumerate(clip_seg[-step_size:]):
                self.ippg_raw[idx] = self._chrom(img)   
            signal = filtfilt(self.b, self.a, self.ippg_raw)
            hr = self.fftpeak(signal)
            return hr
    '''        

    def _butter_bandpass(self, order=5):
        return butter(order, [self.lowcut, self.highcut], btype='bandpass', fs=self.fps)
    
    
    def fftpeak(self, input, N=2048):

        signal_centered = input - np.mean(input)

        window = np.hamming(len(signal_centered))
        signal = signal_centered * window

        # Make FFT
        fft_values = np.fft.fft(signal, n=N)
        frequencies = np.fft.fftfreq(N, 1/self.fps)

        # Take the magnitude of the FFT and consider only the positive frequencies
        magnitude = np.abs(fft_values[:N//2])
        positive_frequencies = frequencies[:N//2]

        # Find the most dominant frequency
        dominant_frequency_index = np.argmax(magnitude)
        bpm = positive_frequencies[dominant_frequency_index]*60

        return bpm

#    def _threshold(img, lower_cut, upper_cut):
#        img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)    
#        mask = cv2.inRange(img_ycrcb, lower_cut, upper_cut) 
#        img_seg = cv2.bitwise_and(img, img, mask=mask)
#
#        return img_seg

    
    def _threshold(images, lower_cut, upper_cut):
        images_ycrcb = np.stack([cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb) for img in images], axis=0)
        lower_cut = np.array(lower_cut, dtype=np.uint8)
        upper_cut = np.array(upper_cut, dtype=np.uint8)
        masks = ((images_ycrcb >= lower_cut) & (images_ycrcb <= upper_cut)).all(axis=-1)
        masks = masks.astype(np.uint8) * 255  # In binäre Masken umwandeln (0 oder 255)
        results = images * masks[..., np.newaxis]

        return results


    def _chrom(signal):
        """
        CHROM method on CPU using Numpy.

        De Haan, G., & Jeanne, V. (2013). Robust pulse rate from chrominance-based rPPG. 
        IEEE Transactions on Biomedical Engineering, 60(10), 2878-2886.
        """

        # CHROM-Signale berechnen
        b, g, r = [np.mean(signal[..., x]) for x in range(3)]    
        x_c1 = 3 * r - 2 * g
        x_c2 = 1.5 * r + g - 1.5 * b

        # Projektion berechnen (Rotation)
        signal = np.array([x_c1, x_c2])
        theta = np.arctan2(np.std(x_c2), np.std(x_c1))  # Optimale Projektion
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                        [np.sin(theta), np.cos(theta)]])
        s = np.dot(rotation_matrix, signal)

        return s[0] 






