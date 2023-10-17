import random
import time
import numpy as np
import pyaudio
import threading
import cv2
import soundfile
from modules.VideoDecorator import VideoShow
from modules.Logger import LogModule
import socket
import lxml.etree
import lxml.builder
from termcolor import colored
import os
import modules.QueueSystem as qs
import json


class DeviceManager():
    def __init__(self):
        pass

    def get_available_microphones(self):
        import pyaudio

        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')

        for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print(i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

    def choose_microphone(self):
        print("The following microphones are available:")
        self.get_available_microphones()
        print("Choose one option.")
        a = input('').split(" ")[0]
        return int(a)

    def get_available_cameras(self):
        from pygrabber.dshow_graph import FilterGraph


        devices = FilterGraph().get_input_devices()

        available_cameras = {}

        for device_index, device_name in enumerate(devices):
            available_cameras[device_index] = device_name
            print(str(device_index) + " - " + device_name)



    def choose_camera(self):
        print("The following cameras are available:")
        self.get_available_cameras()
        print("Choose one option.")
        a = input('').split(" ")[0]
        return int(a)

class AffectPipeline():
    def __init__(self,
                 enable_vad_loop=True,
                 enable_ser_loop=True,
                 enable_stt_loop=True,
                 enable_camera_loop=True,
                 enable_print_loop=True,
                 enable_send_udp_loop=True,
                 enable_send_kafka_loop=True,
                 enable_face_er_loop=True,
                 enable_face_mesh_loop=True,
                 enable_pose_loop=True,
                 enable_fusion_loop=True,
                 enable_sentiment_loop=True,
                 show_face_mesh=True,
                 enable_web_app=False,
                 face_mesh_show_face_edges=True,
                 face_mesh_show_face_pupils=False,
                 face_mesh_show_face_contour=False,
                 camera_id=0,
                 ser_loop_rate=2.0,
                 stt_loop_rate=0.1,
                 sentiment_loop_rate=2.0,
                 vad_loop_rate=20.0,
                 er_loop_rate=5.0,
                 pose_loop_rate=10.0,
                 fusion_loop_rate=10.0,
                 send_loop_rate=2.0,
                 camera_loop_rate=20.0,
                 logging_loop_rate=20.0,
                 face_mesh_rate=1.0,
                 udp_ip='127.0.0.1',
                 udp_port=5006,
                 kafka_ip='127.0.0.1',
                 kafka_port=9092,
                 web_app_port=5000,
                 web_app_communication_port=5001,
                 kafka_topic_name='AffectToolbox',
                 sample_rate=16000,
                 vad_threshold=0.6,
                 face_padding=0.2,
                 microphone_chunks=16000,
                 microphone_id=0,
                 stt_window_length=10,
                 stt_model_size="base",
                 sentiment_model='germansentiment'
                 ):

        self.VAD_LOOP = enable_vad_loop
        self.SER_LOOP = enable_ser_loop
        self.STT_LOOP = enable_stt_loop
        self.SENTIMENT_LOOP = enable_sentiment_loop
        self.POSE_LOOP = enable_pose_loop
        self.FUSION_LOOP = enable_fusion_loop

        self.CAMERA_LOOP = enable_camera_loop
        self.PRINT_LOOP = enable_print_loop
        self.SEND_UDP_LOOP = enable_send_udp_loop
        self.SEND_KAFKA_LOOP = enable_send_kafka_loop
        self.FACE_ER_LOOP = enable_face_er_loop
        self.FACE_MESH_LOOP = enable_face_mesh_loop

        self.SHOW_FACE_MESH = show_face_mesh
        self.FACE_MESH_SHOW_FACE_EDGES = face_mesh_show_face_edges
        self.FACE_MESH_SHOW_FACE_PUPILS = face_mesh_show_face_pupils
        self.FACE_MESH_SHOW_FACE_CONTOUR = face_mesh_show_face_contour

        self.WEB_APP = enable_web_app
        self.WEB_APP_UDP_PORT = web_app_communication_port
        if self.WEB_APP:
            from res.unity_build.unity import start_web_app
            start_web_app(web_app_port)

        self.LOGGING_MODULE = LogModule(enable_vad_loop, enable_ser_loop, enable_stt_loop, enable_sentiment_loop,
                                        enable_face_er_loop, enable_pose_loop, enable_fusion_loop)

        self._SER_LOOP_RATE = ser_loop_rate
        self._STT_LOOP_RATE = stt_loop_rate
        self._SENTIMENT_LOOP_RATE = sentiment_loop_rate
        self._VAD_LOOP_RATE = vad_loop_rate
        self._SEND_LOOP_RATE = send_loop_rate
        self._CAMERA_LOOP_RATE = camera_loop_rate
        self._LOGGING_LOOP_RATE = logging_loop_rate
        self._ER_LOOP_RATE = er_loop_rate
        self._POSE_LOOP_RATE = pose_loop_rate
        self._FUSION_LOOP_RATE = fusion_loop_rate
        self._FM_LOOP_RATE = face_mesh_rate
        self._FC_LOOP_RATE = max(er_loop_rate, face_mesh_rate)

        self._STT_WINDOW_LENGTH = stt_window_length
        self._STT_MODEL_SIZE = stt_model_size
        self._VAD_THRESHOLD = vad_threshold

        self.MICROPHONE_CHUNKS = microphone_chunks
        self._MICROPHONE_ID = microphone_id

        self._CAMERA_ID = camera_id

        self._UDP_IP = udp_ip
        self._UDP_PORT = udp_port
        self._KAFKA_IP = kafka_ip
        self._KAFKA_PORT = kafka_port
        self._KAFKA_TOPIC_NAME = kafka_topic_name

        self.STEP = 1.0
        self.CHANNELS = 1

        self.FACE_PADDING = face_padding

        self.SAMPLE_RATE = sample_rate

        self.CHUNK_SIZE = int(self.STEP * self.SAMPLE_RATE)
        self._LAST_IMAGE = None

        # Initialize necessary modules
        if enable_vad_loop:
            from modules.module_vad import VoiceActivity
            self.VAD_MODULE = VoiceActivity(segment_length=480, sample_rate=16000, threshold=vad_threshold)
        if enable_ser_loop:
            from modules.module_ser import SpeechEmotion
            self.SER_MODULE = SpeechEmotion(self.SAMPLE_RATE)
        if enable_stt_loop:
            from modules.module_stt import SpeechToText
            self.STT_MODULE = SpeechToText(self.SAMPLE_RATE, self._STT_MODEL_SIZE)
        if enable_sentiment_loop:
            from modules.module_sentiment import Sentiment
            self.SENTIMENT_MODULE = Sentiment(model=sentiment_model)
        if enable_face_er_loop:
            from modules.module_ier import EmotionFromCam
            self.IER_MODULE = EmotionFromCam()
        if enable_pose_loop:
            from modules.module_pose import PoseFromCam
            self.POSE_MODULE = PoseFromCam()
        if enable_fusion_loop:
            from modules.module_fusion import FusionModule
            self.FUSION_MODULE = FusionModule()

        if self.VAD_LOOP or self.SER_LOOP or self.STT_LOOP:
            self.audio = pyaudio.PyAudio()
            self.stream = self.audio.open(input_device_index=self._MICROPHONE_ID,
                                          format=pyaudio.paFloat32,
                                          channels=self.CHANNELS,
                                          rate=self.SAMPLE_RATE,
                                          input=True,
                                          output=True,
                                          frames_per_buffer=self.CHUNK_SIZE)

        if self.CAMERA_LOOP or self.FACE_ER_LOOP or self.FACE_MESH_LOOP or self.POSE_LOOP:
            import mediapipe as mp
            self.cam_options = {"output_frame_size": 1,
                                "cam_id": self._CAMERA_ID}
            self.capture = cv2.VideoCapture(self.cam_options["cam_id"])

            self.video_shower_raw = VideoShow("Raw", 25, 100, 300, 300).start()
            self.video_shower_preprocessed = VideoShow("Preprocessed", 350, 100, 300, 300).start()
            self.video_shower_facemesh = VideoShow("FaceMesh", 675, 100, 300, 300).start()
            self.video_shower_pose = VideoShow("Pose", 1000, 100, 300, 300).start()

            self.mp_face_detection = mp.solutions.face_detection
            self.mp_mesh_detection = mp.solutions.face_mesh
            self.mp_face_mesh = self.mp_mesh_detection.FaceMesh(static_image_mode=True,
                                                                max_num_faces=1,
                                                                refine_landmarks=True,
                                                                min_detection_confidence=0.5)
            self.mp_drawing = mp.solutions.drawing_utils
            self.mp_drawing_styles = mp.solutions.drawing_styles
            self.mp_pose = mp.solutions.pose

            self.face_detection = self.mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

        self._SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self._SOCKET.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)

        if self.SEND_KAFKA_LOOP:
            try:
                from kafka import KafkaProducer
                kafka_adress = self._KAFKA_IP + ":" + str(self._KAFKA_PORT)
                self._KAFKA_PRODUCER = KafkaProducer(bootstrap_servers=kafka_adress,
                                                     value_serializer=lambda v: json.dumps(v).encode('utf-8'))
            except:
                print(colored("NO KAFKA SERVER RUNNING. DISABLE KAFKA OR START KAFKA SERVER AND RETRY.","red"))
                os._exit(1)

    def microphone_loop(self):
        data = self.stream.read(self.MICROPHONE_CHUNKS)
        signal = np.fromstring(data, np.float32)
        # signal = np.frombuffer(data, dtype=np.int16)
        signal_list = signal.tolist()

        for n in range(0, len(signal_list)):
            qs.AUDIO_QUEUE.append(signal_list[n])
        threading.Thread(target=self.microphone_loop).start()

    def vad_loop(self):
        time_vad_loop_start = time.time()
        signal = []
        local_audio = qs.AUDIO_QUEUE.copy()
        _LEN_VAD_SIGNAL = 1024
        m = (len(local_audio)) - _LEN_VAD_SIGNAL
        for i in range(0, _LEN_VAD_SIGNAL):
            signal.append(local_audio[m + i - 1])
        signal = np.asarray(signal, dtype=np.float32)
        is_speech = self.VAD_MODULE.process(signal)
        is_speech = 1 if is_speech == True else 0
        qs.VOICE_ACTIVITY.append(is_speech)
        seconds_vad_loop = time.time() - time_vad_loop_start
        vad_timer = 1.0 / float(self._VAD_LOOP_RATE) - seconds_vad_loop
        if vad_timer < 0.0:
            # print(colored('VAD frequency is too high to be maintained. Please lower it and start again.', 'blue'))
            self.LOGGING_MODULE.VOICE_OK = False
        else:
            self.LOGGING_MODULE.VOICE_OK = True

        self.LOGGING_MODULE.TRACKING_VOICE = is_speech and self.LOGGING_MODULE.VOICE_OK
        # os._exit(1)
        threading.Timer(vad_timer, self.vad_loop).start()

    def ser_loop(self):
        time_ser_loop_start = time.time()
        signal = []
        local_audio = qs.AUDIO_QUEUE.copy()
        m = (len(local_audio)) - self.SAMPLE_RATE
        for i in range(0, self.SAMPLE_RATE):
            signal.append(local_audio[m + i - 1])

        signal = np.asarray(signal, dtype=np.float32)
        ser_prediction, _ = self.SER_MODULE.process(signal.astype(np.float32), extract_embeddings=False)
        valence, arousal, dominance = (ser_prediction[0] * 2) - 1, (ser_prediction[1] * 2) - 1, (
                ser_prediction[2] * 2) - 1
        qs.VALENCE_SPEECH.append(valence)
        qs.AROUSAL_SPEECH.append(arousal)
        qs.DOMINANCE_SPEECH.append(dominance)
        seconds_ser_loop = time.time() - time_ser_loop_start
        # print(seconds_ser_loop)
        ser_timer = 1.0 / float(self._SER_LOOP_RATE) - seconds_ser_loop
        if ser_timer < 0.0:
            self.LOGGING_MODULE.SER_OK = False
        else:
            self.LOGGING_MODULE.SER_OK = True
        threading.Timer(ser_timer, self.ser_loop).start()

    def stt_loop(self):
        time_stt_loop_start = time.time()
        signal = []
        local_audio = qs.AUDIO_QUEUE.copy()

        m = int((len(local_audio)) - self._STT_WINDOW_LENGTH * self.SAMPLE_RATE)
        for i in range(0, int(self._STT_WINDOW_LENGTH) * self.SAMPLE_RATE):
            signal.append(local_audio[m + i - 1])

        signal = np.asarray(signal, dtype=np.float32)
        stt_prediction = self.STT_MODULE.process(signal.astype(np.float32))
        qs.TRANSCRIPT_SPEECH.append(stt_prediction)

        seconds_stt_loop = time.time() - time_stt_loop_start
        # print(seconds_stt_loop)
        stt_timer = 1.0 / float(self._STT_LOOP_RATE) - seconds_stt_loop
        if stt_timer < 0.0:
            self.LOGGING_MODULE.STT_OK = False
        else:
            self.LOGGING_MODULE.STT_OK = True
        threading.Timer(stt_timer, self.stt_loop).start()

    def sentiment_loop(self):
        time_sentiment_loop_start = time.time()
        last_text = qs.TRANSCRIPT_SPEECH[-1]

        prediction = self.SENTIMENT_MODULE.process(last_text)[0]
        # Remove magic numbers
        qs.POS_SENTIMENT.append(prediction[0][1])
        qs.NEG_SENTIMENT.append(prediction[1][1])
        qs.NEU_SENTIMENT.append(prediction[2][1])

        seconds_sentiment_loop = time.time() - time_sentiment_loop_start
        # print(seconds_sentiment_loop)

        sentiment_timer = 1.0 / float(self._SENTIMENT_LOOP_RATE) - seconds_sentiment_loop
        if sentiment_timer < 0.0:
            self.LOGGING_MODULE.SENTIMENT_OK = False
        else:
            self.LOGGING_MODULE.SENTIMENT_OK = True
        threading.Timer(sentiment_timer, self.sentiment_loop).start()

    def face_record_loop(self):
        global video_shower_raw
        time_camera_loop_start = time.time()
        ret, img_captured = self.capture.read()
        img = img_captured.copy()
        self.video_shower_raw.frame = img
        qs.RAW_IMAGE_QUEUE.append(img)

        seconds_camera_loop = time.time() - time_camera_loop_start
        camera_timer = 1.0 / float(self._CAMERA_LOOP_RATE) - seconds_camera_loop
        if camera_timer < 0.0:
            self.LOGGING_MODULE.CAMERA_OK = False
        else:
            self.LOGGING_MODULE.CAMERA_OK = True
        threading.Timer(camera_timer, self.face_record_loop).start()

    def face_crop_loop(self):
        global video_shower_preprocessed
        time_fc_loop_start = time.time()
        img = qs.RAW_IMAGE_QUEUE[len(qs.RAW_IMAGE_QUEUE) - 1]

        face_detection_results = self.face_detection.process(img[:, :, ::-1])

        found_face = False
        if face_detection_results.detections:
            found_face = True
            for face_no, face in enumerate(face_detection_results.detections):
                face_data = face.location_data

                img_h = img.shape[0]
                img_w = img.shape[1]

                origin_x = int(img_w * face_data.relative_bounding_box.xmin) - int(
                    self.FACE_PADDING * float(img_w) * float(face_data.relative_bounding_box.width))
                origin_y = int(img_h * face_data.relative_bounding_box.ymin) - int(
                    self.FACE_PADDING * float(img_h) * float(face_data.relative_bounding_box.height))

                origin_x = max(0, origin_x)
                origin_y = max(0, origin_y)

                bb_height = int(img_h * face_data.relative_bounding_box.height) + (
                        2 * int(self.FACE_PADDING * float(img_h) * float(face_data.relative_bounding_box.height)))
                bb_height = min(bb_height, img_h - origin_y)

                bb_width = int(img_h * face_data.relative_bounding_box.width) + (
                        2 * int(self.FACE_PADDING * float(img_w) * float(face_data.relative_bounding_box.width)))
                bb_width = min(bb_width, img_w - origin_x)

        if found_face == True:
            cropped_img = img[origin_y:origin_y + bb_height, origin_x:origin_x + bb_width]
            img = cropped_img

        if type(img) == np.ndarray:
            img2 = cv2.normalize(img, None, -1.0, 1.0, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
            self.video_shower_preprocessed.frame = (img2 + 1) / 2
        qs.FACE_CROP_QUEUE.append(img)

        seconds_fc_loop = time.time() - time_fc_loop_start
        fc_timer = 1.0 / float(self._FC_LOOP_RATE) - seconds_fc_loop
        if fc_timer < 0.0:
            self.LOGGING_MODULE.CAMERA_OK = False
        else:
            self.LOGGING_MODULE.CAMERA_OK = True

        self.LOGGING_MODULE.TRACKING_FACE = found_face and self.LOGGING_MODULE.CAMERA_OK

        threading.Timer(fc_timer, self.face_crop_loop).start()

    def face_er_loop(self):
        global video_shower_preprocessed
        time_er_loop_start = time.time()
        img = qs.FACE_CROP_QUEUE[len(qs.FACE_CROP_QUEUE) - 1]
        img = cv2.normalize(img, None, -1.0, 1.0, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

        if type(img) == np.ndarray:
            prediction = self.IER_MODULE.predict(img)
            qs.VALENCE_FACE.append(prediction[0][0])
            qs.AROUSAL_FACE.append(prediction[0][1])

        seconds_er_loop = time.time() - time_er_loop_start
        er_timer = 1.0 / float(self._ER_LOOP_RATE) - seconds_er_loop
        if er_timer < 0.0:
            self.LOGGING_MODULE.CAMERA_OK = False
        else:
            self.LOGGING_MODULE.CAMERA_OK = True
        threading.Timer(er_timer, self.face_er_loop).start()

    def face_mesh_loop(self):
        time_fm_loop_start = time.time()
        img = qs.FACE_CROP_QUEUE[len(qs.FACE_CROP_QUEUE) - 1]
        results = self.mp_face_mesh.process(img)

        if results.multi_face_landmarks is None:
            pass
        else:
            if self.SHOW_FACE_MESH:
                annotated_image = np.zeros_like(img)
                for face_landmarks in results.multi_face_landmarks:
                    qs.FACE_MESH_QUEUE.append(face_landmarks.landmark)
                    # print('face_landmarks:', face_landmarks)
                    if self.FACE_MESH_SHOW_FACE_EDGES:
                        self.mp_drawing.draw_landmarks(
                            image=annotated_image,
                            landmark_list=face_landmarks,
                            connections=self.mp_mesh_detection.FACEMESH_TESSELATION,
                            landmark_drawing_spec=None,
                            connection_drawing_spec=self.mp_drawing_styles
                            .get_default_face_mesh_tesselation_style())
                    if self.FACE_MESH_SHOW_FACE_CONTOUR:
                        self.mp_drawing.draw_landmarks(
                            image=annotated_image,
                            landmark_list=face_landmarks,
                            connections=self.mp_mesh_detection.FACEMESH_CONTOURS,
                            landmark_drawing_spec=None,
                            connection_drawing_spec=self.mp_drawing_styles
                            .get_default_face_mesh_contours_style())
                    if self.FACE_MESH_SHOW_FACE_PUPILS:
                        self.mp_drawing.draw_landmarks(
                            image=annotated_image,
                            landmark_list=face_landmarks,
                            connections=self.mp_mesh_detection.FACEMESH_IRISES,
                            landmark_drawing_spec=None,
                            connection_drawing_spec=self.mp_drawing_styles
                            .get_default_face_mesh_iris_connections_style())
                self.video_shower_facemesh.frame = annotated_image

        seconds_fm_loop = time.time() - time_fm_loop_start
        fm_timer = 1.0 / float(self._FM_LOOP_RATE) - seconds_fm_loop
        if fm_timer < 0.0:
            self.LOGGING_MODULE.CAMERA_OK = False
        else:
            self.LOGGING_MODULE.CAMERA_OK = True
        threading.Timer(fm_timer, self.face_mesh_loop).start()

    def pose_loop(self):
        global video_shower_pose

        time_pose_loop_start = time.time()

        img = qs.RAW_IMAGE_QUEUE[len(qs.RAW_IMAGE_QUEUE) - 1]
        self.POSE_MODULE.predict(img)

        self.video_shower_pose.frame = self.POSE_MODULE.image

        seconds_pose_loop = time.time() - time_pose_loop_start
        pose_timer = 1.0 / float(self._POSE_LOOP_RATE) - seconds_pose_loop
        if pose_timer < 0.0:
            self.LOGGING_MODULE.BODY_OK = False
        else:
            self.LOGGING_MODULE.BODY_OK = True

        self.LOGGING_MODULE.TRACKING_BODY = self.LOGGING_MODULE.CAMERA_OK and self.LOGGING_MODULE.BODY_OK and self.POSE_MODULE.tracking

        threading.Timer(pose_timer, self.pose_loop).start()

    def fusion_loop(self):
        time_fusion_loop_start = time.time()

        fusion_result = self.FUSION_MODULE.update_fusion()
        qs.FUSION.append(fusion_result)

        seconds_fusion_loop = time.time() - time_fusion_loop_start
        fusion_timer = 1.0 / float(self._FUSION_LOOP_RATE) - seconds_fusion_loop
        threading.Timer(fusion_timer, self.fusion_loop).start()

    def print_loop(self):
        v_s = qs.VALENCE_SPEECH[len(qs.VALENCE_SPEECH) - 1]
        a_s = qs.AROUSAL_SPEECH[len(qs.AROUSAL_SPEECH) - 1]
        d_s = qs.DOMINANCE_SPEECH[len(qs.DOMINANCE_SPEECH) - 1]
        t_s = qs.TRANSCRIPT_SPEECH[len(qs.TRANSCRIPT_SPEECH) - 1]
        s_pos = qs.POS_SENTIMENT[-1]
        s_neu = qs.NEU_SENTIMENT[-1]
        s_neg = qs.NEG_SENTIMENT[-1]
        vad = qs.VOICE_ACTIVITY[len(qs.VOICE_ACTIVITY) - 1]
        v_f = qs.VALENCE_FACE[len(qs.VALENCE_FACE) - 1]
        a_f = qs.AROUSAL_FACE[len(qs.AROUSAL_FACE) - 1]
        d_f = qs.DOMINANCE_FACE[len(qs.DOMINANCE_FACE) - 1]
        m_f = qs.FUSION[len(qs.FUSION) - 1]
        p = ''
        if self.POSE_LOOP:
            p = self.POSE_MODULE.value_string

        analysis_values = {'vad': vad,
                           'v_s': v_s,
                           'a_s': a_s,
                           'd_s': d_s,
                           't_s': t_s,
                           's_pos': s_pos,
                           's_neu': s_neu,
                           's_neg': s_neg,
                           'v_f': v_f,
                           'a_f': a_f,
                           'd_f': d_f,
                           'm_f': m_f,
                           'p': p
                           }

        self.LOGGING_MODULE.update_analysis(analysis_values)
        threading.Timer(0.05, self.print_loop).start()

    def send_loop(self):
        time_send_loop_start = time.time()
        v_s = qs.VALENCE_SPEECH[len(qs.VALENCE_SPEECH) - 1]
        a_s = qs.AROUSAL_SPEECH[len(qs.AROUSAL_SPEECH) - 1]
        d_s = qs.DOMINANCE_SPEECH[len(qs.DOMINANCE_SPEECH) - 1]
        t_s = qs.TRANSCRIPT_SPEECH[len(qs.TRANSCRIPT_SPEECH) - 1]
        s_pos = qs.POS_SENTIMENT[-1]
        s_neu = qs.NEU_SENTIMENT[-1]
        s_neg = qs.NEG_SENTIMENT[-1]
        vad = qs.VOICE_ACTIVITY[len(qs.VOICE_ACTIVITY) - 1]
        v_f = qs.VALENCE_FACE[len(qs.VALENCE_FACE) - 1]
        a_f = qs.AROUSAL_FACE[len(qs.AROUSAL_FACE) - 1]
        face_mesh_raw = qs.FACE_MESH_QUEUE[len(qs.FACE_MESH_QUEUE) - 1]
        m_f = qs.FUSION[len(qs.FUSION) - 1]
        face_mesh = ""
        i = 0
        if isinstance(face_mesh_raw, str):
            face_mesh = ""
        else:
            for lm in face_mesh_raw:
                if i == 0:
                    face_mesh += str(lm.x)
                    face_mesh += "#" + str(lm.y)
                    face_mesh += "#" + str(lm.z)
                else:
                    face_mesh += "#" + str(lm.x)
                    face_mesh += "#" + str(lm.y)
                    face_mesh += "#" + str(lm.z)
                i += 1

        E = lxml.builder.ElementMaker()
        ROOT = E.root
        DOC = E.doc
        V_S = E.v_s
        A_S = E.a_s
        D_S = E.d_s
        VAD = E.vad
        V_F = E.v_f
        A_F = E.a_f
        FACE_MESH = E.face_mesh
        M_F = E.m_f
        T_S = E.t_s
        S_POS = E.s_pos
        S_NEU = E.s_neu
        S_NEG = E.s_neg
        the_doc = ROOT(
            DOC(
                V_S(str(v_s), name='Valence Speech'),
                A_S(str(a_s), name='Arousal Speech'),
                D_S(str(d_s), name='Dominance Speech'),
                VAD(str(vad), name='Voice Activity'),
                V_F(str(v_f), name='Valence Face'),
                A_F(str(a_f), name='Arousal Face'),
                M_F(str(m_f), name='Fusion'),
                FACE_MESH(face_mesh, name='Face Mesh'),
                T_S(str(t_s), name='Transcript'),
                S_POS(str(s_pos), name='Sentiment positive'),
                S_NEU(str(s_neu), name='Sentiment neutral'),
                S_NEG(str(s_neg), name='Sentiment negative')

            )
        )
        command = lxml.etree.tostring(the_doc)
        if self.SEND_UDP_LOOP:
            self._SOCKET.sendto(command, (self._UDP_IP, self._UDP_PORT))
        if self.WEB_APP:
            self._SOCKET.sendto(command, (self._UDP_IP, self.WEB_APP_UDP_PORT))
        if self.SEND_KAFKA_LOOP:
            string_from_byte = str({'pleasure': m_f[0],
                                    'arousal': m_f[1],
                                    'dominance': m_f[2]})
            self._KAFKA_PRODUCER.send(self._KAFKA_TOPIC_NAME, string_from_byte)
        seconds_send_loop = time.time() - time_send_loop_start
        send_timer = 1.0 / float(self._SEND_LOOP_RATE) - seconds_send_loop
        if send_timer < 0.0:
            # print(colored('\nSEND frequency is too high to be maintained. Please lower it and start again.', 'blue'))
            # os._exit(1)
            pass
        threading.Timer(send_timer, self.send_loop).start()

    def start(self):
        if self.VAD_LOOP or self.SER_LOOP or self.STT_LOOP:
            self.microphone_loop()
        if self.CAMERA_LOOP or self.FACE_ER_LOOP or self.FACE_MESH_LOOP or self.POSE_LOOP:
            self.face_record_loop()
            time.sleep(1)
            self.face_crop_loop()

        time.sleep(2)

        if self.FACE_ER_LOOP:
            self.face_er_loop()
        if self.POSE_LOOP:
            self.pose_loop()
        if self.VAD_LOOP:
            self.vad_loop()
        if self.SER_LOOP:
            self.ser_loop()
        if self.STT_LOOP:
            self.stt_loop()
        if self.SENTIMENT_LOOP:
            self.sentiment_loop()
        if self.SEND_UDP_LOOP or self.SEND_KAFKA_LOOP or self.WEB_APP:
            self.send_loop()
        if self.PRINT_LOOP:
            self.print_loop()
        if self.FACE_MESH_LOOP:
            self.face_mesh_loop()

        time.sleep(0.5)

        if self.FUSION_LOOP:
            self.fusion_loop()


if __name__ == "__main__":
    pipe = AffectPipeline()
    pipe.microphone_loop()
    # pipe.camera_loop()
    pipe.face_record_loop()

    time.sleep(6)

    # pipe.face_er_loop()
    pipe.vad_loop()
    pipe.ser_loop()
    pipe.stt_loop()

    pipe.send_loop()
    pipe.print_loop()
