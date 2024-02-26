from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout

class RoundedFrameNoClick(QFrame):
    def __init__(self, text="", color="#0071c1", text_color="#c9ffff", font_size=20, border=False):
        
        super(RoundedFrameNoClick, self).__init__()
        self.layout = QVBoxLayout(self)
        self.label = QLabel(text, self)
        self.label.setStyleSheet(f"QLabel {{ color: {text_color}; font-size: {font_size}px; }}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text horizontally and vertically

        border_css = "border: 1px solid black;" if border else ""
        self.setStyleSheet(f"QFrame {{background-color: {color}; border-radius: 10px; {border_css}}}")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.label.resize(self.size())
    
    