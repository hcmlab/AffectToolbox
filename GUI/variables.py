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

        # Menu Variables
        window.TRANSCRIPTMENU = False