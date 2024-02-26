from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QTimer
from time import sleep
import modules.QueueSystem as qs
from PyQt6.QtCore import Qt
import cv2

class ImageWindow(QWidget):  # Inherit from QWidget instead of QMainWindow
    def __init__(self, parent=None, window=None, name="Image"):
        super(ImageWindow, self).__init__(parent)
        self.image_label = QLabel()
        self.window = window
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)  # Set the layout directly on this widget
        self.timer = QTimer()
        if name == "Image":
            self.resize(window.column_width, 180)
            self.move(2*window.column_width + 15, window.column_height_2//2 + 70)
            self.timer.timeout.connect(lambda: self.update_image())
        elif name == "Skeleton":
            self.resize(window.column_width, 180)
            self.move(2*window.column_width + 15, window.column_height_2//15 *14 + 15)
            self.timer.timeout.connect(lambda: self.update_image_skeleton())
        self.timer.start(50)  # Update every second

    def update_image(self):
        if self.window.START == True:
            # Assuming IMAGE_FACE_RAW is a global list that gets updated with numpy arrays representing images
            image = qs.IMAGE_FACE_RAW[len(qs.IMAGE_FACE_RAW) - 1]  # Get the latest image
            height, width, channel = image.shape
            bytes_per_line = 3 * width
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            qimage = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(qimage)
            scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(scaled_pixmap)
        else:
            sleep(1)

    def update_image_skeleton(self):
        if self.window.START == True:
            image = qs.IMAGE_BODY_SKEL[len(qs.IMAGE_BODY_SKEL) - 1]  # Get the latest image
            height, width, channel = image.shape
            bytes_per_line = 3 * width
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            qimage = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(qimage)
            scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(scaled_pixmap)
        else:
            sleep(1)