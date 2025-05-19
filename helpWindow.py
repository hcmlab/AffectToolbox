from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
import webbrowser

class HelpWindow(QWidget):
    """
    This window displays a help video and a link to the related paper.
    It is designed to support new users by providing visual instructions and documentation.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AffectToolbox Help")
        self.setFixedSize(800, 700)

        # Main layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set dark theme with light text and highlighted link color
        self.setStyleSheet("""
            QWidget {
                background-color: black;
                color: white;
            }
            QLabel {
                color: lightblue;
            }
        """)

        # Set up video display widget
        self.video_widget = QVideoWidget()
        self.video_widget.setMinimumSize(800, 650)
        self.video_widget.show()

        # Create media player and link it to the video output
        self.media_player = QMediaPlayer(self)
        video_path = "HelpVideo.mp4"
        self.media_player.setSource(QUrl.fromLocalFile(video_path))
        self.media_player.setVideoOutput(self.video_widget)

        # Automatically start playback when the window opens
        self.media_player.play()
        self.media_player.mediaStatusChanged.connect(self.handle_media_status)

        # Create a clickable link label to the external paper
        self.link_label = QLabel('<a href="https://arxiv.org/pdf/2402.15195">AffectToolbox</a>')
        self.link_label.setOpenExternalLinks(True)
        self.link_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.link_label.setStyleSheet("font-size: 14px;")

        # Add widgets to the layout
        layout.addWidget(self.video_widget)
        layout.addSpacing(10)
        layout.addWidget(self.link_label)

        self.setLayout(layout)

    def handle_media_status(self, status):
        # Check if the media playback has reached the end
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            # Restart the video by setting the position back to the beginning
            self.media_player.setPosition(0)
            self.media_player.play()

