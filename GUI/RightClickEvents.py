from GUI.RightClickWindow import RightClickWindow
from GUI.RightClickWidget import RightClickWidget


def test(window, event):
    window.rightClickWindow = RightClickWindow(window=window)
    global_position = event.globalPosition().toPoint()
    global_position.setX(int(event.globalPosition().x()))  # X-Position from the event
    global_position.setY(int(window.rounded3_3.y() + 0.5*window.rounded3_2.height()))
    window.rightClickWindow.move(global_position)
    window.rightClickWindow.setWindowTitle("Video Settings")
    window.rightClickWindow.show()

def test2(window, event):
    def turnOn():
        global_position = event.globalPosition().toPoint()
        global_position.setX(int(event.globalPosition().x()))  # X-Position from the event
        global_position.setY(int(window.rounded3_2.y() + 0.5*window.rounded3_2.height()))
        window.rightClickWidget = RightClickWidget(window=window)
        window.rightClickWidget.setParent(window.bodyContainer)
        window.rightClickWidget.move(global_position)
        window.rightClickWidget.show()

    if window.TRANSCRIPTMENU:
        window.TRANSCRIPTMENU = False
    else:
        window.TRANSCRIPTMENU = True
        turnOn()

def InitSettingVideo(window, name=""):
    window.rightClickWindow = RightClickWindow(window=window, name=name)
    # global_position = event.globalPosition().toPoint()
    # global_position.setX(int(event.globalPosition().x()))  # X-Position from the event
    # global_position.setY(int(window.rounded3_3.y() + 0.5*window.rounded3_2.height()))
    # window.rightClickWindow.move(global_position)
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