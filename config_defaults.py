"""Shared defaults for the GUI and AffectPipeline.

Loop rates are in Hz, window lengths in seconds, and fusion speeds in ms.
"""

DEFAULT_PARAMETERS = {
    # Camera and audio devices
    "camera_id": 0,
    "microphone_id": 0,
    "SAMPLE_RATE": 16000,
    "MIC_CHUNKS": 16000,

    # Voice activity
    "VAD_LOOP_RATE": 4.0,
    "VAD_THRESHOLD": 0.25,

    # Speech emotion recognition and voice fusion
    "SER_LOOP_RATE": 1.0,
    "SER_VALENCE_OFFSET": 0.0,
    "SER_AROUSAL_OFFSET": 0.0,
    "SER_DOMINANCE_OFFSET": 0.0,
    "FUSION_VOICE_SPEED": 5000,
    "FUSION_VOICE_VALENCE_WEIGHT": 1.0,
    "FUSION_VOICE_VALENCE_BOOST": 1.0,
    "FUSION_VOICE_AROUSAL_WEIGHT": 1.0,
    "FUSION_VOICE_AROUSAL_BOOST": 1.0,
    "FUSION_VOICE_DOMINANCE_WEIGHT": 1.0,
    "FUSION_VOICE_DOMINANCE_BOOST": 1.0,

    # Transcription and sentiment
    "STT_LOOP_RATE": 0.2,
    "STT_WINDOW_SIZE": 5.0,
    "stt_model_size": "base",
    "SENTIMENT_LOOP_RATE": 1.0,
    "sentiment_model": "multilingual",
    "FUSION_SENTIMENT_SPEED": 5000,
    "FUSION_SENTIMENT_WEIGHT": 1.0,
    "FUSION_SENTIMENT_BOOST": 1.0,

    # Camera capture and face processing
    "CAMERA_LOOP_RATE": 15.0,
    "FACE_PADDING": 0.2,
    "FACE_MESH_RATE": 4.0,
    "ER_LOOP_RATE": 2.0,
    "show_face_mesh": False,
    "face_mesh_show_face_edges": True,
    "face_mesh_show_face_pupils": False,
    "face_mesh_show_face_contour": False,
    "FUSION_FACE_SPEED": 5000,
    "FUSION_FACE_VALENCE_WEIGHT": 1.0,
    "FUSION_FACE_VALENCE_BOOST": 1.25,
    "FUSION_FACE_AROUSAL_WEIGHT": 0.5,
    "FUSION_FACE_AROUSAL_BOOST": 1.75,
    "FUSION_FACE_DOMINANCE_WEIGHT": 1.0,
    "FUSION_FACE_DOMINANCE_BOOST": 1.25,

    # Pose recognition and pose fusion
    "POSE_LOOP_RATE": 5.0,
    "FUSION_POSE_SPEED": 5000,
    "FUSION_POSE_DOMINANCE_WEIGHT": 1.0,
    "FUSION_POSE_DOMINANCE_BOOST": 1.0,

    # Fusion
    "FUSION_LOOP_RATE": 10.0,
    "FUSION_SPEED": 1000,
    "fusion_use_para_v": False,
    "fusion_use_para_a": False,
    "fusion_use_para_d": False,
    "fusion_use_sentiment_v": False,
    "fusion_use_face_v": False,
    "fusion_use_face_a": False,
    "fusion_use_face_d": False,
    "fusion_use_pose_d": False,

    # Network output
    "KAFKA_IP": "127.0.0.1",
    "KAFKA_PORT": 9092,
    "KAFKA_TOPIC": "mithos",
    "UDP_IP": "127.0.0.1",
    "UDP_PORT": 5006,
    "SEND_LOOP_RATE": 2.0,

    # Enabled modules and logging
    "enable_log_to_console": True,
    "enable_print_loop": True,
    "enable_face_mesh_loop": False,
    "enable_transcript": False,
    "enable_voiceactivity": False,
    "enable_paralinguistic": False,
    "enable_sentiment": False,
    "enable_camera": False,
    "enable_facialexpression": False,
    "enable_skeleton": False,
    "enable_fusion": False,
    "enable_udp": False,
    "enable_kafka": False,
    "logging_loop_rate": 10.0,

    # Additional GUI button states
    "enable_micro": False,
    "enable_audio": False,
    "enable_video": False,
    "enable_facetracking": False,
    "enable_bodytracking": False,
    "enable_pose": False,
}
