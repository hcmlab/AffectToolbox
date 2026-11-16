from config_defaults import DEFAULT_PARAMETERS
from PySide6.QtWidgets import QMainWindow, QWidget, QDialog, QVBoxLayout, QSpacerItem, QSizePolicy, QDoubleSpinBox, QLabel, QLineEdit, QSpinBox
from PySide6.QtCore import Qt
from GUI.deviceSelector import DeviceSelector

class RightClickWindow(QDialog):
    """
    A settings dialog that appears when the user right-clicks on a functional button.
    Allows modifying parameters related to specific data streams or sensors.
    """

    # Editable settings, separate from the shared defaults
    PARAMETERS = DEFAULT_PARAMETERS.copy()

    # Mapping buttons to the relevant parameters
    BUTTON_PARAMETER_MAPPING = {
        "Audio": ["SAMPLE_RATE", "MIC_CHUNKS"],
        "VoiceActivity": ["VAD_LOOP_RATE", "VAD_THRESHOLD"],
        "PARALINGUISTIC": [
            "SER_LOOP_RATE", "FUSION_VOICE_SPEED", "SER_VALENCE_OFFSET",
            "FUSION_VOICE_VALENCE_WEIGHT", "FUSION_VOICE_VALENCE_BOOST",
            "SER_AROUSAL_OFFSET", "FUSION_VOICE_AROUSAL_WEIGHT", "FUSION_VOICE_AROUSAL_BOOST",
            "SER_DOMINANCE_OFFSET", "FUSION_VOICE_DOMINANCE_WEIGHT", "FUSION_VOICE_DOMINANCE_BOOST"
        ],
        "Transcript": ["STT_LOOP_RATE", "STT_WINDOW_SIZE"],
        "SENTIMENT": ["SENTIMENT_LOOP_RATE", "FUSION_SENTIMENT_SPEED", "FUSION_SENTIMENT_WEIGHT", "FUSION_SENTIMENT_BOOST"],
        "Video": ["CAMERA_LOOP_RATE"],
        "FaceTracking": ["FACE_PADDING", "FACE_MESH_RATE"],
        "FACIALEXPRESSION": [
            "ER_LOOP_RATE", "FUSION_FACE_SPEED", "FUSION_FACE_VALENCE_WEIGHT", "FUSION_FACE_VALENCE_BOOST",
            "FUSION_FACE_AROUSAL_WEIGHT", "FUSION_FACE_AROUSAL_BOOST",
            "FUSION_FACE_DOMINANCE_WEIGHT", "FUSION_FACE_DOMINANCE_BOOST"
        ],
        "POSE": ["POSE_LOOP_RATE", "FUSION_POSE_SPEED", "FUSION_POSE_DOMINANCE_WEIGHT", "FUSION_POSE_DOMINANCE_BOOST"],
        "FUSION": ["FUSION_LOOP_RATE", "FUSION_SPEED"],
        "KAFKA": ["KAFKA_IP", "KAFKA_PORT", "KAFKA_TOPIC", "SEND_LOOP_RATE"],
        "UDP": ["UDP_IP", "UDP_PORT", "SEND_LOOP_RATE"]
    }


    def __init__(self, parent=None, window=None, name=""):
        """
        Initialize the settings window and load UI
        based on the button name.
        """
        super(RightClickWindow, self).__init__(parent)
        self.PARAMETERS = RightClickWindow.PARAMETERS
        self.name = name
        self.window = window
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.resize(300, 300)

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.add_parameter_widgets()

        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.layout.addItem(spacer)

    def add_parameter_widgets(self):

       # Adds parameter controls dynamically depending on which button was clicked
        params_to_show = self.BUTTON_PARAMETER_MAPPING.get(self.name, [])

        for param_name in params_to_show:
            param_value = self.PARAMETERS.get(param_name)
            if param_value is None:
                continue

            if "PORT" in param_name and isinstance(param_value, int):
                self.add_port_input(param_name, param_value)
            elif "TOPIC" in param_name and isinstance(param_value, str):
                self.add_topic_input(param_name, param_value)
            elif isinstance(param_value, int):
                self.add_int_spinbox(param_name, param_value)
            elif isinstance(param_value, float):
                self.add_double_spinbox(param_name, param_value)
            elif isinstance(param_value, str):
                self.add_ip_input(param_name, param_value)

        if self.name == "Micro":
            selector = DeviceSelector(parent=self, parameters=self.PARAMETERS, name="Micro")
            self.layout.addWidget(selector)

        if self.name == "Camera":
            selector = DeviceSelector(parent=self, parameters=self.PARAMETERS, name="Camera")
            self.layout.addWidget(selector)

    def add_int_spinbox(self, variableName, baseValue):
        label = QLabel(f"{variableName}:")
        spinBox = QSpinBox()
        spinBox.setFixedSize(200, 25)
        spinBox.setMinimum(-100000)
        spinBox.setMaximum(48000)
        spinBox.setSingleStep(1000)
        spinBox.setValue(baseValue)
        spinBox.valueChanged.connect(lambda value: self.on_value_changed(value, variableName))

        self.layout.addWidget(label)
        self.layout.addWidget(spinBox)
    
    def add_double_spinbox(self, variableName, baseValue):
        label = QLabel(f"{variableName}:")
        spinBox = QDoubleSpinBox()
        spinBox.setFixedSize(200, 25)
        spinBox.setDecimals(2) 
        spinBox.setMinimum(-100000.0)
        spinBox.setMaximum(100000.0)
        spinBox.setSingleStep(0.1)
        spinBox.setValue(baseValue)
        spinBox.valueChanged.connect(lambda value: self.on_value_changed(value, variableName))

        self.layout.addWidget(label)
        self.layout.addWidget(spinBox)

    def add_ip_input(self, variableName, baseValue):
        label = QLabel(f"{variableName}:")
        lineEdit = QLineEdit()
        lineEdit.setFixedSize(200, 25)
        lineEdit.setText(baseValue)
        lineEdit.textChanged.connect(lambda value: self.on_value_changed(value, variableName))

        self.layout.addWidget(label)
        self.layout.addWidget(lineEdit)

    def add_port_input(self, variableName, baseValue):
        label = QLabel(f"{variableName}:")
        lineEdit = QLineEdit()
        lineEdit.setFixedSize(200, 25)
        lineEdit.setText(str(baseValue))
        #lineEdit.setValidator(QIntValidator(minValue, maxValue))  # Nur Zahlen erlaubt
        lineEdit.textChanged.connect(lambda value: self.on_text_changed_port(value, variableName))

        self.layout.addWidget(label)
        self.layout.addWidget(lineEdit)

    def add_topic_input(self, variableName, baseValue):
        label = QLabel(f"{variableName}:")
        lineEdit = QLineEdit()
        lineEdit.setFixedSize(200, 25)
        lineEdit.setText(baseValue)
        lineEdit.textChanged.connect(lambda value: self.on_text_changed_topic(value, variableName))

        self.layout.addWidget(label)
        self.layout.addWidget(lineEdit)

    def on_value_changed(self, value, variableName):
        self.PARAMETERS[variableName] = value
        print("value changed")






        