from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout

class RoundedFrameNoClick(QFrame):
    """Non-clickable rounded frame widget with a label in the center"""
    def __init__(self, text="", color="#0071c1", text_color="#c9ffff", font_size=20, border=False):
        """Constructor of the non-clickable rounded frame widget.
        
        Args:
            text (str): The text of the label in the center of the frame
            color (str): The background color of the frame
            text_color (str): The color of the text
            font_size (int): The size of the font
            border (bool): Whether the frame should have a border
        """
        super(RoundedFrameNoClick, self).__init__()
        self.layout = QVBoxLayout(self)
        self.label = QLabel(text, self)
        self.label.setStyleSheet(f"QLabel {{ color: {text_color}; font-size: {font_size}px; }}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text horizontally and vertically

        border_css = "border: 1px solid black;" if border else ""
        self.setStyleSheet(f"QFrame {{background-color: {color}; border-radius: 10px; {border_css}}}")

    def resizeEvent(self, event):
        """Resize the label when the frame is resized"""
        super().resizeEvent(event)
        self.label.resize(self.size())
    
    