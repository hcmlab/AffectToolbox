from GUI.RightClickWindow import RightClickWindow

def InitSettingVideo(window, name=""):
    window.rightClickWindow = RightClickWindow(window=window, name=name)
    window.rightClickWindow.setWindowTitle(f"{name} Settings")
    window.rightClickWindow.show()


def Rightconnect(window):
    window.rounded3_1.rightClicked.connect(lambda: InitSettingVideo(window=window, name="Audio"))
    window.rounded3_2.rightClicked.connect(lambda: InitSettingVideo(window=window, name="Transcript"))
    window.rounded3_3.rightClicked.connect(lambda: InitSettingVideo(window=window, name="Camera"))
    window.rounded3_4.rightClicked.connect(lambda: InitSettingVideo(window=window, name="Skeleton"))
    window.rounded4_1.rightClicked.connect(lambda: InitSettingVideo(window=window, name="VoiceActivity"))
    window.rounded4_2.rightClicked.connect(lambda: InitSettingVideo(window=window, name="FaceTracking"))
    window.rounded4_3.rightClicked.connect(lambda: InitSettingVideo(window=window, name="BodyTracking"))
    window.circle5_1_inner.rightClicked.connect(lambda: InitSettingVideo(window=window, name="Para"))
    window.circle5_2_inner.rightClicked.connect(lambda: InitSettingVideo(window=window, name="Sentiment"))
    window.circle5_3_inner.rightClicked.connect(lambda: InitSettingVideo(window=window, name="FacialExpression"))
    window.circle5_4_inner.rightClicked.connect(lambda: InitSettingVideo(window=window, name="Pose"))
    window.rounded7.rightClicked.connect(lambda: InitSettingVideo(window=window, name="Fusion"))
    window.kafka_button.rightClicked.connect(lambda :InitSettingVideo(window=window, name="Kafka"))
    window.udp_button.rightClicked.connect(lambda :InitSettingVideo(window=window, name="UDP"))
    window.play_button.rightClicked.connect(lambda :InitSettingVideo(window=window, name="Start"))