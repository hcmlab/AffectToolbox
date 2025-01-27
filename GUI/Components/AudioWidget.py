import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
from PyQt6.QtWidgets import  QWidget
import numpy as np
import threading
import sounddevice as sd
from PyQt6.QtWidgets import QVBoxLayout
from pyqtgraph import mkPen

class PlotWidget(QWidget):
    """A widget to plot the audio data in real-time"""
    def __init__(self, parent=None, window=None):
        """Initialize the plot widget.
        
        Args:
            parent: The parent widget
            window: The main window
        """
        super(PlotWidget, self).__init__(parent)

        # Create PlotWidget Object and add it to the window
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.plotItem.hideAxis('bottom')  # Hide x-axis
        self.plot_widget.plotItem.hideAxis('left')  # Hide y-axis

        # Create a layout and add the plot widget to it
        layout = QVBoxLayout()
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

        # Set the size and position of the widget
        self.resize(window.column_width, 100)#155
        self.move(window.frames[1].x() + int(window.column_width_title*1.5) - self.width()//2 ,
        window.circle5_1_inner.y() +2 )
        # self.move(2*window.column_width + 15, window.LINEWIDTH)

        # Create a timer to update the plot
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # Update the plot every 1000 ms

        self.audio_data = np.array([])

    def update_plot(self):
        # Limit the audio data to the last 5 seconds
        last_5_seconds_audio_data = self.audio_data[-220500:]

        # Create a time array
        time = np.arange(len(last_5_seconds_audio_data)) / 2.0

        pen = mkPen(color="green")

        # Plot the audio data
        self.plot_widget.plot(time, last_5_seconds_audio_data, pen=pen, clear=True)

    def audio_callback(self, indata, frames, time, status):
        self.audio_data = np.append(self.audio_data, indata)

    def start_audio_stream(self):
        with sd.InputStream(callback=self.audio_callback):
            while True:
                sd.sleep(1000)  

    def playButtonClicked(self):
        threading.Thread(target=self.start_audio_stream, daemon=True).start()