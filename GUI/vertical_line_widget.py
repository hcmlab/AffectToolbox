from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QWidget

class VerLineWidget(QWidget):
    def __init__(self, parent=None):
        super(VerLineWidget, self).__init__(parent)
        self.setMinimumSize(1, 1)  # Set a minimum size for the widget
        # self.color = QColor("grey")
        self.color = QColor("#EFEEEE")

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(self.color, 3)  # Create a pen with width 3
        painter.setPen(pen)  # Set the pen
        painter.drawLine(self.width() // 2, 0, self.width() // 2, self.height())

  
    def toggleColor(self):
        if self.color == QColor("#EFEEEE"):
            self.color = QColor("green")
        elif self.color == QColor("green"):
            self.color = QColor("#EFEEEE")
        self.update()