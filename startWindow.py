from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from helpWindow import HelpWindow
import os

class StartWindow(QWidget):
    """
    The StartWindow is the entry point of the GUI.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AffectToolbox")

        # Set dark background with styled text
        self.setStyleSheet("""
            QWidget {
                background-color: black;
                color: white;
            }
            QLabel {
                color: lightblue;
            }
        """)

        # Vertical main layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Load and display logo image
        self.logo = QLabel()
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Ordner, wo das Skript liegt
        image_path = os.path.join(script_dir, "AffectToolbox.jpg")
        pixmap = QPixmap(image_path)
        self.logo.setPixmap(pixmap.scaled(650, 550, Qt.AspectRatioMode.KeepAspectRatio))
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Define common button style
        button_style = """
            QPushButton {
                font-size: 16pt;
                font-weight: bold;
                color: white;
                background-color: #1E90FF; 
                border-radius: 8px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #4682B4;
            }
        """

        # Start Button
        self.start_button = QPushButton("Start")
        self.start_button.setFixedWidth(150)
        self.start_button.setStyleSheet(button_style)

        # Help Button
        self.help_button = QPushButton("Help")
        self.help_button.setFixedWidth(150)
        self.help_button.setStyleSheet(button_style)

        # Horizontal layout for buttons
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(self.start_button)
        button_layout.addSpacing(80)  # Space between buttons
        button_layout.addWidget(self.help_button)

        # Add widgets to the main layout
        layout.addWidget(self.logo)
        layout.addSpacing(20)
        layout.addLayout(button_layout)
        layout.setContentsMargins(50, 30, 50, 80)

        self.setLayout(layout)

        #  Connect buttons to actions
        self.start_button.clicked.connect(self.start_main_window)
        self.help_button.clicked.connect(self.open_help)

        self.main_window = None  # Placeholder for the actual application window

    def start_main_window(self):
        # Closes the start window and opens the main GUI
        from mainWindow import MainWindow # Lazy import to avoid circular dependency
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def open_help(self):
        #Opens the help window with video and external documentation.
        self.help_window = HelpWindow()
        self.help_window.show()
