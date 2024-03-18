import sys
from PyQt6.QtWidgets import QTextEdit

class ConsoleOutput(QTextEdit):
    """Redirect the console output to a widget."""
    def __init__(self, parent=None):
        """Initialize the console output widget.
        
        Args:
            parent: The parent widget
        """
        super().__init__(parent)
        sys.stdout = self
        self.setStyleSheet("background-color: #f0f0f0;")
    def write(self, text):
        self.insertPlainText(text)

    def flush(self):
        pass