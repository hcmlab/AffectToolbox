
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap

class StopButton(QPushButton):
    """A custom button that emits signals when left or right clicked, with an icon."""
    leftClicked = pyqtSignal()
    rightClicked = pyqtSignal()

    def __init__(self):
        QPushButton.__init__(self)
        self.setIcon(QIcon('GUI/Icons/stop.png'))  # Set the icon from the PNG file
        self.setIconSize(QPixmap('GUI/Icons/stop.png').size()/10)  # Set the icon size to match the image size
        self.setFlat(True)  # Remove button borders to make it look like an icon only
        self.setStyleSheet("""
            QPushButton {
                border: none;  /* Remove any border */
                outline: none;  /* Remove focus outline */
            }
            QPushButton:pressed {
                border: none;  /* Remove any border */
                outline: none;  /* Remove focus outline */
                background-color: black;  /* Prevent background change on press */
            }
        """)
        self.clicked.connect(self.hide_button)

    def mousePressEvent(self, event):
        """Emit the leftClicked or rightClicked signal when the icon is clicked."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.leftClicked.emit()

        elif event.button() == Qt.MouseButton.RightButton:
            self.rightClicked.emit()

        self.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
            }
        """)
        super().mousePressEvent(event)

    def hide_button(self):
        """Hide the button after it is clicked."""
        self.hide()