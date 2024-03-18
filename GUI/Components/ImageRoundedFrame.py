from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel
from GUI.Components.RoundedFrame import RoundedFrame

class ImageRoundedFrame(RoundedFrame):
    """Class to create a rounded frame with an image inside it"""
    def __init__(self, text="", color="#0071c1", text_color="#c9ffff", font_size=20, border=False, image_path=None):
        """Constructor for the ImageRoundedFrame class.
        
        Args:
            text (str, optional): The text to display in the frame. Defaults to "".
            color (str, optional): The color of the frame. Defaults to "#0071c1".
            text_color (str, optional): The color of the text. Defaults to "#c9ffff".
            font_size (int, optional): The font size of the text. Defaults to 20.
            border (bool, optional): Whether to display a border around the frame. Defaults to False.
            image_path (str, optional): The path to the image to display in the frame. Defaults to None.
        """
        super().__init__(text, color, text_color, font_size, border)
        
        # Add the image to the frame
        if image_path:
            self.image_label = QLabel(self)
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(int(self.width()*0.8), int(self.height()*0.8), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)  
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
            self.layout.addWidget(self.image_label)