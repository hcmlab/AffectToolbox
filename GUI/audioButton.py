from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import QTimer, Qt
import pyqtgraph as pg
from pyqtgraph import mkPen
import numpy as np
from modules import QueueSystem as qs
from GUI.custom_button import CustomButton

# This widget handles the display of live audio data in a simple waveform plot
class AudioStreamWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.streaming = False

        # Set up the plotting area using pyqtgraph
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.plotItem.hideAxis('bottom')
        self.plot_widget.plotItem.hideAxis('left')
        self.plot_widget.setFixedHeight(100)

        # Layout configuration
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

        # Timer for periodic plot updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)

        # Border styling for visual clarity
        self.setStyleSheet("border: 2px solid green; border-radius: 4px;")

    def start_stream(self):
        if not self.streaming:
            self.streaming = True
            self.setFixedHeight(100)
            self.timer.start(100)# update every 100 ms
            self.setVisible(True)

    def stop_stream(self):
        self.streaming = False
        self.timer.stop()
        self.setFixedHeight(0)
        self.setVisible(False)

    def is_stream_running(self):
        return self.streaming

    # This method updates the plot with the latest audio data from the queue
    def update_plot(self):
        if not self.streaming:
            return

        try:
            audio_data = list(qs.AUDIO_QUEUE)[-1000:]  #Get last 1000 samples
            if not audio_data:
                return

            audio_array = np.array(audio_data)
            pen = mkPen(color="green")
            time_axis = np.arange(len(audio_array))
            self.plot_widget.plot(time_axis, audio_array, pen=pen, clear=True)
        except Exception as e:
            print("Error while plotting:", e)


# This container wraps the custom button and the associated AudioStreamWidget
class AudioStreamContainer(QWidget):
    def __init__(self, name, main_window=None):
        super().__init__()
        self.main_window = main_window

        # Create the button and the audio stream plot
        self.button = CustomButton(name, parent=self, main_window=self.main_window)
        self.stream = AudioStreamWidget()
        self.stream.setVisible(False)
        self.stream.setFixedWidth(self.button.width())

        # Connect button click to toggling the stream
        self.button.clicked.connect(self.toggle_stream)

        # Set up the vertical Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(0)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.stream, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(layout)

    def toggle_stream(self):
        if self.stream.is_stream_running():
            self.stream.stop_stream()
        else:
            self.stream.start_stream()

    # Deactivates the entire widget
    def deactivate(self):
        self.setVisible(False)
        self.button.setStyleSheet("")
        self.stream.stop_stream()

    # Adjusts the stream width to match the button width when resized
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.stream.isVisible():
            self.stream.setFixedWidth(self.button.width())



