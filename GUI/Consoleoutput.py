import sys
from PyQt6.QtWidgets import QTextEdit

class ConsoleOutput(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        sys.stdout = self
        #sys.stderr = self

    def write(self, text):
        self.insertPlainText(text)

    def flush(self):
        pass