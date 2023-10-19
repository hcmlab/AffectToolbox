from termcolor import colored
import os
import random
import tkinter
from tkinter import *
from tkinter import ttk
import PIL
from PIL import ImageTk, Image


class LogModule():

    def __init__(self, tk_root,
                 enable_log_to_console=True,
                 enable_vad_loop=True,
                 enable_ser_loop=True,
                 enable_stt_loop=True,
                 enable_sentiment_loop=True,
                 enable_er_loop=True,
                 enable_facemesh_loop=True,
                 enable_pose_loop=True,
                 enable_fusion_loop=True):

        self.value_string = ''
        self.LOG_TO_CONSOLE = enable_log_to_console
        self.PRINT_VAD_LOOP = enable_vad_loop
        self.PRINT_SER_LOOP = enable_ser_loop
        self.PRINT_SENTIMENT_LOOP = enable_sentiment_loop
        self.PRINT_STT_LOOP = enable_stt_loop
        self.PRINT_CAMERA_LOOP = enable_er_loop
        self.PRINT_FACEMESH_LOOP = enable_facemesh_loop
        self.PRINT_FUSION_LOOP = enable_fusion_loop
        self.PRINT_POSE_LOOP = enable_pose_loop

        self.VOICE_OK = False
        self.SER_OK = False
        self.SENTIMENT_OK = False
        self.STT_OK = False
        self.CAMERA_OK = False
        self.BODY_OK = False

        self.TRACKING_VOICE = False
        self.TRACKING_FACE = False
        self.TRACKING_BODY = False

        self.TK_ROOT = tk_root
        self.TK_LOG_STRING = tkinter.StringVar()
        self.TK_LOG_LABEL = tkinter.Label(self.TK_ROOT, textvariable=self.TK_LOG_STRING, bg="azure2")
        self.TK_VIDEO_RAW = tkinter.Label(self.TK_ROOT)
        self.TK_VIDEO_CROP = tkinter.Label(self.TK_ROOT)
        self.TK_VIDEO_MESH = tkinter.Label(self.TK_ROOT)
        self.TK_VIDEO_SKEL = tkinter.Label(self.TK_ROOT)

    def compose_value_string(self, value_dict):

        self.value_string = ''
        self.value_string += colored('##########################################################\n' +
                                     '#              Affect Toolbox Pipeline started           #\n' +
                                     '##########################################################\n' +
                                     '#                    Active Loops:                       #\n' +
                                     '#--------------------------------------------------------#', 'blue')
        if self.PRINT_VAD_LOOP:
            color = 'green'
            if not self.TRACKING_VOICE:
                color = 'yellow'
            if not self.VOICE_OK:
                color = 'red'
            self.value_string += colored('\n# ', color='blue')
            self.value_string += colored('Voice:\t\t\t%i' % (value_dict['vad']), color=color)
        if self.PRINT_SER_LOOP:
            color = 'green'
            if not self.TRACKING_VOICE:
                color = 'yellow'
            if not self.SER_OK:
                color = 'red'
            self.value_string += colored('\n# ', color='blue')
            self.value_string += colored(
                'Speech (PAD):\t\t\t%+2.2f, %+2.2f, %+2.2f' % (value_dict['v_s'], value_dict['a_s'], value_dict['d_s']),
                color=color)
        if self.PRINT_STT_LOOP:
            color = 'green'
            if not self.TRACKING_VOICE:
                color = 'yellow'
            if not self.STT_OK:
                color = 'red'
            self.value_string += colored('\n# ', color='blue')
            self.value_string += colored(f"Transcript:\t\t\t{value_dict['t_s']}", color=color)
        if self.PRINT_SENTIMENT_LOOP:
            color = 'green'
            if not self.TRACKING_VOICE:
                color = 'yellow'
            if not self.SENTIMENT_OK:
                color = 'red'
            self.value_string += colored('\n# ', color='blue')
            self.value_string += colored('Sentiment (pos/neut/neg):\t%+2.2f, %+2.2f, %+2.2f' % (
                value_dict['s_pos'], value_dict['s_neu'], value_dict['s_neg']), color=color)
        if self.PRINT_CAMERA_LOOP:
            color = 'green'
            if not self.TRACKING_FACE:
                color = 'yellow'
            if not self.CAMERA_OK:
                color = 'red'
            self.value_string += colored('\n# ', color='blue')
            self.value_string += colored(
                'Face (PAD):\t\t\t%+2.2f, %+2.2f, %+2.2f' % (value_dict['v_f'], value_dict['a_f'], value_dict['d_f']),
                color=color)
        if self.PRINT_POSE_LOOP:
            color = 'green'
            if not self.TRACKING_BODY:
                color = 'yellow'
            if not self.BODY_OK:
                color = 'red'
            self.value_string += colored('\n# ', color='blue')
            self.value_string += colored('Body (Features):\t\t' + value_dict['p'], color=color)
        if self.PRINT_FUSION_LOOP:
            color = 'blue'
            self.value_string += colored('\n#\n# ', color='blue')
            self.value_string += colored('Fusion (PAD):\t\t\t%+2.2f, %+2.2f, %+2.2f' % (
                value_dict['m_f'][0], value_dict['m_f'][1], value_dict['m_f'][2]) + "\n#", color=color)

    def update_analysis(self, value_dict, img_raw, img_preprocessed, img_facemesh, img_bodyskel):

        self.compose_value_string(value_dict)

        if self.LOG_TO_CONSOLE:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.value_string)

        if self.PRINT_CAMERA_LOOP:
            if img_raw is not None:
                imgtk_raw = ImageTk.PhotoImage(image=PIL.Image.fromarray(img_raw).resize((250,
                                                                                          250)))
                self.TK_VIDEO_RAW.configure(image=imgtk_raw)
                self.TK_VIDEO_RAW.image = imgtk_raw
                self.TK_VIDEO_RAW.place(width=int(self.TK_ROOT.winfo_width() / 4),
                                        height=int(self.TK_ROOT.winfo_height() / 2), x=0, y=0)

            if img_preprocessed is not None:
                imgtk_preprocessed = ImageTk.PhotoImage(image=PIL.Image.fromarray(img_preprocessed).resize((250, 250)))
                self.TK_VIDEO_CROP.configure(image=imgtk_preprocessed)
                self.TK_VIDEO_CROP.image = imgtk_preprocessed
                self.TK_VIDEO_CROP.place(width=int(self.TK_ROOT.winfo_width() / 4),
                                        height=int(self.TK_ROOT.winfo_height() / 2), x=int(self.TK_ROOT.winfo_width() / 4), y=0)

        if self.PRINT_FACEMESH_LOOP:
            if img_facemesh is not None:
                imgtk_mesh = ImageTk.PhotoImage(image=PIL.Image.fromarray(img_facemesh).resize((250, 250)))
                self.TK_VIDEO_MESH.configure(image=imgtk_mesh)
                self.TK_VIDEO_MESH.image = imgtk_mesh
                self.TK_VIDEO_MESH.place(width=int(self.TK_ROOT.winfo_width() / 4),
                                        height=int(self.TK_ROOT.winfo_height() / 2), x=int(self.TK_ROOT.winfo_width() / 4)*2, y=0)

        if self.PRINT_POSE_LOOP:
            if img_bodyskel is not None:
                imgtk_skel = ImageTk.PhotoImage(image=PIL.Image.fromarray(img_bodyskel).resize((250, 250)))
                self.TK_VIDEO_SKEL.configure(image=imgtk_skel)
                self.TK_VIDEO_SKEL.image = imgtk_skel
                self.TK_VIDEO_SKEL.place(width=int(self.TK_ROOT.winfo_width() / 4),
                                        height=int(self.TK_ROOT.winfo_height() / 2), x=int(self.TK_ROOT.winfo_width() / 4)*3, y=0)

        self.TK_LOG_STRING.set(self.value_string)
        self.TK_LOG_LABEL.place(width=int(self.TK_ROOT.winfo_width()), height=int(self.TK_ROOT.winfo_height() / 2), x=0,
                                y=int(self.TK_ROOT.winfo_height() / 2))
