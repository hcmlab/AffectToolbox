from termcolor import colored
import os
import random

class LogModule():
    def __init__(self,
                 enable_vad_loop = True,
                 enable_ser_loop = True,
                 enable_stt_loop = True,
                 enable_sentiment_loop = True,
                 enable_er_loop = True,
                 enable_fusion_loop = True):
        self.PRINT_VAD_LOOP = enable_vad_loop
        self.PRINT_SER_LOOP = enable_ser_loop
        self.PRINT_SENTIMENT_LOOP = enable_sentiment_loop
        self.PRINT_STT_LOOP = enable_stt_loop
        self.PRINT_CAMERA_LOOP = enable_er_loop
        self.PRINT_FUSION_LOOP = enable_fusion_loop
        self.value_string = None
        self.VAD_OK = True
        self.SER_OK = True
        self.SENTIMENT_OK = True
        self.STT_OK = True
        self.CAMERA_OK = True

    def update_analysis(self, value_dict):
        self.value_string = ''
        if self.PRINT_VAD_LOOP:
            color = 'green'
            if (not self.VAD_OK):
                color = 'red'
            self.value_string += colored('Voice Activity: %i'% (value_dict['vad']),color=color)
        if self.PRINT_SER_LOOP:
            color = 'green'
            if (not self.SER_OK):
                color = 'red'
            self.value_string += colored('\t Valence Speech: %+2.3f \t Arousal Speech: %+2.3f \t Dominance Speech: %+2.3f' % (value_dict['v_s'], value_dict['a_s'], value_dict['d_s']),color=color)
        if self.PRINT_SENTIMENT_LOOP:
            color = 'green'
            if (not self.SENTIMENT_OK):
                color = 'red'
            self.value_string += colored('\t Pos Sentiment: %+2.3f \t Neut Sentiment: %+2.3f \t Neg Sentiment: %+2.3f' % (value_dict['s_pos'], value_dict['s_neu'], value_dict['s_neg']),color=color)
        if self.PRINT_STT_LOOP:
            color = 'green'
            if (not self.STT_OK):
                color = 'red'
            self.value_string += colored(f"\t Transcript: { value_dict['t_s'] }",color=color)
        if self.PRINT_CAMERA_LOOP:
            color = 'green'
            if (not self.CAMERA_OK):
                color = 'red'
            self.value_string += colored('\t Valence Face: %+2.3f \t Arousal Face: %+2.3f' % (value_dict['v_f'], value_dict['a_f']),color=color)

        # color = 'green'
        # if (not self.VAD_OK) or (not self.SER_OK) or (not self.CAMERA_OK):
        #     color = 'red'

        if self.PRINT_FUSION_LOOP:
            self.value_string += ('\tFusion (VAD): %+2.3f, %+2.3f, %+2.3f' % (value_dict['m_f'][0], value_dict['m_f'][1], value_dict['m_f'][2]))

        print("\r" + self.value_string, end='')

