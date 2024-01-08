from modules.AffectPipeline import AffectPipeline, DeviceManager
from GUI.main import MainWindow
from PyQt6.QtWidgets import QApplication

app = QApplication([])
window = MainWindow()
# dm = DeviceManager()
window.mic_id = 2 #dm.choose_microphone()
window.cam_id = 0 #dm.choose_camera()
window.show()
app.exec()