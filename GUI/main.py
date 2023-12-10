from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from GUI.rounded_frame import RoundedFrame
from GUI.image_rounded_frame import ImageRoundedFrame
from GUI.rounded_frame_noclick import RoundedFrameNoClick
from GUI.Eventfilter import handleEventFilter
from GUI.ui_initializer import initialize_ui
from GUI.ClickEvents import connect
from GUI.variables import initVariables

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.lines_initialized = False
        self.initSizes()
        self.initUI()
        initVariables(self)
        connect(self)
        
    def eventFilter(self, source, event):
        return handleEventFilter(self, source, event)

    def initUI(self):
        initialize_ui(self)
        
    def initSizes(self):
        self.screen_height = QApplication.instance().primaryScreen().geometry().height()
        self.screen_width = QApplication.instance().primaryScreen().geometry().width()
        self.column_width = int((self.screen_width - 45) / 8)
        self.column_height_light = int(self.screen_height * 0.87)
        self.column_height_5 = int(self.screen_height * 0.8)
        self.column_height_2 = int(self.screen_height * 0.5)

    def createTitleContainer(self):
        titles = ["MODALITIES", "SENSORS", "DATA STREAMS", "ACTIVITY CHECK", "ANALYSIS", "UNIMODAL RESULTS", "FUSION", "MULTIMODAL RESULTS"]
        self.frames = [RoundedFrameNoClick(title) for title in titles]
        for frame in self.frames:
            frame.setFixedHeight(int(self.screen_height * 0.05))

        # Create a container for the titles
        self.titleContainer = QWidget()
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setContentsMargins(5, 0, 5, 0)  # Set the margins 
        self.titleLayout.setSpacing(5)  # Set the spacing between widgets to 5

        # Add the titles to the layout
        for frame in self.frames:
            self.titleLayout.addWidget(frame)

        self.titleContainer.setLayout(self.titleLayout)

    def createBodyContainer(self):
        # Create a second container for the RoundedFrame widgets
        self.bodyContainer = QWidget()
        self.secondLayout = QHBoxLayout()
        self.secondLayout.setContentsMargins(5, 0, 5, 5)  # Set the margins 
        self.secondLayout.setSpacing(5)  # Set the spacing between widgets to 5

        # Add the RoundedFrame widgets to the second layout
        for i in range(8):
            if(i == 0):
                frame = ImageRoundedFrame(color="#bdd7ee", image_path="./GUI/Icons/personIcon.svg")
            else: 
                frame = RoundedFrameNoClick(color="#bdd7ee")
            if (i <= 4):
                frame.setFixedHeight(int(self.screen_height*0.4 + self.screen_height * (i) * 0.1))
            else :
                frame.setFixedHeight(int(self.screen_height * 0.87))
            self.secondLayout.addWidget(frame)
            self.secondLayout.setAlignment(frame, Qt.AlignmentFlag.AlignTop)

        self.bodyContainer.setLayout(self.secondLayout)

    def createLayout(self):
        self.widget = QWidget()
        self.layout = QVBoxLayout()  # Change to QVBoxLayout

        self.layout.setContentsMargins(0, 0, 0, 0)  # Set the margins to 0
        self.layout.setSpacing(0)  # Set the spacing between widgets to 10px

        # Add the title container to the main layout
        self.layout.addWidget(self.titleContainer)

        # Add the second container and the circle8_1 to the main layout
        self.layout.addWidget(self.bodyContainer)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    