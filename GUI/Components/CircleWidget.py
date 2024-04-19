from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import QEvent
from PyQt6.QtCore import QTimer

class CircleWidget(QWidget):
    """A clickable widget to display a circle with an optional label in the center."""
    clicked = pyqtSignal()
    rightClicked = pyqtSignal(QEvent)

    def __init__(self, color="#f2f2f2", label=None, font_size=10, image_path=None, parent=None):
        """Initialize the circle widget.
        
        Args:
            color (str, optional): The color of the circle. Defaults to "#f2f2f2".
            label (str, optional): The label to display in the center of the circle. Defaults to None.
            font_size (int, optional): The font size of the label. Defaults to 10.
            image_path (str, optional): The path to an image to display in the center of the circle. Defaults to None.
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super(CircleWidget, self).__init__(parent)
        self.window = None
        self.name = ""
        self.color = QColor(color)
        self.baseColor = self.color
        self.setMinimumSize(100, 100) 
        self.setStyleSheet("background-color: transparent;")  
        self.layout = QVBoxLayout(self)
        self.label = QLabel(label, self)
        self.label.setFont(QFont('Arial', font_size))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.layout.addWidget(self.label)

        #Add an image to the circle widget if a path is provided
        if image_path:
            self.image_label = QLabel(self)
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)  # Change the size of the image
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the image
            self.layout.addWidget(self.image_label)
        
        #Connect a timer to the trafficLight method
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.trafficLight()) 
        self.timer.start(1000)


    def paintEvent(self, event):
        """Paint the circle"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(self.color)
        painter.drawEllipse(0, 0, self.width(), self.height())

    def mousePressEvent(self, event) -> None:
        """Emit a signal when the widget is clicked"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        elif event.button() == Qt.MouseButton.RightButton:
            self.rightClicked.emit(event)
        super().mousePressEvent(event)
    
    def toggleColor(self):
        """Toggle the color of the circle widget"""
        if self.color == self.baseColor:
            self.color = QColor("green")
        elif self.color == QColor("green"):
            self.color = self.baseColor
        self.update()
        
    def trafficLight(self):
        """Change the color of the circle widget based on the logging module status"""
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
                

        