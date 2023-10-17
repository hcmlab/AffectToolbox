from modules.AffectPipeline import AffectPipeline, DeviceManager

dm = DeviceManager()



mic_id = dm.choose_microphone()
cam_id = dm.choose_camera()

#exit()

pipe = AffectPipeline(enable_vad_loop=True,
                      enable_ser_loop=True,
                      enable_stt_loop=True,
                      enable_camera_loop=True,
                      enable_print_loop=True,
                      enable_send_udp_loop=False,
                      enable_send_kafka_loop=False,
                      enable_face_er_loop=True,
                      enable_face_mesh_loop=True,
                      enable_pose_loop=True,
                      enable_fusion_loop=True,
                      enable_sentiment_loop=True,
                      show_face_mesh=True,
                      face_mesh_show_face_edges=True,
                      face_mesh_show_face_pupils=False,
                      face_mesh_show_face_contour=False,
                      camera_id=cam_id,
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
                      microphone_id=mic_id,
                      stt_window_length=5,
                      stt_model_size="base",
                      sentiment_model="germansentiment")
pipe.start()
