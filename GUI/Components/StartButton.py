# from PyQt6.QtWidgets import QPushButton
# from PyQt6.QtCore import Qt, pyqtSignal
# from PyQt6.QtGui import QPixmap, QIcon
#
#
# class StartButton(QPushButton):
#     """A custom button that emits signals when left or right clicked."""
#     leftClicked = pyqtSignal()
#     rightClicked = pyqtSignal()
#
#     def __init__(self):
#         QPushButton.__init__(self)
#      #   self.setIcon(QIcon('Mikrofon.png'))
#
#
#     def mousePressEvent(self, event):
#         """Emit the leftClicked or rightClicked signal when the button is clicked."""
#
#         if event.button() == Qt.MouseButton.LeftButton:
#             self.leftClicked.emit()
#         elif event.button() == Qt.MouseButton.RightButton:
#             self.rightClicked.emit()
#
#         super().mousePressEvent(event)

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QTimer

class StartButton(QPushButton):
    """A custom button that emits signals when left or right clicked, with an icon."""
    leftClicked = pyqtSignal()
    rightClicked = pyqtSignal()

    def __init__(self):
        QPushButton.__init__(self)
        self.icon_play = QIcon('GUI/Icons/play.png')
        self.icon_waiting = QIcon('GUI/Icons/waiting.png')

        self.setIcon(self.icon_play)  # Set the icon from the PNG file
        self.setIconSize(QPixmap('GUI/Icons/play.png').size()/10)  # Set the icon size to match the image size




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
            self.setIcon(self.icon_waiting)

        elif event.button() == Qt.MouseButton.RightButton:
            self.rightClicked.emit()


        super().mousePressEvent(event)
        self.setStyleSheet("""
                    QPushButton {
                        border: none;
                        background-color: transparent;
                    }
                """)

    def hide_button(self):
        """Hide the button after it is clicked."""
        self.hide()

    def hide(self):
        """Override the hide method to add custom behavior."""
        super().hide()  # Call the base class hide() method

    def show(self):
        self.setIcon(self.icon_play)
        super().show()