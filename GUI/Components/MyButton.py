from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt, pyqtSignal

class MyButton(QPushButton):
    """A custom button that emits signals when left or right clicked."""
    leftClicked = pyqtSignal()
    rightClicked = pyqtSignal()
    
    def mousePressEvent(self, event):
        """Emit the leftClicked or rightClicked signal when the button is clicked."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.leftClicked.emit()
        elif event.button() == Qt.MouseButton.RightButton:
            self.rightClicked.emit()

        super().mousePressEvent(event)