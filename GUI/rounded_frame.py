from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import pyqtSignal
from GUI.RightClickWindow import RightClickWindow
from PyQt6.QtCore import QEvent

class RoundedFrame(QFrame):
    clicked = pyqtSignal()
    rightClicked = pyqtSignal(QEvent)
    def __init__(self, text="", color="#0071c1", text_color="#c9ffff", font_size=20, border=False):
        
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
        super().resizeEvent(event)
        self.label.resize(self.size())

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        elif event.button() == Qt.MouseButton.RightButton:
            self.rightClicked.emit(event)
        super().mousePressEvent(event)
        
        
    def toggleColor(self):
        if self.color == self.basecolor:
            self.setStyleSheet(f"QFrame {{background-color: green; border-radius: 10px; {self.border_css}}}")
            self.color = "green"
        elif self.color == "green":
            self.setStyleSheet(f"QFrame {{background-color: {self.basecolor}; border-radius: 10px; {self.border_css}}}")
            self.color = self.basecolor