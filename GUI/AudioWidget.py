import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
from PyQt6.QtWidgets import  QMainWindow, QWidget
import numpy as np
import modules.QueueSystem as qs
import threading
import sounddevice as sd
from PyQt6.QtWidgets import QVBoxLayout

class PlotWidget(QWidget):
    def __init__(self, parent=None, window=None):
        super(PlotWidget, self).__init__(parent)

        # Erstellen Sie ein PlotWidget-Objekt und fügen Sie es zum Fenster hinzu
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.plotItem.hideAxis('bottom')  # Versteckt die x-Achse
        self.plot_widget.plotItem.hideAxis('left')  # Versteckt die y-Achse
        #self.setCentralWidget(self.plot_widget)

        # Erstellen Sie ein Layout und fügen Sie das PlotWidget hinzu
        layout = QVBoxLayout()
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

        self.resize(window.column_width, 180)
        #self.resize(100, 100)
        self.move(2*window.column_width + 15, window.column_height_2//20 )

        # Erstellen Sie einen Timer, um das Diagramm regelmäßig zu aktualisieren
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # Aktualisieren Sie das Diagramm jede Sekunde

        # Definieren Sie eine Warteschlange, um die Lautstärkewerte zu speichern
        #qs.RMS_VALUES = deque(maxlen=500)

    def update_plot(self):
        # Erstellen Sie einen Zeitvektor
        time = np.arange(len(qs.RMS_VALUES)) / 2.0 #Ser_LOOP_RATE
        rms_values_array = np.array(qs.RMS_VALUES)

        # Plotten Sie die Daten
        self.plot_widget.plot(time, rms_values_array, clear=True)

    def audio_callback(self, indata, frames, time, status):
        volume_norm = np.linalg.norm(indata) * 10
        qs.RMS_VALUES.append(volume_norm)

    def start_audio_stream(self):
        with sd.InputStream(callback=self.audio_callback):
            while True:
                sd.sleep(1000)  # Warten Sie 1 Sekunde zwischen jedem Aufruf von sleep

    def playButtonClicked(self):
        threading.Thread(target=self.start_audio_stream, daemon=True).start()