import pyaudio
from PyQt6.QtWidgets import QComboBox, QVBoxLayout, QWidget
from pygrabber.dshow_graph import FilterGraph
from PyQt6.QtCore import Qt

class DeviceSelector(QWidget):
    def __init__(self, parent=None, window=None):
        super().__init__(parent)

        self.microphone_selector = QComboBox(self)
        self.camera_selector = QComboBox(self)
        
        self.window = window

        layout = QVBoxLayout(self)
        layout.addWidget(self.microphone_selector)
        layout.addWidget(self.camera_selector)

        self.update_devices()
        
        # Set the selected item in the combo boxes
        microphone_index = self.microphone_selector.findText(str(window.MIC_ID), Qt.MatchFlag.MatchStartsWith)
        if microphone_index != -1:
            self.microphone_selector.setCurrentIndex(microphone_index)
        camera_index = self.camera_selector.findText(str(window.CAM_ID), Qt.MatchFlag.MatchStartsWith)
        if camera_index != -1:
            self.camera_selector.setCurrentIndex(camera_index)
        
        self.microphone_selector.currentIndexChanged.connect(self.exp_selected_microphone)
        self.camera_selector.currentIndexChanged.connect(self.exp_selected_camera)
    
    def update_devices(self):
        # Update microphone devices
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                self.microphone_selector.addItem(str(i) + " - " + p.get_device_info_by_host_api_device_index(0, i).get('name'))

        # Update camera devices
        devices = FilterGraph().get_input_devices()

        available_cameras = {}

        for device_index, device_name in enumerate(devices):
            available_cameras[device_index] = device_name
            self.camera_selector.addItem(str(device_index) + " - " + device_name)
    
    def exp_selected_camera(self):
        return int(self.camera_selector.currentText().split()[0])
        
    def exp_selected_microphone(self):
        return int(self.microphone_selector.currentText().split()[0])