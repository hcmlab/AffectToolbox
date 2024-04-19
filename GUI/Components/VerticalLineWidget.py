from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QWidget

class VerLineWidget(QWidget):
    """A vertical line widget that can be toggled between two colors"""
    def __init__(self, parent=None):
        super(VerLineWidget, self).__init__(parent)
        self.setMinimumSize(1, 1) 
        self.color = QColor("#EFEEEE")

    def paintEvent(self, event):
        """Draw the line"""
        painter = QPainter(self)
        pen = QPen(self.color, 3)  
        painter.setPen(pen) 
        painter.drawLine(self.width() // 2, 0, self.width() // 2, self.height())

    def toggleColor(self):
        """Toggle the color of the line"""
        if self.color == QColor("#EFEEEE"):
            self.color = QColor("green")
        elif self.color == QColor("green"):
            self.color = QColor("#EFEEEE")
        self.update()