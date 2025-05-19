from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap, QImage
from custom_button import CustomButton
import cv2

# This widget displays images from a queue in a QLabel using a timer-based update
class ImageStreamWidget(QWidget):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue # Image source
        self.streaming = False

        # Display label for the image
        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFixedHeight(150)
        self.label.setStyleSheet("background-color: black;")

        # Layout setup
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Timer for periodic image updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_image)

    def start_stream(self):
        if not self.streaming:
            self.timer.start(500) # update every 500 ms
            self.streaming = True
            self.setVisible(True)

    def stop_stream(self):
        if self.streaming:
            self.timer.stop()
            self.streaming = False
            self.setVisible(False)

    def is_stream_running(self):
        return self.streaming

    # Called by the timer to update the displayed image
    def update_image(self):
        if self.queue and len(self.queue) > 0:
            image = self.queue[-1] # Use the latest image in the queue
            if hasattr(image, "shape"):
                height, width, channel = image.shape
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                qimage = QImage(image.data, width, height, 3 * width, QImage.Format.Format_RGB888).rgbSwapped()
                pixmap = QPixmap.fromImage(qimage)
                scaled = pixmap.scaled(200, 150, Qt.AspectRatioMode.KeepAspectRatio)
                self.label.setPixmap(scaled)

# This container combines a toggle button with the image stream widget
class ImageStreamContainer(QWidget):
    def __init__(self, name, queue, main_window=None):
        super().__init__()
        self.main_window = main_window

        # Create a labeled button and link it to the main window
        self.button = CustomButton(f"{name}", parent=self, main_window=self.main_window)

        # Set up the image stream widget
        self.stream = ImageStreamWidget(queue)
        self.stream.setVisible(False)

        # Connect button to toggling the stream
        self.button.clicked.connect(self.toggle_stream)

        # Layout with button and image stream
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.addWidget(self.button)
        layout.addWidget(self.stream)
        self.setLayout(layout)

    def toggle_stream(self):
        if self.stream.is_stream_running():
            self.stream.stop_stream()
        else:
            self.stream.start_stream()

    def deactivate(self):
        self.setVisible(False)
        self.button.setStyleSheet("")  # Style is handled in toggle logic
        self.stream.stop_stream()