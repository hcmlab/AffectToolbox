from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QDoubleSpinBox, QLabel, QSpacerItem, QSizePolicy, QLineEdit, QSpinBox

class RightClickWindow(QMainWindow):
    def __init__(self, parent=None, window=None, name=""):
        super(RightClickWindow, self).__init__(parent)
        self.resize(300, 300)

        # Create a central widget
        central_widget = QWidget()

        self.window = window

        self.layout = QVBoxLayout(central_widget)
        self.layout.setSpacing(5)

        # Create a QSpinBox
        if name == "Camera":
            self.AddDoubleSpinBox(baseValue=window.CAMERA_LOOP_RATE, name="Camera")
        elif name == "Kafka":
            self.AddIp(baseValue=window.KAFKA_IP, name="KAFKA")
            self.AddPort(baseValue=window.KAFKA_PORT, name="KAFKA")
            self.AddTopic(baseValue=window.KAFKA_TOPIC, name="KAFKA")
        elif name == "UDP":
            self.AddIp(baseValue=window.UDP_IP, name="UDP")
            self.AddPort(baseValue=window.UDP_PORT, name="UDP")
        elif name == "Sentiment":
            self.AddDoubleSpinBox(baseValue=window.SENTIMENT_LOOP_RATE, name="Sentiment")
        elif name == "Audio":
            self.AddDoubleSpinBox(baseValue=window.VAD_LOOP_RATE, name="Audio")
        elif name == "Pose":
            self.AddDoubleSpinBox(baseValue=window.POSE_LOOP_RATE, name="Pose")
        elif name == "FaceTracking":
            self.AddDoubleSpinBox(baseValue=window.FACE_MESH_RATE, name="FaceTracking")
        elif name == "Fusion":
            self.AddSpinBox(baseValue=window.SAMPLE_RATE, name="Fusion")

        # Erstellen Sie ein QSpacerItem
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        # Fügen Sie das QSpacerItem zum Layout hinzu
        self.layout.addItem(spacer)
        # Set the layout
        central_widget.setLayout(self.layout)

        # Set the central widget
        self.setCentralWidget(central_widget)

        # Connect the valueChanged signal to a slot
        #self.spinBox.valueChanged.connect(self.on_value_changed)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    
    def on_double_value_changed(self, value, name=""):
        # This method will be called whenever the value of the spinBox is changed
        value = round(value, 1)
        if name == "Camera":
            self.window.CAMERA_LOOP_RATE = value
        elif name == "SER":
            self.window.SER_LOOP_RATE = value
        elif name == "Sentiment":
            self.window.SENTIMENT_LOOP_RATE = value
        elif name == "Audio":
            self.window.VAD_LOOP_RATE = value
        elif name == "Pose":
            self.window.POSE_LOOP_RATE = value
        elif name == "FaceTracking":
            self.window.FACE_MESH_RATE = value
        elif name == "Fusion":
            self.window.SAMPLE_RATE = value
        #print(f"The {name}-Loop-Rate has been changed to {value}")

    def AddDoubleSpinBox(self, baseValue=0.0, name=""):
        self.doublespinBoxLabel = QLabel(f"{name} Loop Rate:")
        self.doublespinBoxLabel.setFixedSize(300, 20)
        self.doublespinBox = QDoubleSpinBox()
        self.doublespinBox.setFixedSize(300, 20)
        self.layout.addWidget(self.doublespinBoxLabel)
        self.layout.addWidget(self.doublespinBox)
        self.doublespinBox.setValue(baseValue)
        self.doublespinBox.setSingleStep(0.1)
        self.doublespinBox.valueChanged.connect(lambda value: self.on_value_changed(value=value, name=name))

    def on_value_changed(self, value, name=""):
        if name == "Fusion":
            self.window.SAMPLE_RATE = value
        #print(f"The {name}-Loop-Rate has been changed to {value}")

    def AddSpinBox(self, baseValue=0, name=""):
        self.spinBoxLabel = QLabel(f"{name} Sample Rate:")
        self.spinBoxLabel.setFixedSize(300, 20)
        self.spinBox = QSpinBox()
        self.spinBox.setFixedSize(300, 20)
        self.layout.addWidget(self.spinBoxLabel)
        self.layout.addWidget(self.spinBox)
        self.spinBox.setMaximum(48000)
        self.spinBox.setValue(baseValue)
        self.spinBox.setSingleStep(1000)
        self.spinBox.valueChanged.connect(lambda value: self.on_double_value_changed(value=value, name=name))

    def AddIp(self, baseValue='0.0.0.0', name=""):
        self.ipLabel = QLabel(f"{name}-IP Address:")
        self.ipLabel.setFixedSize(300, 20)
        self.ipLineEdit = QLineEdit()
        self.ipLineEdit.setFixedSize(300, 20)
        self.layout.addWidget(self.ipLabel)
        self.layout.addWidget(self.ipLineEdit)
        self.ipLineEdit.setText(baseValue)
        self.ipLineEdit.textChanged.connect(lambda  text: self.on_text_changed_IP(text=text, name=name))

    def on_text_changed_IP(self, text, name=""):
        # Diese Methode wird aufgerufen, wenn der Text im QLineEdit geändert wird
        if name == "UDP":
            self.window.UDP_IP = text
        if name == "KAFKA":
            self.window.KAFKA_IP = text
        #print(f"The IP address has been changed to {text}")

    def AddPort(self, baseValue=3000, name=""):
        self.portLabel = QLabel(f"{name}-Port:")
        self.portLabel.setFixedSize(300, 20)
        self.portLineEdit = QLineEdit()
        self.portLineEdit.setFixedSize(300, 20)
        self.layout.addWidget(self.portLabel)
        self.layout.addWidget(self.portLineEdit)
        self.portLineEdit.setText(str(baseValue))
        self.portLineEdit.textChanged.connect(lambda value: self.on_text_changed_port(value=value, name=name))

    def on_text_changed_port(self, value, name=""):
        # Diese Methode wird aufgerufen, wenn der Text im QLineEdit geändert wird
        if name == "UDP":
            self.window.UDP_PORT = int(value)
        if name == "KAFKA":
            self.window.KAFKA_PORT = int(value)
        #print(f"The {name}-Port has been changed to {value}")

    def AddTopic(self, baseValue='mithos', name=""):
        self.topicLabel = QLabel(f"{name}-Topic:")
        self.topicLabel.setFixedSize(300, 20)
        self.topicLineEdit = QLineEdit()
        self.topicLineEdit.setFixedSize(300, 20)
        self.layout.addWidget(self.topicLabel)
        self.layout.addWidget(self.topicLineEdit)
        self.topicLineEdit.setText(baseValue)
        self.topicLineEdit.textChanged.connect(lambda value: self.on_text_changed_topic(value=value, name=name))

    def on_text_changed_topic(self, value, name=""):
        # Diese Methode wird aufgerufen, wenn der Text im QLineEdit geändert wird
        if name == "KAFKA":
            self.window.KAFKA_TOPIC = value
        #print(f"The {name}-Topic has been changed to {value}")
            
        