import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
from PyQt6.QtWidgets import  QWidget
import numpy as np
import threading
import sounddevice as sd
from PyQt6.QtWidgets import QVBoxLayout
from pyqtgraph import mkPen

class PlotWidget(QWidget):
    def __init__(self, parent=None, window=None):
        super(PlotWidget, self).__init__(parent)

        # Erstellen Sie ein PlotWidget-Objekt und fügen Sie es zum Fenster hinzu
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.plotItem.hideAxis('bottom')  # Versteckt die x-Achse
        self.plot_widget.plotItem.hideAxis('left')  # Versteckt die y-Achse

        # Erstellen Sie ein Layout und fügen Sie das PlotWidget hinzu
        layout = QVBoxLayout()
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

        self.resize(window.column_width, 155)
        #self.resize(100, 100)
        self.move(2*window.column_width + 15, 3)

        # Erstellen Sie einen Timer, um das Diagramm regelmäßig zu aktualisieren
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # Aktualisieren Sie das Diagramm jede Sekunde

        self.audio_data = np.array([])

    def update_plot(self):
        # # Erstellen Sie einen Zeitvektor

        # Begrenzen Sie die Audiodaten auf die letzten 5 Sekunden
        last_5_seconds_audio_data = self.audio_data[-220500:]

        # Erstellen Sie einen Zeitvektor
        time = np.arange(len(last_5_seconds_audio_data)) / 2.0

        pen = mkPen(color="green")

        # Plotten Sie die Daten
        self.plot_widget.plot(time, last_5_seconds_audio_data, pen=pen, clear=True)

    def audio_callback(self, indata, frames, time, status):
        self.audio_data = np.append(self.audio_data, indata)

    def start_audio_stream(self):
        with sd.InputStream(callback=self.audio_callback):
            while True:
                sd.sleep(1000)  # Warten Sie 1 Sekunde zwischen jedem Aufruf von sleep

    def playButtonClicked(self):
        threading.Thread(target=self.start_audio_stream, daemon=True).start()