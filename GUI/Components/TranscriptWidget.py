from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
import modules.QueueSystem as qs

class TranscriptWidget(QWidget):
    """Widget to display the transcript of the speech recognition system."""
    def __init__(self, window=None):
        """Constructor of the transcript widget.
        
        Args:
            window (QWidget): The parent window of the widget    
    """
        super().__init__()

        self.transcript_label = QLabel()
        self.transcript_label.setWordWrap(True)
        layout = QVBoxLayout()
        layout.addWidget(self.transcript_label)
        self.setLayout(layout)

        # self.resize(window.column_width, 150)
        self.resize(int(1.25*window.column_width), 120)
        self.move(window.frames[1].x() + int(window.column_width_title*1.5) - window.column_width//2 ,
        window.circle5_2_inner.y() -20)
        # self.move(2*window.column_width + 15, window.column_height_2//3)
        self.setStyleSheet(f"QFrame {{background-color: white; border-radius: 10px; border: 1px solid black;}}")

        qs.TRANSCRIPT_SPEECH.register_observer(self.update_transcript)
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.update_transcript)
        # self.timer.start(1000)  # Aktualisieren Sie das Label jede Sekunde

    def update_transcript(self, temp=None):
        """Update the transcript label with the last three entries in the transcript queue."""
        last_three_entries = [qs.TRANSCRIPT_SPEECH[i] for i in range(max(0, len(qs.TRANSCRIPT_SPEECH) - 3), len(qs.TRANSCRIPT_SPEECH))]
        text = "\n".join(last_three_entries)
        self.transcript_label.setText(text)