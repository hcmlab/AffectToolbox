from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer
import modules.QueueSystem as qs

class FloatWidget(QFrame):
    """Class to create a Widget that displays a float number in a frame with a label and a timer to update the number every second"""
    def __init__(self, name="", color="#d9d9d9", font_size=20, border=True):
        """Constructor for the FloatWidget class.
        
        Args:
            name (str, optional): The name of the widget. Defaults to "".
            color (str, optional): The color of the widget. Defaults to "#d9d9d9".
            font_size (int, optional): The font size of the label. Defaults to 20.
            border (bool, optional): Whether to display a border around the widget. Defaults to True.
        """
        super(FloatWidget, self).__init__()
        self.name = name
        self.layout = QVBoxLayout(self)
        self.number = 0.0
        self.label = QLabel(str(self.number), self)
        self.label.setStyleSheet(f"QLabel {{ color: black; font-size: {font_size}px; }}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text horizontally and vertically

        self.border_css = "border: 1px solid black;" if border else ""
        self.setStyleSheet(f"QFrame {{background-color: {color}; border-radius: 10px; {self.border_css}}}")
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.update_number())
        self.timer.start(1000)
        
        
    def update_number(self):
        """Function to update the number in the label every second depending on the name of the widget"""
        if self.name == "Para_Pleasure":
            self.number = round(qs.VALENCE_SPEECH[len(qs.VALENCE_SPEECH) - 1],2)
            self.label.setText("P:{:.2f}".format(self.number))
        elif self.name == "Para_Arousal":
            self.number = round(qs.AROUSAL_SPEECH[len(qs.AROUSAL_SPEECH) - 1],2)
            self.label.setText("A:{:.2f}".format(self.number))
        elif self.name == "Para_Dominance":
            self.number = round(qs.DOMINANCE_SPEECH[len(qs.DOMINANCE_SPEECH) - 1],2)
            self.label.setText("D:{:.2f}".format(self.number))
        elif self.name == "Sent_Pleasure":
            self.number = round(qs.VALENCE_SENTIMENT[len(qs.VALENCE_SENTIMENT) - 1],2)
            self.label.setText("P:{:.2f}".format(self.number))
        elif self.name == "Facial_Pleasure":
            self.number = round(qs.VALENCE_FACE[len(qs.VALENCE_FACE) - 1],2)
            self.label.setText("P:{:.2f}".format(self.number))
        elif self.name == "Facial_Arousal":
            self.number = round(qs.AROUSAL_FACE[len(qs.AROUSAL_FACE) - 1],2)
            self.label.setText("A:{:.2f}".format(self.number))
        elif self.name == "Facial_Dominance":
            self.number = round(qs.DOMINANCE_FACE[len(qs.DOMINANCE_FACE) - 1], 2)
            self.label.setText("D:{:.2f}".format(self.number))
            pass
        elif self.name == "Pose_Dominance":
             # Needed to be implemented within the AffectPipeline
            pass
        elif self.name == "Pleasure":
            self.number = round(qs.FUSION[len(qs.FUSION) - 1][0],2)
            self.label.setText("P:{:.2f}".format(self.number))
        elif self.name == "Arousal":
            self.number = round(qs.FUSION[len(qs.FUSION) - 1][1],2)
            self.label.setText("A:{:.2f}".format(self.number))
        elif self.name == "Dominance":
            self.number = round(qs.FUSION[len(qs.FUSION) - 1][2],2)
            self.label.setText("D:{:.2f}".format(self.number))
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.label.resize(self.size())
        