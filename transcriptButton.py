from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QTimer
from custom_button import CustomButton

class TranscriptWidget(QWidget):
    """
    Displays live transcript data from a queue.
    Shows the last few entries inside a styled QLabel.
    """
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.streaming = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_transcript)
        self.timer.setInterval(500)

        # Text display label
        self.label = QLabel("No transcript")
        self.label.setFixedHeight(100)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Styling for visibility and readability
        self.label.setStyleSheet("""
                    QLabel {
                        background-color: white;
                        color: black;
                        border: 1px solid black;
                        border-radius: 10px;
                        padding: 5px;
                        font-size: 11pt;
                    }
                """)

        # Layout setup
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label)
        self.setLayout(layout)



    def start_stream(self):
        #Starts displaying transcript content
        if not self.streaming:
            self.streaming = True
            self.setVisible(True)
            self.update_transcript()
            self.timer.start()

    def stop_stream(self):
        #Stops displaying the transcript and hides the widget
        if self.streaming:
            self.streaming = False
            self.setVisible(False)
            self.timer.stop()

    def is_stream_running(self):
        return self.streaming

    def update_transcript(self):
        #Updates the label with the last few transcript entries from the queue
        if self.streaming and self.queue and len(self.queue) > 0:
            last_entries = [self.queue[i] for i in range(max(0, len(self.queue) - 3), len(self.queue))]
            self.label.setText("\n".join(last_entries))


class TranscriptContainer(QWidget):
    """
    A container that combines a button with a transcript display area.
    """
    def __init__(self, name, queue, main_window=None):
        super().__init__()
        self.main_window = main_window

        # Button with right-click functionality
        self.button = CustomButton(name, parent=self, main_window=main_window)

        # Transcript widget
        self.stream = TranscriptWidget(queue)
        self.stream.setVisible(False)

        # Connect button to toggle functionality
        self.button.clicked.connect(self.toggle_stream)

        # Layout with button and transcript
        layout = QVBoxLayout()
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.setSpacing(0)
        layout.addWidget(self.stream)
        self.setLayout(layout)

    def toggle_stream(self):
        #Toggles the transcript stream on or off
        if self.stream.is_stream_running():
            self.stream.stop_stream()
        else:
            self.stream.start_stream()

    def deactivate(self):
        # Deactivates the component visually and functionally
        self.setVisible(False)
        self.button.setStyleSheet("")
        self.stream.stop_stream()
