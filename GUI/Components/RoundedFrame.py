from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import QEvent

class RoundedFrame(QFrame):
    """Clickable rounded frame widget with a label in the center"""
    clicked = pyqtSignal()
    rightClicked = pyqtSignal(QEvent)
    def __init__(self, text="", color="#0071c1", text_color="#c9ffff", font_size=20, border=False):
        """Constructor of the rounded frame widget.
        
        Args:
            text (str): The text of the label in the center of the frame
            color (str): The background color of the frame
            text_color (str): The color of the text
            font_size (int): The size of the font
            border (bool): Whether the frame should have a border
        """
        super(RoundedFrame, self).__init__()
        self.layout = QVBoxLayout(self)
        self.label = QLabel(text, self)
        self.label.setStyleSheet(f"QLabel {{ color: {text_color}; font-size: {font_size}px; }}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text horizontally and vertically

        self.border_css = "border: 1px solid black;" if border else ""
        self.setStyleSheet(f"QFrame {{background-color: {color}; border-radius: 10px; {self.border_css}}}")
        self.basecolor = color
        self.color = color

    def resizeEvent(self, event):
        """Resize the label when the frame is resized"""
        super().resizeEvent(event)
        self.label.resize(self.size())

    def mousePressEvent(self, event) -> None:
        """Emit the clicked or rightClicked signal when the frame is clicked."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        elif event.button() == Qt.MouseButton.RightButton:
            self.rightClicked.emit(event)
        super().mousePressEvent(event)
        
    def toggleColor(self):
        """Toggle the color of the frame between the base color and green."""
        if self.color == self.basecolor:
            self.setStyleSheet(f"QFrame {{background-color: green; border-radius: 10px; {self.border_css}}}")
            self.color = "green"
        elif self.color == "green":
            self.setStyleSheet(f"QFrame {{background-color: {self.basecolor}; border-radius: 10px; {self.border_css}}}")
            self.color = self.basecolor