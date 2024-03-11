from modules.AffectPipeline import AffectPipeline, DeviceManager
from GUI.main import MainWindow
from PyQt6.QtWidgets import QApplication

app = QApplication([])
window = MainWindow()
# dm = DeviceManager()
# window.mic_id = 2#dm.choose_microphone()
# window.cam_id = 0#dm.choose_camera()
# window.show()
window.showFullScreen()
app.exec()

"""
vad_loop_thread
ser_loop_thread
stt_loop_thread
sentiment_loop_thread
face_record_loop_thread
face_crop_loop_thread
face_er_loop_thread
face_mesh_loop_thread
pose_loop_thread
fusion_loop_thread
print_loop_thread
send_loop_thread
"""