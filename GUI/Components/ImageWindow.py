from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QTimer
from time import sleep
import modules.QueueSystem as qs
from PyQt6.QtCore import Qt
import cv2

class ImageWindow(QWidget):
    """Class to create a widget that displays an image stream"""  
    def __init__(self, parent=None, window=None, name="Image"):
        """Constructor for the ImageWindow class.
        
        Args:
            parent: The parent widget
            window: The main window
            name (str, optional): The name of the stream. Defaults to "Image".
        """
        super(ImageWindow, self).__init__(parent)
        self.image_label = QLabel()
        self.window = window
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)  
        self.timer = QTimer()
        #Check which stream is being displayed
        if name == "Image":
            #self.resize(window.column_width, 180)
            self.resize(135, 160)
            self.move(window.frames[1].x() + int(window.column_width_title*1.5) - self.width()//2 + 5, 
                      window.circle5_3_inner.y() - self.height()//4)
            #self.move(2*window.column_width + 15, window.column_height_2//2 + 70)
            #self.timer.timeout.connect(lambda: self.update_image())
            qs.IMAGE_FACE_PREPROCESSED.register_observer(self.update_image)
        elif name == "Skeleton":
            # self.resize(window.column_width, 180)
            self.resize(window.column_width_title, 125)
            self.move(window.frames[1].x() + int(window.column_width_title*1.5) - self.width()//2 ,
                        window.circle5_4_inner.y())
            qs.IMAGE_BODY_SKEL.register_observer(self.update_image_skeleton)
            # self.move(2*window.column_width + 15, window.column_height_2//15 *14 + 15)
            #self.timer.timeout.connect(lambda: self.update_image_skeleton())
        #self.timer.start(50)  

    def update_image(self, temp=None):
        """Method to update the image displayed in the window """
        if self.window.START == True:
            image = qs.IMAGE_FACE_PREPROCESSED[len(qs.IMAGE_FACE_PREPROCESSED) - 1]
            height, width, channel = image.shape
            bytes_per_line = 3 * width
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            qimage = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(qimage)
            scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(scaled_pixmap)
        # else:
        #     sleep(1)

    def update_image_skeleton(self, temp=None):
        """Method to update the image for the Skeleton stream displayed in the window"""
        if self.window.START == True:
            image = qs.IMAGE_BODY_SKEL[len(qs.IMAGE_BODY_SKEL) - 1]  # Get the latest image
            height, width, channel = image.shape
            bytes_per_line = 3 * width
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            qimage = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(qimage)
            scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(scaled_pixmap)
        # else:
        #     sleep(1)