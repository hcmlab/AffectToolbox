from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer
import modules.QueueSystem as qs

class floatWidget(QFrame):
    def __init__(self, name="", color="#d9d9d9", font_size=20, border=True):
        
        super(floatWidget, self).__init__()
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
            self.number = round(qs.NEU_SENTIMENT[-1],2)
            self.label.setText("P:{:.2f}".format(self.number))
        elif self.name == "Facial_Pleasure":
            self.number = round(qs.VALENCE_FACE[len(qs.VALENCE_FACE) - 1],2)
            self.label.setText("P:{:.2f}".format(self.number))
        elif self.name == "Facial_Arousal":
            self.number = round(qs.AROUSAL_FACE[len(qs.AROUSAL_FACE) - 1],2)
            self.label.setText("A:{:.2f}".format(self.number))
        elif self.name == "Facial_Dominance":
            pass
        elif self.name == "Pose_Dominance":
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
        