def initVariables(window=None):
    if window is not None:
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
        window.KAFKA_IP = '127.0.0.1'
        window.KAFKA_PORT = 9092
        window.KAFKA_TOPIC = 'mithos'

        window.UDP = False
        window.UDP_IP = '127.0.0.1'
        window.UDP_PORT = 5006

        # Menu Variables
        window.TRANSCRIPTMENU = False

        #Loop Rates
        window.SER_LOOP_RATE = 1.0
        window.STT_LOOP_RATE = 0.2
        window.SENTIMENT_LOOP_RATE = 1.0    #Sentiment
        window.VAD_LOOP_RATE = 4.0  #Audio
        window.ER_LOOP_RATE = 2.0
        window.POSE_LOOP_RATE = 4.0 #Pose
        window.SEND_LOOP_RATE = 2.0 
        window.CAMERA_LOOP_RATE = 4.0  #Camera
        window.FACE_MESH_RATE = 4.0 #Face Tracking
        window.SAMPLE_RATE = 16000  #Fusion