import pyaudio
from PyQt6.QtWidgets import QComboBox, QVBoxLayout, QWidget
from pygrabber.dshow_graph import FilterGraph
from PyQt6.QtCore import Qt

class DeviceSelector(QWidget):
    """Class to select the microphone and camera devices to use in the application same functionality as the DeviceManager class in AffectPipeline.py"""
    def __init__(self, parent=None, window=None, name=""):
        """Constructor for the DeviceSelector class.
        
        Args:
            parent: The parent widget
            window: The main window
        """
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        self.window = window
        
        if name == "Microphone":
            self.microphone_selector = QComboBox(self)
            layout.addWidget(self.microphone_selector)
            self.update_audio_devices()
            
            # Set the selected item in the combo boxes
            microphone_index = self.microphone_selector.findText(str(window.MIC_ID), Qt.MatchFlag.MatchStartsWith)
            if microphone_index != -1:
                self.microphone_selector.setCurrentIndex(microphone_index)
            self.microphone_selector.currentIndexChanged.connect(self.exp_selected_microphone)
            
        elif name == "Camera":
            self.camera_selector = QComboBox(self)
            layout.addWidget(self.camera_selector)
            self.update_camera_devices()
            
            # Set the selected item in the combo boxes
            camera_index = self.camera_selector.findText(str(window.CAM_ID), Qt.MatchFlag.MatchStartsWith)
            if camera_index != -1:
                self.camera_selector.setCurrentIndex(camera_index)
            self.camera_selector.currentIndexChanged.connect(self.exp_selected_camera)
                
    
    def update_audio_devices(self):
        """Function to update the microphone and camera devices in the combo boxes"""
        # Update microphone devices
        self.microphone_selector.addItem("Local File")

        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                self.microphone_selector.addItem(str(i) + " - " + p.get_device_info_by_host_api_device_index(0, i).get('name'))

    def update_camera_devices(self):
        # Update camera devices
        devices = FilterGraph().get_input_devices()

        available_cameras = {}
        self.camera_selector.addItem("Local File")

        for device_index, device_name in enumerate(devices):
            available_cameras[device_index] = device_name
            self.camera_selector.addItem(str(device_index) + " - " + device_name)
    
    def exp_selected_camera(self):
        """Function to get the selected camera device"""
        if self.camera_selector.currentText() == "Local File":
            return -1
        return int(self.camera_selector.currentText().split()[0])
        
    def exp_selected_microphone(self):
        """Function to get the selected microphone device"""
        if self.microphone_selector.currentText() == "Local File":
            return -1
        return int(self.microphone_selector.currentText().split()[0])