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


def Rightconnect(window):
    window.rounded3_3.rightClicked.connect(lambda event: test(window, event))
    window.rounded3_2.rightClicked.connect(lambda event: test2(window, event))