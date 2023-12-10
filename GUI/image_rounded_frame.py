from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel
from GUI.rounded_frame import RoundedFrame

class ImageRoundedFrame(RoundedFrame):
    def __init__(self, text="", color="#0071c1", text_color="#c9ffff", font_size=20, border=False, image_path=None):
        super().__init__(text, color, text_color, font_size, border)
        
        if image_path:
            self.image_label = QLabel(self)
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(int(self.width()*0.8), int(self.height()*0.8), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)  # Change the size of the image
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the image
            self.layout.addWidget(self.image_label)