import os, json

def initVariables(window=None):
    """Initialize the variables of the main window."""
    if window is not None:
        # Load the configuration file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, '../config.json')
        with open(config_path, 'r') as file:
            data = json.load(file)
            file.close()
        
        window.CAMERA = False 
        window.HEADSET = False
        window.CAMERA_LOOP = False
        window.MIC_LOOP = False
        window.TRANSCRIPT_LOOP = False
        window.VOICE_ACTIVITY_LOOP = False
        window.PARA_LOOP = False
        window.SENTIMENT_LOOP = False
        window.FACE_TRACKING_LOOP = False
        window.FACIAL_EXPRESSION_LOOP = False
        window.SKELETON_LOOP = False
        window.BODY_TRACKING_LOOP = False
        window.POSE_LOOP = False
        window.FUSION_LOOP = False
        window.PLEASURE = False
        window.AROUSAL = False
        window.DOMINANCE = False

        #UniModal Results
        window.PARA_PLEASURE = False
        window.PARA_AROUSAL = False
        window.PARA_DOMINANCE = False

        window.SENT_PLEASURE = False

        window.FACIAL_PLEASURE = False
        window.FACIAL_AROUSAL = False
        window.FACIAL_DOMINANCE = False

        window.POSE_DOMINANCE = False

        #Kafka / UDP Variables
        window.KAFKA = False
        window.KAFKA_IP = data["kafka"]["IP"] #'127.0.0.1'
        window.KAFKA_PORT = data["kafka"]["PORT"] #9092
        window.KAFKA_TOPIC = data["kafka"]["TOPIC"] #'mithos'

        window.UDP = False
        window.UDP_IP = data["udp"]["IP"] #'127.0.0.1'
        window.UDP_PORT = data["udp"]["PORT"] #5006

        # Menu Variables
        window.TRANSCRIPTMENU = False

        #Loop Rates
        window.SER_LOOP_RATE = data["loop_rates"]["SER_LOOP_RATE"] #1.0 #Speech Emotion Recognition
        window.STT_LOOP_RATE = data["loop_rates"]["STT_LOOP_RATE"] #0.2 #Speech to Text
        window.SENTIMENT_LOOP_RATE = data["loop_rates"]["SENTIMENT_LOOP_RATE"] #1.0    #Sentiment
        window.VAD_LOOP_RATE = data["loop_rates"]["VAD_LOOP_RATE"] #4.0  #Voice Actitivity Detection
        window.ER_LOOP_RATE = data["loop_rates"]["ER_LOOP_RATE"] #2.0 #Emotion Recognition (Facial)
        window.POSE_LOOP_RATE = data["loop_rates"]["POSE_LOOP_RATE"] #4.0 #Pose
        window.SEND_LOOP_RATE = data["loop_rates"]["SEND_LOOP_RATE"]#2.0 #Kafka + UDP
        window.CAMERA_LOOP_RATE = data["loop_rates"]["CAMERA_LOOP_RATE"] #4.0  #Camera
        window.FACE_MESH_RATE = data["loop_rates"]["FACE_MESH_RATE"] #4.0 #Face Tracking
        window.SAMPLE_RATE = data["loop_rates"]["SAMPLE_RATE"] #16000  #Audio Sample Rate
        
        window.CAM_ID = data["cam_id"] 
        window.MIC_ID = data["mic_id"]
        
        window.image = None
        window.transcript = None
        window.skeleton = None

def changeValues(kafkaIP=None, kafkaPort=None, kafkaTopic=None, udpIP=None, udpPort=None, ser_loop_rate=None, stt_loop_rate=None, sentiment_loop_rate=None, vad_loop_rate=None, er_loop_rate=None, pose_loop_rate=None, send_loop_rate=None, camera_loop_rate=None, face_mesh_rate=None, sample_rate=None, cam_id=None, mic_id=None):
    """Change the values of the config file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, '../config.json')
    with open(config_path, 'r+') as file:
        data = json.load(file)
        if kafkaIP is not None:
            data["kafka"]["IP"] = kafkaIP
        if kafkaPort is not None:
            data["kafka"]["PORT"] = kafkaPort
        if kafkaTopic is not None:
            data["kafka"]["TOPIC"] = kafkaTopic
        if udpIP is not None:
            data["udp"]["IP"] = udpIP
        if udpPort is not None:
            data["udp"]["PORT"] = udpPort
        if ser_loop_rate is not None:
            data["loop_rates"]["SER_LOOP_RATE"] = ser_loop_rate
        if stt_loop_rate is not None:
            data["loop_rates"]["STT_LOOP_RATE"] = stt_loop_rate
        if sentiment_loop_rate is not None:
            data["loop_rates"]["SENTIMENT_LOOP_RATE"] = sentiment_loop_rate
        if vad_loop_rate is not None:
            data["loop_rates"]["VAD_LOOP_RATE"] = vad_loop_rate
        if er_loop_rate is not None:
            data["loop_rates"]["ER_LOOP_RATE"] = er_loop_rate
        if pose_loop_rate is not None:
            data["loop_rates"]["POSE_LOOP_RATE"] = pose_loop_rate
        if send_loop_rate is not None:
            data["loop_rates"]["SEND_LOOP_RATE"] = send_loop_rate
        if camera_loop_rate is not None:
            data["loop_rates"]["CAMERA_LOOP_RATE"] = camera_loop_rate
        if face_mesh_rate is not None:
            data["loop_rates"]["FACE_MESH_RATE"] = face_mesh_rate
        if sample_rate is not None:
            data["loop_rates"]["SAMPLE_RATE"] = sample_rate
        if cam_id is not None:
            data["cam_id"] = cam_id
        if mic_id is not None:
            data["mic_id"] = mic_id
        file.seek(0)
        json.dump(data, file)
        file.truncate()
        file.close()
