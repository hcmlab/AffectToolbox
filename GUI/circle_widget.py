from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import pyqtSignal

class CircleWidget(QWidget):
    clicked = pyqtSignal()

    def __init__(self, color="#f2f2f2", label=None, font_size=10, image_path=None, parent=None):
        super(CircleWidget, self).__init__(parent)
        self.color = QColor(color)
        self.baseColor = self.color
        self.setMinimumSize(100, 100)  # Set a minimum size for the widget

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

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(self.color)
        painter.drawEllipse(0, 0, self.width(), self.height())

    def mousePressEvent(self, event) -> None:
        self.clicked.emit()
    
    def toggleColor(self):
        if self.color == self.baseColor:
            self.color = QColor("green")
        elif self.color == QColor("green"):
            self.color = self.baseColor
        self.update()

    # def resizeEvent(self, event):
    #     self.radius = min(self.width(), self.height()) // 2  # Update the radius
        