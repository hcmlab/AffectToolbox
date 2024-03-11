from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import QEvent
from PyQt6.QtCore import QTimer

class CircleWidget(QWidget):
    clicked = pyqtSignal()
    rightClicked = pyqtSignal(QEvent)

    def __init__(self, color="#f2f2f2", label=None, font_size=10, image_path=None, parent=None):
        super(CircleWidget, self).__init__(parent)
        self.window = None
        self.name = ""
        self.color = QColor(color)
        self.baseColor = self.color
        self.setMinimumSize(100, 100)  # Set a minimum size for the widget
        self.setStyleSheet("background-color: transparent;")  # Set the background color to transparent
        self.layout = QVBoxLayout(self)
        self.label = QLabel(label, self)
        self.label.setFont(QFont('Arial', font_size))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.layout.addWidget(self.label)

        if image_path:
            self.image_label = QLabel(self)
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)  # Change the size of the image
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the image
            self.layout.addWidget(self.image_label)
        
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.trafficLight()) 
        self.timer.start(1000)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(self.color)
        painter.drawEllipse(0, 0, self.width(), self.height())

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        elif event.button() == Qt.MouseButton.RightButton:
            self.rightClicked.emit(event)
        super().mousePressEvent(event)
    
    def toggleColor(self):
        if self.color == self.baseColor:
            self.color = QColor("green")
        elif self.color == QColor("green"):
            self.color = self.baseColor
        self.update()
        
    def trafficLight(self):
        if self.window is not None:
            self.color = QColor("green")
            if self.name == "Voice_Activity":
                if not self.window.pipe.LOGGING_MODULE.TRACKING_VOICE:
                    self.color = QColor("yellow")
                if not self.window.pipe.LOGGING_MODULE.VOICE_OK:
                    self.color = QColor("red")
            elif self.name == "Face_Tracking":
                if not self.window.pipe.LOGGING_MODULE.TRACKING_FACE:
                    self.color = QColor("yellow")
                if not self.window.pipe.LOGGING_MODULE.CAMERA_OK:
                    self.color = QColor("red")
            elif self.name == "Body_Tracking":
                if not self.window.pipe.LOGGING_MODULE.TRACKING_BODY:
                    self.color = QColor("yellow")
                if not self.window.pipe.LOGGING_MODULE.BODY_OK:
                    self.color = QColor("red")
            self.update()
                

        