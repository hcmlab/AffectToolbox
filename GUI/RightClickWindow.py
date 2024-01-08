from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QSpinBox

class RightClickWindow(QMainWindow):
    def __init__(self, parent=None, window=None):
        super(RightClickWindow, self).__init__(parent)
        self.resize(300, 300)
        layout = QVBoxLayout()

        # Create a QSpinBox
        self.spinBox = QSpinBox()

        # Add the QSpinBox to the layout
        layout.addWidget(self.spinBox)

                        # Set the layout
        self.setLayout(layout)

        # Connect the valueChanged signal to a slot
        self.spinBox.valueChanged.connect(self.on_value_changed)
        self.setWindowFlags( Qt.WindowType.WindowStaysOnTopHint)
    
    def on_value_changed(self, value):
        # This method will be called whenever the value of the spinBox is changed
        print(f"The value has been changed to {value}")
