from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt, pyqtSignal

class MyButton(QPushButton):
    leftClicked = pyqtSignal()
    rightClicked = pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.leftClicked.emit()
        elif event.button() == Qt.MouseButton.RightButton:
            self.rightClicked.emit()

        super().mousePressEvent(event)