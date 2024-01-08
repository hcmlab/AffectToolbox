from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QSizePolicy
from PyQt6.QtCore import Qt 

class RightClickWidget(QLabel):
    def __init__(self, parent=None, window=None):
        super(RightClickWidget, self).__init__(parent)

        # Set the background color and size of the label
        self.setStyleSheet("background-color: gray;")
        self.setFixedSize(300, 300)

        # Create a layout for the label
        self.layout = QVBoxLayout(self)

        # Add buttons
        self.button1 = QPushButton("Button 1", self)
        self.button2 = QPushButton("Button 2", self)
        self.button3 = QPushButton("Close", self)

        # Set the size policy and height of the buttons
        button_height = 100
        for button in [self.button1, self.button2]:
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            button.setFixedHeight(button_height)

        self.button3.setFixedSize(50, 50)
        self.button3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # Add the buttons to the layout
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.setAlignment(self.button3, Qt.AlignmentFlag.AlignCenter)

        # Set the spacing of the layout
        self.layout.setSpacing(0)  # Set the spacing to 10

        # Change the color of the buttons
        self.button1.setStyleSheet("background-color: white; border: 2px solid black;")
        self.button2.setStyleSheet("background-color: white; border: 2px solid black;")
        self.button3.setStyleSheet("background-color: white; border: 2px solid black;")

        self.button3.clicked.connect(lambda: on_button3_clicked(self, window))

        # Set the widget as a window
        self.setWindowFlags(Qt.WindowType.Popup)
    
def on_button3_clicked(self, window):
    # Do something
    print("Button3 was clicked!")
    window.TRANSCRIPTMENU = False
    # Close the widget
    self.close()