from modules.AffectPipeline import AffectPipeline, DeviceManager
from GUI.Image_window import ImageWindow

def headphonesClick(window):
    window.rounded1_1.toggleColor()
    window.hlineWidgetVoicetoVer.toggleColor()
    window.verlineWidgetVoicetoHeadset.toggleColor()
    window.hlineWidgetVertoHeadset.toggleColor()
    window.circle2_1.toggleColor()

def WebcamClick(window):
    if window.CAMERA_LOOP:
        window.CAMERA_LOOP = False
    else:
        window.CAMERA_LOOP = True
    window.rounded1_2.toggleColor()
    window.rounded1_3.toggleColor()
    window.hlineWidgetFacetoCol.toggleColor()
    window.hlineWidgetBodytoCol.toggleColor()
    window.collineWidgetBodyandFace.toggleColor()
    window.hlineWidgetColtoCam.toggleColor()
    window.circle2_2.toggleColor()

def AudioClick(window):
    headphonesClick(window)
    window.hlineWidgetHeadsettoAudio.toggleColor()
    window.rounded3_1.toggleColor()

def TranscriptClick(window):
    AudioClick(window)
    window.verlineWidgetAudioToTra.toggleColor()
    window.rounded3_2.toggleColor()

def PlayButtonClick(window):
    print("Play Button Clicked")
    
    window.pipe = AffectPipeline(enable_log_to_console=False,
                      enable_vad_loop=False,
                      enable_ser_loop=False,
                      enable_stt_loop=False,
                      enable_camera_loop=window.CAMERA_LOOP,
                      enable_print_loop=False, #
                      enable_send_udp_loop=False,
                      enable_send_kafka_loop=False,
                      enable_face_er_loop= False, #
                      enable_face_mesh_loop=False,
                      enable_pose_loop=False,
                      enable_fusion_loop=False,
                      enable_sentiment_loop=False,
                      show_face_mesh=False,
                      face_mesh_show_face_edges=False,
                      face_mesh_show_face_pupils=False,
                      face_mesh_show_face_contour=False,
                      camera_id=window.cam_id,
                      ser_loop_rate=1.0,
                      stt_loop_rate=0.2,
                      sentiment_loop_rate=1.0,
                      vad_loop_rate=4.0,
                      er_loop_rate=2.0,
                      pose_loop_rate=4.0,
                      send_loop_rate=2.0,
                      camera_loop_rate=4.0,
                      face_mesh_rate=4.0,
                      udp_ip='127.0.0.1',
                      udp_port=5006,
                      kafka_ip='127.0.0.1',
                      kafka_port=9092,
                      web_app_port=5000,
                      kafka_topic_name='mithos',
                      sample_rate=16000,
                      vad_threshold=0.25,
                      face_padding=0.2,
                      microphone_chunks=16000,
                      microphone_id=window.mic_id,
                      stt_window_length=5,
                      stt_model_size="base",
                      sentiment_model="germansentiment")
    window.START = False
    if window.CAMERA_LOOP:
        window.image = ImageWindow(window=window)
        window.image.show()
    window.pipe.start(window)
    

def connect(window):
    window.circle2_1.clicked.connect(lambda: headphonesClick(window)) 
    window.circle2_2.clicked.connect(lambda: WebcamClick(window)) 
    window.rounded3_1.clicked.connect(lambda: AudioClick(window)) 
    window.rounded3_2.clicked.connect(lambda: TranscriptClick(window))
    window.play_button.clicked.connect(lambda: PlayButtonClick(window))

