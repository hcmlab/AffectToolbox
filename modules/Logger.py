from termcolor import colored
import os
import random

class LogModule():
    def __init__(self,
                 enable_vad_loop=True,
                 enable_ser_loop=True,
                 enable_stt_loop=True,
                 enable_sentiment_loop=True,
                 enable_er_loop=True,
                 enable_pose_loop=True,
                 enable_fusion_loop=True):
        self.PRINT_VAD_LOOP = enable_vad_loop
        self.PRINT_SER_LOOP = enable_ser_loop
        self.PRINT_SENTIMENT_LOOP = enable_sentiment_loop
        self.PRINT_STT_LOOP = enable_stt_loop
        self.PRINT_CAMERA_LOOP = enable_er_loop
        self.PRINT_FUSION_LOOP = enable_fusion_loop
        self.PRINT_POSE_LOOP = enable_pose_loop
        self.value_string = ''
        self.VAD_OK = True
        self.SER_OK = True
        self.SENTIMENT_OK = True
        self.STT_OK = True
        self.CAMERA_OK = True

    def update_analysis(self, value_dict):
        os.system('cls' if os.name == 'nt' else 'clear')

        self.value_string += colored(   '##########################################################\n' +
                                        '#              Affect Toolbox Pipeline started           #\n' +
                                        '##########################################################\n' +
                                        '#                    Active Loops:                       #\n' +
                                        '#--------------------------------------------------------#', 'blue')

        if self.PRINT_VAD_LOOP:
            color = 'green'
            if not self.VAD_OK:
                color = 'red'
            self.value_string += colored('\n# ', color='blue')
            self.value_string += colored('Voice:\t\t\t%i'% (value_dict['vad']), color=color)
        if self.PRINT_SER_LOOP:
            color = 'green'
            if value_dict['vad'] == 0:
                color = 'yellow'
            if not self.SER_OK:
                color = 'red'
            self.value_string += colored('\n# ', color='blue')
            self.value_string += colored('Speech (PAD):\t\t\t%+2.2f, %+2.2f, %+2.2f' % (value_dict['v_s'], value_dict['a_s'], value_dict['d_s']), color=color)
        if self.PRINT_STT_LOOP:
            color = 'green'
            if value_dict['vad'] == 0:
                color = 'yellow'
            if not self.STT_OK:
                color = 'red'
            self.value_string += colored('\n# ', color='blue')
            self.value_string += colored(f"Transcript:\t\t\t{ value_dict['t_s'] }", color=color)
        if self.PRINT_SENTIMENT_LOOP:
            color = 'green'
            if value_dict['vad'] == 0:
                color = 'yellow'
            if not self.SENTIMENT_OK:
                color = 'red'
            self.value_string += colored('\n# ', color='blue')
            self.value_string += colored('Sentiment (pos/neut/neg):\t%+2.2f, %+2.2f, %+2.2f' % (value_dict['s_pos'], value_dict['s_neu'], value_dict['s_neg']), color=color)
        if self.PRINT_CAMERA_LOOP:
            color = 'green'
            if not self.CAMERA_OK:
                color = 'red'
            self.value_string += colored('\n# ', color='blue')
            self.value_string += colored('Face (PAD):\t\t\t%+2.2f, %+2.2f, %+2.2f' % (value_dict['v_f'], value_dict['a_f'], value_dict['d_f']), color=color)
        if self.PRINT_FUSION_LOOP:
            self.value_string += colored('\n#\n# ', color='blue')
            self.value_string += colored('Fusion (PAD):\t\t\t%+2.2f, %+2.2f, %+2.2f' % (value_dict['m_f'][0], value_dict['m_f'][1], value_dict['m_f'][2]) + "\n#", color='blue')
        if self.PRINT_POSE_LOOP:
            self.value_string += colored('\n# ', color='blue')
            self.value_string += ('Body (Features):\t\t' + value_dict['p'])

        print(self.value_string)
        self.value_string = ''

