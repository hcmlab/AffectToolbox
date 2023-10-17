from modules.AffectPipeline import AffectPipeline, DeviceManager
from modules.ConfigManager import config

conf = config("examples/mithos.conf")

dm = DeviceManager()
mic_id = dm.choose_microphone()
cam_id = dm.choose_camera()

conf["microphone_id"] = mic_id
conf["camera_id"] = cam_id

pipe = AffectPipeline(**conf)
pipe.start()
