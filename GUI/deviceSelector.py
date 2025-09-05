import pyaudio
from PySide6.QtWidgets import QComboBox, QVBoxLayout, QWidget, QLabel
import platform
from pygrabber.dshow_graph import FilterGraph

class DeviceSelector(QWidget):
    """
    Class to select the microphone and camera devices to use
    in the application
    """

    def __init__(self, parent=None, parameters=None, name=""):
        super().__init__(parent)
        self.parameters = parameters
        self.layout = QVBoxLayout(self)

        # Initialize either microphone or camera selector based on the name
        if name == "Micro":
            self.layout.addWidget(QLabel("Select Microphone:"))
            self.microphone_selector = QComboBox(self)
            self.layout.addWidget(self.microphone_selector)
            self.update_audio_devices()
            self.microphone_selector.currentIndexChanged.connect(self.exp_selected_microphone)

        elif name == "Camera":
            self.layout.addWidget(QLabel("Select Camera:"))
            self.camera_selector = QComboBox(self)
            self.layout.addWidget(self.camera_selector)
            self.update_camera_devices()
            self.camera_selector.currentIndexChanged.connect(self.exp_selected_camera)

    # def update_audio_devices(self):
    #     # Detects and lists all available microphone input devices using PyAudio
    #     p = pyaudio.PyAudio()
    #     for i in range(p.get_device_count()):
    #         device_info = p.get_device_info_by_index(i)
    #         if device_info.get('maxInputChannels') > 0:
    #             device_name = f"{i} - {device_info.get('name')}"
    #             self.microphone_selector.addItem(device_name)
    #
    # def update_camera_devices(self):
    #     # Detects and lists all available camera devices.
    #     system = platform.system()
    #     graph = FilterGraph()
    #     devices = graph.get_input_devices()
    #     if system == "Windows":
    #         for device_index, device_name in enumerate(devices):
    #             self.camera_selector.addItem(f"{device_index} - {device_name}")
    #     elif system == "Darwin":  # macOS
    #         self.camera_selector.addItem("0 - MacBook Inbuilt Camera (Dummy)") #Dummy
    #     else:
    #         self.camera_selector.addItem("0 - Default Camera")
    #
    # def exp_selected_camera(self):
    #     # Called when a new camera is selected.
    #     # Stores the selected camera index in the parameter dictionary
    #
    #     cam_id = int(self.camera_selector.currentText().split()[0])
    #     if self.parameters is not None:
    #         self.parameters["camera_id"] = cam_id
    #     return cam_id
    #
    # def exp_selected_microphone(self):
    #     #Called when a new microphone is selected.
    #     #Stores the selected microphone index in the parameter dictionary.
    #
    #     mic_id = int(self.microphone_selector.currentText().split()[0])
    #     if self.parameters is not None:
    #         self.parameters["microphone_id"] = mic_id
    #     return mic_id

    def update_audio_devices(self):
        """Function to update the microphone and camera devices in the combo boxes"""
        # Update microphone devices
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                self.microphone_selector.addItem(
                    str(i) + " - " + p.get_device_info_by_host_api_device_index(0, i).get('name'))

    def update_camera_devices(self):
        # Update camera devices
        devices = FilterGraph().get_input_devices()

        available_cameras = {}

        for device_index, device_name in enumerate(devices):
            available_cameras[device_index] = device_name
            self.camera_selector.addItem(str(device_index) + " - " + device_name)

    def exp_selected_camera(self):
        """Function to get the selected camera device"""
        return int(self.camera_selector.currentText().split()[0])

    def exp_selected_microphone(self):
        """Function to get the selected microphone device"""
        return int(self.microphone_selector.currentText().split()[0])