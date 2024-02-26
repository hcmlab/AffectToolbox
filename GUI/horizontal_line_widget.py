from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QWidget

class HorLineWidget(QWidget):
    def __init__(self, parent=None):
        super(HorLineWidget, self).__init__(parent)
        self.setMinimumHeight(3)  # Set a minimum height for the widget
        # self.color = QColor("white")
        self.color = QColor("#EFEEEE")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen(self.color, 6) 
        painter.setPen(pen)
        painter.drawLine(self.rect().topLeft(), self.rect().topRight())  # Draw a horizontal line

    def toggleColor(self):
        if self.color == QColor("#EFEEEE"):
            self.color = QColor("green")
        elif self.color == QColor("green"):
            self.color = QColor("#EFEEEE")
        self.update()