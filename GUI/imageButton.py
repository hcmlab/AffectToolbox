from config_defaults import DEFAULT_PARAMETERS
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap, QImage
from GUI.custom_button import CustomButton
from GUI.rightClickWindow import RightClickWindow
import cv2

# This widget displays images from a queue in a QLabel using a timer-based update
class ImageStreamWidget(QWidget):
    def __init__(self, queue, rate_key="CAMERA_LOOP_RATE"):
        super().__init__()
        self.queue = queue # Image source
        self.rate_key = rate_key
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
            self.update_refresh_rate()
            self.timer.start()
            self.streaming = True
            self.setVisible(True)

    def pause_stream(self):
        self.timer.stop()
        self.streaming = False

    def stop_stream(self):
        self.pause_stream()
        self.setVisible(False)

    def is_stream_running(self):
        return self.streaming

    def clear_display(self):
        self.label.clear()

    def update_refresh_rate(self):
        loop_rate = float(RightClickWindow.PARAMETERS[self.rate_key])
        if loop_rate <= 0:
            loop_rate = DEFAULT_PARAMETERS[self.rate_key]
        interval_ms = max(1, round(1000 / loop_rate))
        if self.timer.interval() != interval_ms:
            self.timer.setInterval(interval_ms)

    # Called by the timer to update the displayed image
    def update_image(self):
        if not self.streaming:
            return
        self.update_refresh_rate()
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
    def __init__(self, name, queue, main_window=None, button=None, rate_key="CAMERA_LOOP_RATE"):
        super().__init__()
        self.main_window = main_window

        # Create a labeled button and link it to the main window
        if button is None:
            button = CustomButton(f"{name}", parent=self, main_window=self.main_window)
        self.button = button

        # Set up the image stream widget
        self.stream = ImageStreamWidget(queue, rate_key=rate_key)
        self.stream.setVisible(False)

        # Layout with button and image stream
        layout = QVBoxLayout()
        layout.setContentsMargins(9, 9, 9, 9)
        layout.setSpacing(0)
        layout.addWidget(self.button)
        layout.addWidget(self.stream)
        self.setLayout(layout)

    def deactivate(self):
        self.setVisible(False)
        self.button.setStyleSheet("")  # Style is handled in toggle logic
        self.stream.stop_stream()
