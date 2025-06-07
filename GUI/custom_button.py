from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt
from GUI.initSettingWindow import InitSettingWindow

class CustomButton(QPushButton):
    """
    A custom QPushButton that can detect right-clicks.
    On right-click, it opens a settings window via the main window reference.
    """
    def __init__(self, text, parent=None, main_window=None):
        super().__init__(text, parent)
        self.main_window = main_window
        self.base_text = text

    def mousePressEvent(self, event):
        # Check if the click was a right-click
        if event.button() == Qt.MouseButton.RightButton:
            InitSettingWindow(self)

        else:
            # For left-click or other buttons perform the default behavior
            super().mousePressEvent(event)