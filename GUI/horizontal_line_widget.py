from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QWidget

class HorLineWidget(QWidget):
    def __init__(self, parent=None):
        super(HorLineWidget, self).__init__(parent)
        self.setMinimumHeight(3)  # Set a minimum height for the widget
        self.color = QColor("black")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        pen = QPen(self.color, 6)  # Create a pen with a width of 3
        painter.setPen(pen)
        painter.drawLine(self.rect().topLeft(), self.rect().topRight())  # Draw a horizontal line

    # def mousePressEvent(self, event) -> None:
    #     self.toggleColor()
    #     self.update()

    def toggleColor(self):
        if self.color == QColor("black"):
            self.color = QColor("green")
        elif self.color == QColor("green"):
            self.color = QColor("black")
        self.update()