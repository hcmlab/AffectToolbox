from config_defaults import DEFAULT_PARAMETERS
import time
import numpy as np
import pyaudio
import threading
import cv2
import math
from modules.Logger import LogModule
import socket
import lxml.etree
import lxml.builder
from termcolor import colored
import os
import modules.QueueSystem as qs
import json

class AffectPipeline():
    _LOOP_THREADS = (
        "microphone_loop_thread", "vad_loop_thread", "ser_loop_thread",
        "stt_loop_thread", "sentiment_loop_thread", "face_record_loop_thread",
        "face_crop_loop_thread", "face_er_loop_thread", "face_mesh_loop_thread",
        "pose_loop_thread", "fusion_loop_thread", "print_loop_thread", "send_loop_thread",
    )

    def __init__(self,
                 enable_log_to_console=DEFAULT_PARAMETERS["enable_log_to_console"],
                 enable_vad_loop=DEFAULT_PARAMETERS["enable_voiceactivity"],
                 enable_ser_loop=DEFAULT_PARAMETERS["enable_paralinguistic"],
                 enable_stt_loop=DEFAULT_PARAMETERS["enable_transcript"],
                 enable_camera_loop=DEFAULT_PARAMETERS["enable_camera"],
                 enable_print_loop=DEFAULT_PARAMETERS["enable_print_loop"],
                 enable_send_udp_loop=DEFAULT_PARAMETERS["enable_udp"],
                 enable_send_kafka_loop=DEFAULT_PARAMETERS["enable_kafka"],
                 enable_face_er_loop=DEFAULT_PARAMETERS["enable_facialexpression"],
                 enable_face_mesh_loop=DEFAULT_PARAMETERS["enable_face_mesh_loop"],
                 enable_pose_loop=DEFAULT_PARAMETERS["enable_skeleton"],
                 enable_fusion_loop=DEFAULT_PARAMETERS["enable_fusion"],
                 enable_sentiment_loop=DEFAULT_PARAMETERS["enable_sentiment"],
                 show_face_mesh=DEFAULT_PARAMETERS["show_face_mesh"],
                 face_mesh_show_face_edges=DEFAULT_PARAMETERS["face_mesh_show_face_edges"],
                 face_mesh_show_face_pupils=DEFAULT_PARAMETERS["face_mesh_show_face_pupils"],
                 face_mesh_show_face_contour=DEFAULT_PARAMETERS["face_mesh_show_face_contour"],
                 camera_id=DEFAULT_PARAMETERS["camera_id"],
                 ser_loop_rate=DEFAULT_PARAMETERS["SER_LOOP_RATE"],
                 ser_valence_offset=DEFAULT_PARAMETERS["SER_VALENCE_OFFSET"],
                 ser_arousal_offset=DEFAULT_PARAMETERS["SER_AROUSAL_OFFSET"],
                 ser_dominance_offset=DEFAULT_PARAMETERS["SER_DOMINANCE_OFFSET"],
                 stt_loop_rate=DEFAULT_PARAMETERS["STT_LOOP_RATE"],
                 sentiment_loop_rate=DEFAULT_PARAMETERS["SENTIMENT_LOOP_RATE"],
                 vad_loop_rate=DEFAULT_PARAMETERS["VAD_LOOP_RATE"],
                 er_loop_rate=DEFAULT_PARAMETERS["ER_LOOP_RATE"],
                 pose_loop_rate=DEFAULT_PARAMETERS["POSE_LOOP_RATE"],
                 fusion_loop_rate=DEFAULT_PARAMETERS["FUSION_LOOP_RATE"],
                 send_loop_rate=DEFAULT_PARAMETERS["SEND_LOOP_RATE"],
                 camera_loop_rate=DEFAULT_PARAMETERS["CAMERA_LOOP_RATE"],
                 logging_loop_rate=DEFAULT_PARAMETERS["logging_loop_rate"],
                 face_mesh_rate=DEFAULT_PARAMETERS["FACE_MESH_RATE"],
                 udp_ip=DEFAULT_PARAMETERS["UDP_IP"],
                 udp_port=DEFAULT_PARAMETERS["UDP_PORT"],
                 kafka_ip=DEFAULT_PARAMETERS["KAFKA_IP"],
                 kafka_port=DEFAULT_PARAMETERS["KAFKA_PORT"],
                 kafka_topic_name=DEFAULT_PARAMETERS["KAFKA_TOPIC"],
                 sample_rate=DEFAULT_PARAMETERS["SAMPLE_RATE"],
                 vad_threshold=DEFAULT_PARAMETERS["VAD_THRESHOLD"],
                 face_padding=DEFAULT_PARAMETERS["FACE_PADDING"],
                 microphone_chunks=DEFAULT_PARAMETERS["MIC_CHUNKS"],
                 microphone_id=DEFAULT_PARAMETERS["microphone_id"],
                 stt_window_length=DEFAULT_PARAMETERS["STT_WINDOW_SIZE"],
                 stt_model_size=DEFAULT_PARAMETERS["stt_model_size"],
                 sentiment_model=DEFAULT_PARAMETERS["sentiment_model"],
                 fusion_use_para_v=DEFAULT_PARAMETERS["fusion_use_para_v"],
                 fusion_use_para_a=DEFAULT_PARAMETERS["fusion_use_para_a"],
                 fusion_use_para_d=DEFAULT_PARAMETERS["fusion_use_para_d"],
                 fusion_use_sentiment_v=DEFAULT_PARAMETERS["fusion_use_sentiment_v"],
                 fusion_use_face_v=DEFAULT_PARAMETERS["fusion_use_face_v"],
                 fusion_use_face_a=DEFAULT_PARAMETERS["fusion_use_face_a"],
                 fusion_use_face_d=DEFAULT_PARAMETERS["fusion_use_face_d"],
                 fusion_use_pose_d=DEFAULT_PARAMETERS["fusion_use_pose_d"],
                 fusion_speed=DEFAULT_PARAMETERS["FUSION_SPEED"],
                 fusion_voice_speed = DEFAULT_PARAMETERS["FUSION_VOICE_SPEED"],
                 fusion_voice_valence_weight = DEFAULT_PARAMETERS["FUSION_VOICE_VALENCE_WEIGHT"],
                 fusion_voice_valence_boost = DEFAULT_PARAMETERS["FUSION_VOICE_VALENCE_BOOST"],
                 fusion_voice_arousal_weight = DEFAULT_PARAMETERS["FUSION_VOICE_AROUSAL_WEIGHT"],
                 fusion_voice_arousal_boost = DEFAULT_PARAMETERS["FUSION_VOICE_AROUSAL_BOOST"],
                 fusion_voice_dominance_weight = DEFAULT_PARAMETERS["FUSION_VOICE_DOMINANCE_WEIGHT"],
                 fusion_voice_dominance_boost = DEFAULT_PARAMETERS["FUSION_VOICE_DOMINANCE_BOOST"],
                 fusion_face_speed = DEFAULT_PARAMETERS["FUSION_FACE_SPEED"],
                 fusion_face_valence_weight = DEFAULT_PARAMETERS["FUSION_FACE_VALENCE_WEIGHT"],
                 fusion_face_valence_boost = DEFAULT_PARAMETERS["FUSION_FACE_VALENCE_BOOST"],
                 fusion_face_arousal_weight = DEFAULT_PARAMETERS["FUSION_FACE_AROUSAL_WEIGHT"],
                 fusion_face_arousal_boost = DEFAULT_PARAMETERS["FUSION_FACE_AROUSAL_BOOST"],
                 fusion_face_dominance_weight = DEFAULT_PARAMETERS["FUSION_FACE_DOMINANCE_WEIGHT"],
                 fusion_face_dominance_boost = DEFAULT_PARAMETERS["FUSION_FACE_DOMINANCE_BOOST"],
                 fusion_sentiment_speed = DEFAULT_PARAMETERS["FUSION_SENTIMENT_SPEED"],
                 fusion_sentiment_weight = DEFAULT_PARAMETERS["FUSION_SENTIMENT_WEIGHT"],
                 fusion_sentiment_boost = DEFAULT_PARAMETERS["FUSION_SENTIMENT_BOOST"],
                 fusion_pose_speed = DEFAULT_PARAMETERS["FUSION_POSE_SPEED"],
                 fusion_pose_dominance_weight = DEFAULT_PARAMETERS["FUSION_POSE_DOMINANCE_WEIGHT"],
                 fusion_pose_dominance_boost = DEFAULT_PARAMETERS["FUSION_POSE_DOMINANCE_BOOST"]
                 ):

        self._stop_event = threading.Event()
        self._worker_lock = threading.Lock()
        self._shutdown_lock = threading.Lock()
        self._workers = set()
        self._started = False
        self.stop_thread = False
        for name in self._LOOP_THREADS:
            setattr(self, name, None)
        self.capture = None
        self.stream = None
        self.audio = None
        self._SOCKET = None
        self._KAFKA_PRODUCER = None
        self.face_detection = None
        self.mp_face_mesh = None
        self.POSE_MODULE = None

        self.LOG_TO_CONSOLE = enable_log_to_console
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
        self._face_mesh_detected = False

        self.SHOW_FACE_MESH = show_face_mesh
        self.FACE_MESH_SHOW_FACE_EDGES = face_mesh_show_face_edges
        self.FACE_MESH_SHOW_FACE_PUPILS = face_mesh_show_face_pupils
        self.FACE_MESH_SHOW_FACE_CONTOUR = face_mesh_show_face_contour

        self._SER_LOOP_RATE = ser_loop_rate
        self.SER_VALENCE_OFFSET = ser_valence_offset
        self.SER_AROUSAL_OFFSET = ser_arousal_offset
        self.SER_DOMINANCE_OFFSET = ser_dominance_offset
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

        # self.FUSION_USE_PARA_V = fusion_use_para_v
        # self.FUSION_USE_PARA_A = fusion_use_para_a
        # self.FUSION_USE_PARA_D = fusion_use_para_d
        # self.FUSION_USE_SENTIMENT_V = fusion_use_sentiment_v
        # self.FUSION_USE_FACE_V = fusion_use_face_v
        # self.FUSION_USE_FACE_A = fusion_use_face_a
        # self.FUSION_USE_FACE_D = fusion_use_face_d
        # self.FUSION_USE_POSE_D = fusion_use_pose_d

        self.LOGGING_MODULE = LogModule(enable_log_to_console, enable_vad_loop, enable_ser_loop, enable_stt_loop,
                                        enable_sentiment_loop, enable_face_er_loop, enable_face_mesh_loop,
                                        enable_pose_loop, enable_fusion_loop)

        try:
            # Initialize necessary modules
            if enable_fusion_loop:
                from modules.module_fusion import FusionModule
                self.FUSION_MODULE = FusionModule()

                self.FUSION_MODULE.FUSION_USE_PARA_V = fusion_use_para_v
                self.FUSION_MODULE.FUSION_USE_PARA_A = fusion_use_para_a
                self.FUSION_MODULE.FUSION_USE_PARA_D = fusion_use_para_d
                self.FUSION_MODULE.FUSION_USE_SENTIMENT_V = fusion_use_sentiment_v
                self.FUSION_MODULE.FUSION_USE_FACE_V = fusion_use_face_v
                self.FUSION_MODULE.FUSION_USE_FACE_A = fusion_use_face_a
                self.FUSION_MODULE.FUSION_USE_FACE_D = fusion_use_face_d
                self.FUSION_MODULE.FUSION_USE_POSE_D = fusion_use_pose_d

                self.FUSION_MODULE.fusion_speed = fusion_speed

                self.FUSION_MODULE.voice_speed = fusion_voice_speed
                self.FUSION_MODULE.voice_weight_valence = fusion_voice_valence_weight
                self.FUSION_MODULE.voice_boost_valence = fusion_voice_valence_boost
                self.FUSION_MODULE.voice_weight_arousal = fusion_voice_arousal_weight
                self.FUSION_MODULE.voice_boost_arousal = fusion_voice_arousal_boost
                self.FUSION_MODULE.voice_weight_dominance = fusion_voice_dominance_weight
                self.FUSION_MODULE.voice_boost_dominance = fusion_voice_dominance_boost

                self.FUSION_MODULE.face_speed = fusion_face_speed
                self.FUSION_MODULE.face_weight_valence = fusion_face_valence_weight
                self.FUSION_MODULE.face_boost_valence = fusion_face_valence_boost
                self.FUSION_MODULE.face_weight_arousal = fusion_face_arousal_weight
                self.FUSION_MODULE.face_boost_arousal = fusion_face_arousal_boost
                self.FUSION_MODULE.face_weight_dominance = fusion_face_dominance_weight
                self.FUSION_MODULE.face_boost_dominance = fusion_face_dominance_boost

                self.FUSION_MODULE.sentiment_speed = fusion_sentiment_speed
                self.FUSION_MODULE.sentiment_weight_valence = fusion_sentiment_weight
                self.FUSION_MODULE.sentiment_boost_valence = fusion_sentiment_boost

                self.FUSION_MODULE.pose_speed = fusion_pose_speed
                self.FUSION_MODULE.pose_weight_dominance = fusion_pose_dominance_weight
                self.FUSION_MODULE.pose_boost_dominance = fusion_pose_dominance_boost
            if enable_vad_loop:
                from modules.module_vad import VoiceActivity
                self.VAD_MODULE = VoiceActivity(sample_rate=self.SAMPLE_RATE, threshold=vad_threshold)
                if enable_fusion_loop:
                    self.FUSION_MODULE.voice_activity_tracked = True
            else:
                self.LOGGING_MODULE.TRACKING_VOICE = True
                if enable_fusion_loop:
                    self.FUSION_MODULE.voice_activity_tracked = False
            if enable_ser_loop:
                from modules.module_ser import SpeechEmotion
                self.SER_MODULE = SpeechEmotion(self.SAMPLE_RATE, self.SER_VALENCE_OFFSET, self.SER_AROUSAL_OFFSET, self.SER_DOMINANCE_OFFSET)
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

                from mediapipe.tasks.python.vision import drawing_utils, drawing_styles
                self.mp = mp
                self.mp_mesh_detection = mp.tasks.vision.FaceLandmarksConnections
                self.mp_drawing = drawing_utils
                self.mp_drawing_styles = drawing_styles
                self.face_detection = mp.tasks.vision.FaceDetector.create_from_options(
                    mp.tasks.vision.FaceDetectorOptions(
                        base_options=mp.tasks.BaseOptions(model_asset_path='res/face_model/face_detector.tflite'),
                        min_detection_confidence=0.5))
                if self.FACE_MESH_LOOP:
                    self.mp_face_mesh = mp.tasks.vision.FaceLandmarker.create_from_options(
                        mp.tasks.vision.FaceLandmarkerOptions(
                            base_options=mp.tasks.BaseOptions(model_asset_path='res/face_model/face_landmarker.task'),
                            num_faces=1, min_face_detection_confidence=0.5))

            self._SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            self._SOCKET.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)

            if self.SEND_KAFKA_LOOP:
                try:
                    from kafka import KafkaProducer
                    kafka_adress = self._KAFKA_IP + ":" + str(self._KAFKA_PORT)
                    self._KAFKA_PRODUCER = KafkaProducer(bootstrap_servers=kafka_adress,
                                                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
                except Exception as error:
                    raise RuntimeError("Could not connect to Kafka. Check the server or disable Kafka.") from error
                    
        except Exception:
            self.stop()
            raise

    def _start_worker(self, name, worker):
        with self._worker_lock:
            if self._stop_event.is_set():
                return
            setattr(self, name, worker)
            self._workers.add(worker)
            try:
                worker.start()
            except Exception:
                self._workers.discard(worker)
                setattr(self, name, None)
                raise

    def _schedule_loop(self, name, delay, callback):
        worker = threading.Timer(max(0.0, delay), self._run_loop, args=(callback,))
        worker.daemon = True
        self._start_worker(name, worker)

    def _run_loop(self, callback):
        try:
            if not self._stop_event.is_set():
                callback()
        except Exception:
            if not self._stop_event.is_set():
                raise
        finally:
            with self._worker_lock:
                self._workers.discard(threading.current_thread())

    def microphone_loop(self):
        worker = threading.Thread(target=self._run_loop, args=(self.microphone_loop_func,), daemon=True)
        self._start_worker("microphone_loop_thread", worker)

    def microphone_loop_func(self):
        while not self._stop_event.is_set():
            # Wait for buffered samples so shutdown does not block in stream.read().
            if self.stream.get_read_available() < self.MICROPHONE_CHUNKS:
                self._stop_event.wait(0.01)
                continue
            data = self.stream.read(self.MICROPHONE_CHUNKS, exception_on_overflow=False)
            if self._stop_event.is_set():
                break
            signal = np.frombuffer(data, dtype=np.float32)
            qs.AUDIO_QUEUE.extend(signal.tolist())

    def vad_loop(self):
        if self._stop_event.is_set():
            return
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
        self._schedule_loop("vad_loop_thread", vad_timer, self.vad_loop)

    def ser_loop(self):
        if self._stop_event.is_set():
            return
        time_ser_loop_start = time.time()
        signal = []
        local_audio = qs.AUDIO_QUEUE.copy()
        m = (len(local_audio)) - self.SAMPLE_RATE
        for i in range(0, self.SAMPLE_RATE):
            signal.append(local_audio[m + i - 1])

        signal = np.asarray(signal, dtype=np.float32)
        ser_prediction, _ = self.SER_MODULE.process(signal.astype(np.float32), extract_embeddings=False)
        valence, arousal, dominance = ser_prediction[0], ser_prediction[1], ser_prediction[2]
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
        self._schedule_loop("ser_loop_thread", ser_timer, self.ser_loop)

    def stt_loop(self):
        if self._stop_event.is_set():
            return
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
        self._schedule_loop("stt_loop_thread", stt_timer, self.stt_loop)

    def sentiment_loop(self):
        if self._stop_event.is_set():
            return
        time_sentiment_loop_start = time.time()
        last_text = qs.TRANSCRIPT_SPEECH[-1]

        prediction = self.SENTIMENT_MODULE.process(last_text)[0]
        # Remove magic numbers
        qs.POS_SENTIMENT.append(prediction[0][1])
        qs.NEG_SENTIMENT.append(prediction[1][1])
        qs.NEU_SENTIMENT.append(prediction[2][1])

        qs.VALENCE_SENTIMENT.append(prediction[0][1] - prediction[1][1])

        seconds_sentiment_loop = time.time() - time_sentiment_loop_start
        # print(seconds_sentiment_loop)

        sentiment_timer = 1.0 / float(self._SENTIMENT_LOOP_RATE) - seconds_sentiment_loop
        if sentiment_timer < 0.0:
            self.LOGGING_MODULE.SENTIMENT_OK = False
        else:
            self.LOGGING_MODULE.SENTIMENT_OK = True
        self._schedule_loop("sentiment_loop_thread", sentiment_timer, self.sentiment_loop)

    def face_record_loop(self):
        if self._stop_event.is_set():
            return
        time_camera_loop_start = time.time()
        ret, img_captured = self.capture.read()
        if self._stop_event.is_set():
            return
        if not ret or img_captured is None:
            self.LOGGING_MODULE.CAMERA_OK = False
            self._schedule_loop("face_record_loop_thread", 1.0 / self._CAMERA_LOOP_RATE, self.face_record_loop)
            return
        img = img_captured.copy()
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # added RGB conversion
        qs.IMAGE_FACE_RAW.append(img_rgb)

        seconds_camera_loop = time.time() - time_camera_loop_start
        camera_timer = 1.0 / float(self._CAMERA_LOOP_RATE) - seconds_camera_loop
        if camera_timer < 0.0:
            self.LOGGING_MODULE.CAMERA_OK = False
        else:
            self.LOGGING_MODULE.CAMERA_OK = True
        self._schedule_loop("face_record_loop_thread", camera_timer, self.face_record_loop)

    def face_crop_loop(self):
        if self._stop_event.is_set():
            return
        time_fc_loop_start = time.time()
        if len(qs.IMAGE_FACE_RAW) == 0:
            self._schedule_loop("face_crop_loop_thread", 1.0 / self._FC_LOOP_RATE, self.face_crop_loop)
            return
        img = qs.IMAGE_FACE_RAW[len(qs.IMAGE_FACE_RAW) - 1]

        image = self.mp.Image(image_format=self.mp.ImageFormat.SRGB, data=np.ascontiguousarray(img))
        face_detection_results = self.face_detection.detect(image)

        found_face = False
        if face_detection_results.detections:
            found_face = True
            for face_no, face in enumerate(face_detection_results.detections):
                face_data = face.bounding_box

                img_h = img.shape[0]
                img_w = img.shape[1]

                origin_x = int(face_data.origin_x) - int(
                    self.FACE_PADDING * float(face_data.width))
                origin_y = int(face_data.origin_y) - int(
                    self.FACE_PADDING * float(face_data.height))

                origin_x = max(0, origin_x)
                origin_y = max(0, origin_y)

                bb_height = int(face_data.height) + (
                        2 * int(self.FACE_PADDING * float(face_data.height)))
                bb_height = min(bb_height, img_h - origin_y)

                bb_width = int(face_data.width) + (
                        2 * int(self.FACE_PADDING * float(face_data.width)))
                bb_width = min(bb_width, img_w - origin_x)

        if found_face:
            cropped_img = img[origin_y:origin_y + bb_height, origin_x:origin_x + bb_width]
            qs.IMAGE_FACE_PREPROCESSED.append(cropped_img)
        else:
            self._face_mesh_detected = False
        qs.FACE_ACTIVITY.append(float(found_face))

        seconds_fc_loop = time.time() - time_fc_loop_start
        fc_timer = 1.0 / float(self._FC_LOOP_RATE) - seconds_fc_loop
        if fc_timer < 0.0:
            self.LOGGING_MODULE.CAMERA_OK = False
        else:
            self.LOGGING_MODULE.CAMERA_OK = True

        self.LOGGING_MODULE.TRACKING_FACE = found_face and self.LOGGING_MODULE.CAMERA_OK

        self._schedule_loop("face_crop_loop_thread", fc_timer, self.face_crop_loop)

    def face_er_loop(self):
        if self._stop_event.is_set():
            return
        time_er_loop_start = time.time()
        if qs.FACE_ACTIVITY[-1] and len(qs.IMAGE_FACE_PREPROCESSED) > 0:
            img = qs.IMAGE_FACE_PREPROCESSED[len(qs.IMAGE_FACE_PREPROCESSED) - 1]
            img = cv2.normalize(img, None, -1.0, 1.0, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

            if type(img) == np.ndarray:
                prediction = self.IER_MODULE.predict(img)
                qs.VALENCE_FACE.append(prediction[0][0])
                qs.AROUSAL_FACE.append(prediction[0][1])

                # DERIVE PERCEIVED DOMINANCE FROM VALENCE/AROUSAL
                dominance_face_latest = 0.0
                valence_face_latest = prediction[0][0]
                arousal_face_latest = prediction[0][1]

                if arousal_face_latest < 0.0:
                    dominance_face_latest = -1.0
                elif arousal_face_latest > 0.5:
                    dominance_face_latest = 1.0
                elif abs(valence_face_latest) > (-2.0 * arousal_face_latest + 1.0):
                    dominance_face_latest = 1.0
                else:
                    dominance_face_latest = -1.0

                # NORMALIZE PERCEIVED DOMINANCE
                if dominance_face_latest == 1.0:
                    dominance_face_latest = (math.sqrt(
                        math.pow(valence_face_latest, 2.0) + math.pow(arousal_face_latest, 2.0))) / 1.4
                else:
                    dominance_face_latest = (math.sqrt(
                        math.pow(valence_face_latest, 2.0) + math.pow(arousal_face_latest, 2.0))) / -1.4

                # FACE - PERCEIVED DOMINANCE
                qs.DOMINANCE_FACE.append(dominance_face_latest)

        seconds_er_loop = time.time() - time_er_loop_start
        er_timer = 1.0 / float(self._ER_LOOP_RATE) - seconds_er_loop
        if er_timer < 0.0:
            self.LOGGING_MODULE.CAMERA_OK = False
        else:
            self.LOGGING_MODULE.CAMERA_OK = True
        self._schedule_loop("face_er_loop_thread", er_timer, self.face_er_loop)

    def face_mesh_loop(self):
        if self._stop_event.is_set():
            return
        time_fm_loop_start = time.time()
        if qs.FACE_ACTIVITY[-1] and len(qs.IMAGE_FACE_PREPROCESSED) > 0:
            img = qs.IMAGE_FACE_PREPROCESSED[len(qs.IMAGE_FACE_PREPROCESSED) - 1]
            image = self.mp.Image(image_format=self.mp.ImageFormat.SRGB, data=np.ascontiguousarray(img))
            results = self.mp_face_mesh.detect(image)
            self._face_mesh_detected = bool(results.face_landmarks)

            if self._face_mesh_detected:
                for face_landmarks in results.face_landmarks:
                    qs.FACE_MESH_QUEUE.append(face_landmarks)

            if self._face_mesh_detected and self.SHOW_FACE_MESH:
                annotated_image = np.zeros_like(img)
                for face_landmarks in results.face_landmarks:
                    if self.FACE_MESH_SHOW_FACE_EDGES:
                        self.mp_drawing.draw_landmarks(
                            image=annotated_image,
                            landmark_list=face_landmarks,
                            connections=self.mp_mesh_detection.FACE_LANDMARKS_TESSELATION,
                            landmark_drawing_spec=None,
                            connection_drawing_spec=self.mp_drawing_styles
                            .get_default_face_mesh_tesselation_style())
                    if self.FACE_MESH_SHOW_FACE_CONTOUR:
                        self.mp_drawing.draw_landmarks(
                            image=annotated_image,
                            landmark_list=face_landmarks,
                            connections=self.mp_mesh_detection.FACE_LANDMARKS_CONTOURS,
                            landmark_drawing_spec=None,
                            connection_drawing_spec=self.mp_drawing_styles
                            .get_default_face_mesh_contours_style())
                    if self.FACE_MESH_SHOW_FACE_PUPILS:
                        self.mp_drawing.draw_landmarks(
                            image=annotated_image,
                            landmark_list=face_landmarks,
                            connections=(self.mp_mesh_detection.FACE_LANDMARKS_LEFT_IRIS + self.mp_mesh_detection.FACE_LANDMARKS_RIGHT_IRIS),
                            landmark_drawing_spec=None,
                            connection_drawing_spec=self.mp_drawing_styles
                            .get_default_face_mesh_iris_connections_style())

                qs.IMAGE_FACE_MESH.append(annotated_image)
        else:
            self._face_mesh_detected = False

        seconds_fm_loop = time.time() - time_fm_loop_start
        fm_timer = 1.0 / float(self._FM_LOOP_RATE) - seconds_fm_loop
        if fm_timer < 0.0:
            self.LOGGING_MODULE.CAMERA_OK = False
        else:
            self.LOGGING_MODULE.CAMERA_OK = True
        self._schedule_loop("face_mesh_loop_thread", fm_timer, self.face_mesh_loop)

    def pose_loop(self):
        if self._stop_event.is_set():
            return
        time_pose_loop_start = time.time()
        if len(qs.IMAGE_FACE_RAW) == 0:
            self._schedule_loop("pose_loop_thread", 1.0 / self._POSE_LOOP_RATE, self.pose_loop)
            return
        img = qs.IMAGE_FACE_RAW[len(qs.IMAGE_FACE_RAW) - 1]
        self.POSE_MODULE.predict(img)
        qs.DOMINANCE_POSE.append(self.POSE_MODULE.dominance)
        qs.FACINGCAM_POSE.append(self.POSE_MODULE.facing_cam)
        qs.IMAGE_BODY_SKEL.append(self.POSE_MODULE.image)
        if self.POSE_MODULE.tracking:
            qs.IMAGE_BODY_SKEL_BLACK.append(self.POSE_MODULE.skeleton_image)

        seconds_pose_loop = time.time() - time_pose_loop_start
        pose_timer = 1.0 / float(self._POSE_LOOP_RATE) - seconds_pose_loop
        if pose_timer < 0.0:
            self.LOGGING_MODULE.BODY_OK = False
        else:
            self.LOGGING_MODULE.BODY_OK = True

        self.LOGGING_MODULE.TRACKING_BODY = self.LOGGING_MODULE.CAMERA_OK and self.LOGGING_MODULE.BODY_OK and self.POSE_MODULE.tracking

        self._schedule_loop("pose_loop_thread", pose_timer, self.pose_loop)

    def fusion_loop(self):
        if self._stop_event.is_set():
            return
        time_fusion_loop_start = time.time()

        fusion_result = self.FUSION_MODULE.update_fusion()
        qs.FUSION.append(fusion_result)

        seconds_fusion_loop = time.time() - time_fusion_loop_start
        fusion_timer = 1.0 / float(self._FUSION_LOOP_RATE) - seconds_fusion_loop
        self._schedule_loop("fusion_loop_thread", fusion_timer, self.fusion_loop)

    def print_loop(self):
        if self._stop_event.is_set():
            return
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
        img_raw = None
        if self.CAMERA_LOOP:
            if len(qs.IMAGE_FACE_RAW) >= 1:
                img_raw = qs.IMAGE_FACE_RAW[len(qs.IMAGE_FACE_RAW) - 1]
        img_preprocessed = None
        if self.CAMERA_LOOP:
            if len(qs.IMAGE_FACE_PREPROCESSED) >= 1:
                img_preprocessed = qs.IMAGE_FACE_PREPROCESSED[len(qs.IMAGE_FACE_PREPROCESSED) - 1]
        img_facemesh = None
        if self.FACE_MESH_LOOP:
            if len(qs.IMAGE_FACE_MESH) >= 1:
                img_facemesh = qs.IMAGE_FACE_MESH[len(qs.IMAGE_FACE_MESH) - 1]
        img_bodyskel = None
        if self.POSE_LOOP:
            if len(qs.IMAGE_BODY_SKEL) >= 1:
                img_bodyskel = qs.IMAGE_BODY_SKEL[len(qs.IMAGE_BODY_SKEL) - 1]

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

        self.LOGGING_MODULE.update_analysis(analysis_values, img_raw, img_preprocessed, img_facemesh, img_bodyskel)
        self._schedule_loop("print_loop_thread", 0.05, self.print_loop)

    def send_loop(self):
        if self._stop_event.is_set():
            return
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
        v_act = qs.VOICE_ACTIVITY[len(qs.VOICE_ACTIVITY) - 1]
        f_act = qs.FACE_ACTIVITY[len(qs.FACE_ACTIVITY) - 1]
        if self.FACE_MESH_LOOP:
            f_act = float(bool(f_act) and self._face_mesh_detected)
        f_facing = qs.FACINGCAM_POSE[len(qs.FACINGCAM_POSE) - 1]

        face_mesh = ""
        i = 0
        if not self.FACE_MESH_LOOP or isinstance(face_mesh_raw, str):
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
        V_ACT = E.v_act
        F_ACT = E.f_act
        F_FACING = E.f_facing

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
                S_NEG(str(s_neg), name='Sentiment negative'),
                V_ACT(str(v_act), name='Voice Activity'),
                F_ACT(str(f_act), name="Face Activity"),
                F_FACING(str(f_facing), name="Facing Cam")
            )
        )
        command = lxml.etree.tostring(the_doc)
        if self.SEND_UDP_LOOP:
            print("UDP send")
            self._SOCKET.sendto(command, (self._UDP_IP, self._UDP_PORT))
        if self.SEND_KAFKA_LOOP:
            print("Kafka send")
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
        self._schedule_loop("send_loop_thread", send_timer, self.send_loop)

    def start(self, window):
        with self._worker_lock:
            if self._stop_event.is_set() or self._started:
                raise RuntimeError("Create a new pipeline instance before starting again.")
            self._started = True
        if self.VAD_LOOP or self.SER_LOOP or self.STT_LOOP:
            self.microphone_loop()
        if self.CAMERA_LOOP or self.FACE_ER_LOOP or self.FACE_MESH_LOOP or self.POSE_LOOP:
            self._schedule_loop("face_record_loop_thread", 0.0, self.face_record_loop)
            if self._stop_event.wait(1.0):
                return
            self._schedule_loop("face_crop_loop_thread", 0.0, self.face_crop_loop)

        if self._stop_event.wait(2.0):
            return

        if self.FACE_ER_LOOP:
            self._schedule_loop("face_er_loop_thread", 0.0, self.face_er_loop)
        if self.POSE_LOOP:
            self._schedule_loop("pose_loop_thread", 0.0, self.pose_loop)
        if self.VAD_LOOP:
            self._schedule_loop("vad_loop_thread", 0.0, self.vad_loop)
        if self.SER_LOOP:
            self._schedule_loop("ser_loop_thread", 0.0, self.ser_loop)
        if self.STT_LOOP:
            self._schedule_loop("stt_loop_thread", 0.0, self.stt_loop)
        if self.SENTIMENT_LOOP:
            self._schedule_loop("sentiment_loop_thread", 0.0, self.sentiment_loop)
        if self.SEND_UDP_LOOP or self.SEND_KAFKA_LOOP:
            self._schedule_loop("send_loop_thread", 0.0, self.send_loop)
        if self.PRINT_LOOP:
            self._schedule_loop("print_loop_thread", 0.0, self.print_loop)
        if self.FACE_MESH_LOOP:
            self._schedule_loop("face_mesh_loop_thread", 0.0, self.face_mesh_loop)

        if self._stop_event.wait(0.5):
            return

        if self.FUSION_LOOP:
            self._schedule_loop("fusion_loop_thread", 0.0, self.fusion_loop)

        if not self._stop_event.is_set():
            window.START = True

    def _close_resource(self, name, methods, errors, **kwargs):
        resource = getattr(self, name, None)
        if resource is None:
            return
        for method in methods:
            try:
                getattr(resource, method)(**kwargs)
            except Exception as error:
                errors.append(f"{name}.{method}: {error}")
            else:
                if method == methods[-1]:
                    setattr(self, name, None)

    def stop(self):
        with self._shutdown_lock:
            # Use the same lock as scheduling so no worker can start after this snapshot.
            with self._worker_lock:
                self._stop_event.set()
                self.stop_thread = True
                workers = tuple(self._workers)
            for worker in workers:
                if isinstance(worker, threading.Timer):
                    worker.cancel()

            deadline = time.monotonic() + 5.0
            for worker in workers:
                if worker is not threading.current_thread():
                    worker.join(max(0.0, deadline - time.monotonic()))
            if any(worker.is_alive() for worker in workers):
                raise RuntimeError("A pipeline worker is still busy. Wait for it to finish and retry stopping.")

            with self._worker_lock:
                self._workers.clear()
                for name in self._LOOP_THREADS:
                    setattr(self, name, None)

            # Close each resource independently, even if another cleanup fails.
            errors = []
            self._close_resource("capture", ("release",), errors)
            self._close_resource("stream", ("stop_stream", "close"), errors)
            self._close_resource("audio", ("terminate",), errors)
            self._close_resource("face_detection", ("close",), errors)
            self._close_resource("mp_face_mesh", ("close",), errors)
            self._close_resource("POSE_MODULE", ("close",), errors)
            self._close_resource("_KAFKA_PRODUCER", ("flush", "close"), errors, timeout=5.0)
            self._close_resource("_SOCKET", ("close",), errors)
            self._face_mesh_detected = False
            self.LOGGING_MODULE.TRACKING_FACE = False
            self.LOGGING_MODULE.TRACKING_BODY = False
            self.LOGGING_MODULE.TRACKING_VOICE = False
            if errors:
                raise RuntimeError("Pipeline cleanup failed: " + "; ".join(errors))


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
