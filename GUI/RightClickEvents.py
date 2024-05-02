"""This file contains the right click events for the GUI. It is used to initialize the right click window for each widget."""
from GUI.Components.RightClickWindow import RightClickWindow

def InitSettingWindow(window, name=""):
    """Initialize the right click window for the settings of the widgets"""
    window.rightClickWindow = RightClickWindow(window=window, name=name)
    window.rightClickWindow.setWindowTitle(f"{name} Settings")
    window.rightClickWindow.show()

def Rightconnect(window):
    """Connect the right click events to the widgets in the GUI"""
    window.circle2_1.rightClicked.connect(lambda: InitSettingWindow(window=window, name="Microphone"))
    window.circle2_2.rightClicked.connect(lambda: InitSettingWindow(window=window, name="Camera"))
    window.rounded3_1.rightClicked.connect(lambda: InitSettingWindow(window=window, name="Audio"))
    window.rounded3_2.rightClicked.connect(lambda: InitSettingWindow(window=window, name="Transcript"))
    window.rounded3_3.rightClicked.connect(lambda: InitSettingWindow(window=window, name="Video"))
    window.rounded3_4.rightClicked.connect(lambda: InitSettingWindow(window=window, name="Skeleton"))
    window.rounded4_1.rightClicked.connect(lambda: InitSettingWindow(window=window, name="VoiceActivity"))
    window.rounded4_2.rightClicked.connect(lambda: InitSettingWindow(window=window, name="FaceTracking"))
    window.rounded4_3.rightClicked.connect(lambda: InitSettingWindow(window=window, name="BodyTracking"))
    window.circle5_1_inner.rightClicked.connect(lambda: InitSettingWindow(window=window, name="Para"))
    window.circle5_2_inner.rightClicked.connect(lambda: InitSettingWindow(window=window, name="Sentiment"))
    window.circle5_3_inner.rightClicked.connect(lambda: InitSettingWindow(window=window, name="FacialExpression"))
    window.circle5_4_inner.rightClicked.connect(lambda: InitSettingWindow(window=window, name="Pose"))
    window.rounded7.rightClicked.connect(lambda: InitSettingWindow(window=window, name="Fusion"))
    window.kafka_button.rightClicked.connect(lambda :InitSettingWindow(window=window, name="Kafka"))
    window.udp_button.rightClicked.connect(lambda :InitSettingWindow(window=window, name="UDP"))
    window.play_button.rightClicked.connect(lambda :InitSettingWindow(window=window, name="Start"))