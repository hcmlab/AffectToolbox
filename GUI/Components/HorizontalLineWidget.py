from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QWidget

class HorLineWidget(QWidget):
    """Class to create a Widget that displays a horizontal line"""
    def __init__(self, parent=None):
        """Constructor for the HorLineWidget class.
        
        Args:
            parent: The parent widget
        """
        super(HorLineWidget, self).__init__(parent)
        self.setMinimumHeight(3)  
        self.color = QColor("#EFEEEE")

    def paintEvent(self, event):
        """Function to paint the widget"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen(self.color, 6) 
        painter.setPen(pen)
        painter.drawLine(self.rect().topLeft(), self.rect().topRight())  

    def toggleColor(self):
        """Function to change the color of the line"""
        if self.color == QColor("#EFEEEE"):
            self.color = QColor("green")
        elif self.color == QColor("green"):
            self.color = QColor("#EFEEEE")
        self.update()