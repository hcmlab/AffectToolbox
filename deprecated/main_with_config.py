from modules.AffectPipeline import AffectPipeline
from deprecated.ConfigManager import config

class DeviceManager():
    def __init__(self):
        pass

    def get_available_microphones(self):
        import pyaudio

        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')

        for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print(i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

    def choose_microphone(self):
        print("The following microphones are available:")
        self.get_available_microphones()
        print("Choose one option.")
        a = input('').split(" ")[0]
        return int(a)

    def get_available_cameras(self):
        from pygrabber.dshow_graph import FilterGraph

        devices = FilterGraph().get_input_devices()

        available_cameras = {}

        for device_index, device_name in enumerate(devices):
            available_cameras[device_index] = device_name
            print(str(device_index) + " - " + device_name)

    def choose_camera(self):
        print("The following cameras are available:")
        self.get_available_cameras()
        print("Choose one option.")
        a = input('').split(" ")[0]
        return int(a)

conf = config("examples/mithos.conf")

dm = DeviceManager()
mic_id = dm.choose_microphone()
cam_id = dm.choose_camera()

conf["microphone_id"] = mic_id
conf["camera_id"] = cam_id

pipe = AffectPipeline(**conf)
pipe.start()
