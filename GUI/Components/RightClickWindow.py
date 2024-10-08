from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QDoubleSpinBox, QLabel, QSpacerItem, QSizePolicy, QLineEdit, QSpinBox
from GUI.Components.DeviceSelector import DeviceSelector
from GUI.Variables import changeValues

class RightClickWindow(QMainWindow):
    """A window that pops up when the user right-clicks on a frame. It allows the user to change the settings of the different sensors and data streams."""
    def __init__(self, parent=None, window=None, name=""):
        """Constructor for the RightClickWindow class.
        
        Args:
            parent (QWidget): The parent widget
            window (MainWindow): The main window of the application
            name (str): The name of the widget that was right-clicked
        """
        super(RightClickWindow, self).__init__(parent)
        self.resize(300, 300)

        # Create a central widget
        central_widget = QWidget()

        self.window = window
        self.name = name
        self.layout = QVBoxLayout(central_widget)
        self.layout.setSpacing(5)

        #Check which widget is rightlcicked and add the corresponding settings into a layout
        if name == "Camera":
            self.Device = DeviceSelector(window=window, name="Camera")
            self.layout.addWidget(self.Device)
        elif name == "Microphone":
            self.Device = DeviceSelector(window=window, name="Microphone")
            self.layout.addWidget(self.Device)
        elif name == "Video":
            self.CameraLoopRate = None
            self.CameraLoopRateLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.CameraLoopRate, Labelinstance=self.CameraLoopRateLabel,
                                  baseValue=window.CAMERA_LOOP_RATE, variableName="CAMERA_LOOP_RATE")
        elif name == "FaceTracking":
            self.FaceTrackingPadding = None
            self.FaceTrackingPaddingLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FaceTrackingPadding, Labelinstance=self.FaceTrackingPaddingLabel,
                                  baseValue=window.FACE_PADDING, variableName="FACE_PADDING")
            self.FaceMeshLoopRate = None
            self.FaceMeshLoopRateLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FaceMeshLoopRate, Labelinstance=self.FaceMeshLoopRateLabel,
                                  baseValue=window.FACE_MESH_RATE, variableName="FACE_MESH_RATE")
        elif name == "FacialExpression":
            self.ERLoopRate = None
            self.ERLoopRateLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.ERLoopRate, Labelinstance=self.ERLoopRateLabel,
                                  baseValue=window.ER_LOOP_RATE, variableName="ER_LOOP_RATE")

            self.FusionFaceSpeed = None
            self.FusionFaceSpeedLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionFaceSpeed, Labelinstance=self.FusionFaceSpeedLabel,
                                  baseValue=window.FUSION_FACE_SPEED, variableName="FUSION_FACE_SPEED")

            self.FusionFaceValenceWeight = None
            self.FusionFaceValenceWeightLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionFaceValenceWeight,
                                  Labelinstance=self.FusionFaceValenceWeightLabel,
                                  baseValue=window.FUSION_FACE_VALENCE_WEIGHT,
                                  variableName="FUSION_FACE_VALENCE_WEIGHT")
            self.FusionFaceValenceBoost = None
            self.FusionFaceValenceBoostLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionFaceValenceBoost,
                                  Labelinstance=self.FusionFaceValenceBoostLabel,
                                  baseValue=window.FUSION_FACE_VALENCE_BOOST,
                                  variableName="FUSION_FACE_VALENCE_BOOST")

            self.FusionFaceArousalWeight = None
            self.FusionFaceArousalWeightLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionFaceArousalWeight,
                                  Labelinstance=self.FusionFaceArousalWeightLabel,
                                  baseValue=window.FUSION_FACE_AROUSAL_WEIGHT,
                                  variableName="FUSION_FACE_AROUSAL_WEIGHT")
            self.FusionFaceArousalBoost = None
            self.FusionFaceArousalBoostLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionFaceArousalBoost,
                                  Labelinstance=self.FusionFaceArousalBoostLabel,
                                  baseValue=window.FUSION_FACE_AROUSAL_BOOST,
                                  variableName="FUSION_FACE_AROUSAL_BOOST")

            self.FusionFaceDominanceWeight = None
            self.FusionFaceDominanceWeightLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionFaceDominanceWeight,
                                  Labelinstance=self.FusionFaceDominanceWeightLabel,
                                  baseValue=window.FUSION_FACE_DOMINANCE_WEIGHT,
                                  variableName="FUSION_FACE_DOMINANCE_WEIGHT")
            self.FusionFaceDominanceBoost = None
            self.FusionFaceDominanceBoostLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionFaceDominanceBoost,
                                  Labelinstance=self.FusionFaceDominanceBoostLabel,
                                  baseValue=window.FUSION_FACE_DOMINANCE_BOOST,
                                  variableName="FUSION_FACE_DOMINANCE_BOOST")
        elif name == "Audio":
            self.AddIntSpinBox(baseValue=window.SAMPLE_RATE, variableName="SAMPLE_RATE")
            self.AddIntSpinBox(baseValue=window.MIC_CHUNKS, variableName="MIC_CHUNKS")
        elif name == "VoiceActivity":
            self.VADLoopRate = None
            self.VADLoopRateLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.VADLoopRate, Labelinstance=self.VADLoopRateLabel,
                                  baseValue=window.VAD_LOOP_RATE, variableName="VAD_LOOP_RATE")
            self.VADTreshold = None
            self.VADTresholdLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.VADTreshold, Labelinstance=self.VADTresholdLabel,
                                  baseValue=window.VAD_THRESHOLD, variableName="VAD_THRESHOLD")
        elif name == "Para":
            self.SERLoopRate = None
            self.SERLoopRateLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.SERLoopRate, Labelinstance=self.SERLoopRateLabel,
                                  baseValue=window.SER_LOOP_RATE, variableName="SER_LOOP_RATE")

            self.FusionVoiceSpeed = None
            self.FusionVoiceSpeedLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionVoiceSpeed, Labelinstance=self.FusionVoiceSpeedLabel,
                                  baseValue=window.FUSION_VOICE_SPEED, variableName="FUSION_VOICE_SPEED")

            self.SerValenceOffset = None
            self.SerValenceOffsetLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.SerValenceOffset,
                                  Labelinstance=self.SerValenceOffsetLabel,
                                  baseValue=window.SER_VALENCE_OFFSET,
                                  variableName="SER_VALENCE_OFFSET")

            self.FusionVoiceValenceWeight = None
            self.FusionVoiceValenceWeightLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionVoiceValenceWeight,
                                  Labelinstance=self.FusionVoiceValenceWeightLabel,
                                  baseValue=window.FUSION_VOICE_VALENCE_WEIGHT,
                                  variableName="FUSION_VOICE_VALENCE_WEIGHT")
            self.FusionVoiceValenceBoost = None
            self.FusionVoiceValenceBoostLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionVoiceValenceBoost,
                                  Labelinstance=self.FusionVoiceValenceBoostLabel,
                                  baseValue=window.FUSION_VOICE_VALENCE_BOOST,
                                  variableName="FUSION_VOICE_VALENCE_BOOST")

            self.SerArousalOffset = None
            self.SerArousalOffsetLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.SerArousalOffset,
                                  Labelinstance=self.SerArousalOffsetLabel,
                                  baseValue=window.SER_AROUSAL_OFFSET,
                                  variableName="SER_AROUSAL_OFFSET")

            self.FusionVoiceArousalWeight = None
            self.FusionVoiceArousalWeightLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionVoiceArousalWeight,
                                  Labelinstance=self.FusionVoiceArousalWeightLabel,
                                  baseValue=window.FUSION_VOICE_AROUSAL_WEIGHT,
                                  variableName="FUSION_VOICE_AROUSAL_WEIGHT")
            self.FusionVoiceArousalBoost = None
            self.FusionVoiceArousalBoostLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionVoiceArousalBoost,
                                  Labelinstance=self.FusionVoiceArousalBoostLabel,
                                  baseValue=window.FUSION_VOICE_AROUSAL_BOOST,
                                  variableName="FUSION_VOICE_AROUSAL_BOOST")

            self.SerDominanceOffset = None
            self.SerDominanceOffsetLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.SerDominanceOffset,
                                  Labelinstance=self.SerDominanceOffsetLabel,
                                  baseValue=window.SER_DOMINANCE_OFFSET,
                                  variableName="SER_DOMINANCE_OFFSET")

            self.FusionVoiceDominanceWeight = None
            self.FusionVoiceDominanceWeightLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionVoiceDominanceWeight,
                                  Labelinstance=self.FusionVoiceDominanceWeightLabel,
                                  baseValue=window.FUSION_VOICE_DOMINANCE_WEIGHT,
                                  variableName="FUSION_VOICE_DOMINANCE_WEIGHT")
            self.FusionVoiceDominanceBoost = None
            self.FusionVoiceDominanceBoostLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionVoiceDominanceBoost,
                                  Labelinstance=self.FusionVoiceDominanceBoostLabel,
                                  baseValue=window.FUSION_VOICE_DOMINANCE_BOOST,
                                  variableName="FUSION_VOICE_DOMINANCE_BOOST")
        elif name == "Transcript":
            self.STTLoopRate = None
            self.STTLoopRateLabel = None
            self.AddDoubleSpinBox( SpinBoxinstance=self.STTLoopRate, Labelinstance=self.STTLoopRateLabel,
                                   baseValue=window.STT_LOOP_RATE, variableName="STT_LOOP_RATE")
            self.STTWindowSize = None
            self.STTWindowSizeLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.STTWindowSize, Labelinstance=self.STTWindowSizeLabel,
                                  baseValue=window.STT_WINDOW_SIZE, variableName="STT_WINDOW_SIZE")
        elif name == "Sentiment":
            self.SentimentLoopRate = None
            self.SentimentLoopRateLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.SentimentLoopRate, Labelinstance=self.SentimentLoopRateLabel,
                                  baseValue=window.SENTIMENT_LOOP_RATE, variableName="SENTIMENT_LOOP_RATE")

            self.FusionSentimentSpeed = None
            self.FusionSentimentSpeedLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionSentimentSpeed,
                                  Labelinstance=self.FusionSentimentSpeedLabel,
                                  baseValue=window.FUSION_SENTIMENT_SPEED, variableName="FUSION_SENTIMENT_SPEED")

            self.FusionSentimentWeight = None
            self.FusionSentimentWeightLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionSentimentWeight,
                                  Labelinstance=self.FusionSentimentWeightLabel,
                                  baseValue=window.FUSION_SENTIMENT_WEIGHT,
                                  variableName="FUSION_SENTIMENT_WEIGHT")
            self.FusionSentimentBoost = None
            self.FusionSentimentBoostLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionSentimentBoost,
                                  Labelinstance=self.FusionSentimentBoostLabel,
                                  baseValue=window.FUSION_SENTIMENT_BOOST,
                                  variableName="FUSION_SENTIMENT_BOOST")
        elif name == "Pose":
            self.PoseLoopRate = None
            self.PoseLoopRateLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.PoseLoopRate, Labelinstance=self.PoseLoopRateLabel,
                                  baseValue=window.POSE_LOOP_RATE, variableName="POSE_LOOP_RATE")

            self.FusionPoseSpeed = None
            self.FusionPoseSpeedLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionPoseSpeed,
                                  Labelinstance=self.FusionPoseSpeedLabel,
                                  baseValue=window.FUSION_POSE_SPEED, variableName="FUSION_POSE_SPEED")

            self.FusionPoseDominanceWeight = None
            self.FusionPoseDominanceWeightLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionPoseDominanceWeight,
                                  Labelinstance=self.FusionPoseDominanceWeightLabel,
                                  baseValue=window.FUSION_POSE_DOMINANCE_WEIGHT,
                                  variableName="FUSION_POSE_DOMINANCE_WEIGHT")
            self.FusionPoseDominanceBoost = None
            self.FusionPoseDominanceBoostLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionPoseDominanceBoost,
                                  Labelinstance=self.FusionPoseDominanceBoostLabel,
                                  baseValue=window.FUSION_POSE_DOMINANCE_BOOST,
                                  variableName="FUSION_POSE_DOMINANCE_BOOST")
        elif name == "Fusion":
            self.FusionLoopRate = None
            self.FusionLoopRateLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionLoopRate, Labelinstance=self.FusionLoopRateLabel,
                                  baseValue=window.FUSION_LOOP_RATE, variableName="FUSION_LOOP_RATE")

            self.FusionSpeed = None
            self.FusionSpeedLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.FusionSpeed, Labelinstance=self.FusionSpeedLabel,
                                  baseValue=window.FUSION_SPEED, variableName="FUSION_SPEED")
        elif name == "Kafka":
            self.AddIp(baseValue=window.KAFKA_IP, variableName="KAFKA_IP")
            self.AddPort(baseValue=window.KAFKA_PORT, variableName="KAFKA_PORT")
            self.AddTopic(baseValue=window.KAFKA_TOPIC, variableName="KAFKA_TOPIC")
            self.kafkaSendLoopRate = None
            self.kafkaSendLoopRateLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.kafkaSendLoopRate, Labelinstance=self.kafkaSendLoopRateLabel,
                                  baseValue=window.SEND_LOOP_RATE, variableName="SEND_LOOP_RATE")
        elif name == "UDP":
            self.AddIp(baseValue=window.UDP_IP, variableName="UDP_IP")
            self.AddPort(baseValue=window.UDP_PORT, variableName="UDP_PORT")
            self.udpSendLoopRate = None
            self.udpSendLoopRateLabel = None
            self.AddDoubleSpinBox(SpinBoxinstance=self.udpSendLoopRate, Labelinstance=self.udpSendLoopRateLabel,
                                  baseValue=window.SEND_LOOP_RATE, variableName="SEND_LOOP_RATE")
        # elif name == "Start":
        #     self.Device = DeviceSelector(window=window, name="Camera")
        #     self.layout.addWidget(self.Device)

        # Create a QSpacerItem to "press" the widgets to the top
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        # add the spacer to the layout
        self.layout.addItem(spacer)
        # Set the layout
        central_widget.setLayout(self.layout)

        # Set the central widget
        self.setCentralWidget(central_widget)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    
    def closeEvent(self, event):
        """This method is called when the window is closed. It is used to save the selected camera and microphone.
        
        Args:
            event (QCloseEvent): The close event
        """
        # if self.name == "Start":
        #     self.window.CAM_ID = self.Device.exp_selected_camera()
        #     self.window.MIC_ID = self.Device.exp_selected_microphone()
        #     changeValues(cam_id=self.window.CAM_ID, mic_id=self.window.MIC_ID)
        #     event.accept()
        if self.name == "Camera":
            self.window.CAM_ID = self.Device.exp_selected_camera()
            changeValues(cam_id=self.window.CAM_ID)
            event.accept()
        elif self.name == "Microphone":
            self.window.MIC_ID = self.Device.exp_selected_microphone()
            changeValues(mic_id=self.window.MIC_ID)
            event.accept()
    
    def on_double_value_changed(self, value, variableName=""):
        """This method will be called whenever the value of the spinBox is changed.
        
        Args:
            value (float): The new value of the spin box
            varibaleName (str): The name of the corresponding value
        """
        value = round(value, 1)
        if variableName == "CAMERA_LOOP_RATE":
            self.window.CAMERA_LOOP_RATE = value
            changeValues(camera_loop_rate=value)
        elif variableName == "SENTIMENT_LOOP_RATE":
            self.window.SENTIMENT_LOOP_RATE = value
            changeValues(sentiment_loop_rate=value)
        elif variableName == "VAD_LOOP_RATE":
            self.window.VAD_LOOP_RATE = value
            changeValues(vad_loop_rate=value)
        elif variableName == "VAD_THRESHOLD":
            self.window.VAD_THRESHOLD = value
            changeValues(vad_threshold=value)
        elif variableName == "SER_LOOP_RATE":
            self.window.SER_LOOP_RATE = value
            changeValues(ser_loop_rate=value)
        elif variableName == "POSE_LOOP_RAT":
            self.window.POSE_LOOP_RATE = value
            changeValues(pose_loop_rate=value)
        elif variableName == "FACE_MESH_RATE":
            self.window.FACE_MESH_RATE = value
            changeValues(face_mesh_rate=value)
        elif variableName == "ER_LOOP_RATE":
            self.window.ER_LOOP_RATE = value
            changeValues(er_loop_rate=value)
        elif variableName == "STT_LOOP_RATE":
            self.window.STT_LOOP_RATE = value
            changeValues(stt_loop_rate=value)
        elif variableName == "STT_WINDOW_SIZE":
            self.window.STT_WINDOW_SIZE = value
            changeValues(stt_window_size=value)
        elif variableName == "FACE_PADDING":
            self.window.FACE_PADDING = value
            changeValues(face_padding=value)
        elif variableName == "MIC_CHUNKS":
            self.window.MIC_CHUNKS = value
            changeValues(mic_chunks=value)
        elif variableName == "SEND_LOOP_RATE":
            self.window.SEND_LOOP_RATE = value
            changeValues(send_loop_rate=value)
        elif variableName == "FUSION_LOOP_RATE":
            self.window.FUSION_LOOP_RATE = value
            changeValues(fusion_loop_rate=value)
        elif variableName == "FUSION_SPEED":
            self.window.FUSION_SPEED = value
            changeValues(fusion_speed=value)
        elif variableName == "FUSION_VOICE_SPEED":
            self.window.FUSION_VOICE_SPEED = value
            changeValues(fusion_voice_speed=value)
        elif variableName == "SER_VALENCE_OFFSET":
            self.window.SER_VALENCE_OFFSET = value
            changeValues(ser_valence_offset=value)
        elif variableName == "SER_AROUSAL_OFFSET":
            self.window.SER_AROUSAL_OFFSET = value
            changeValues(ser_arousal_offset=value)
        elif variableName == "SER_DOMINANCE_OFFSET":
            self.window.SER_DOMINANCE_OFFSET = value
            changeValues(ser_dominance_offset=value)
        elif variableName == "FUSION_VOICE_VALENCE_WEIGHT":
            self.window.FUSION_VOICE_VALENCE_WEIGHT = value
            changeValues(fusion_voice_valence_weight=value)
        elif variableName == "FUSION_VOICE_VALENCE_BOOST":
            self.window.FUSION_VOICE_VALENCE_BOOST = value
            changeValues(fusion_voice_valence_boost=value)
        elif variableName == "FUSION_VOICE_AROUSAL_WEIGHT":
            self.window.FUSION_VOICE_AROUSAL_WEIGHT = value
            changeValues(fusion_voice_arousal_weight=value)
        elif variableName == "FUSION_VOICE_AROUSAL_BOOST":
            self.window.FUSION_VOICE_AROUSAL_BOOST = value
            changeValues(fusion_voice_arousal_boost=value)
        elif variableName == "FUSION_VOICE_DOMINANCE_WEIGHT":
            self.window.FUSION_VOICE_DOMINANCE_WEIGHT = value
            changeValues(fusion_voice_dominance_weight=value)
        elif variableName == "FUSION_VOICE_DOMINANCE_BOOST":
            self.window.FUSION_VOICE_DOMINANCE_BOOST = value
            changeValues(fusion_voice_dominance_boost=value)
        elif variableName == "FUSION_FACE_SPEED":
            self.window.FUSION_FACE_SPEED = value
            changeValues(fusion_face_speed=value)
        elif variableName == "FUSION_FACE_VALENCE_WEIGHT":
            self.window.FUSION_FACE_VALENCE_WEIGHT = value
            changeValues(fusion_face_valence_weight=value)
        elif variableName == "FUSION_FACE_VALENCE_BOOST":
            self.window.FUSION_FACE_VALENCE_BOOST = value
            changeValues(fusion_face_valence_boost=value)
        elif variableName == "FUSION_FACE_AROUSAL_WEIGHT":
            self.window.FUSION_FACE_AROUSAL_WEIGHT = value
            changeValues(fusion_face_arousal_weight=value)
        elif variableName == "FUSION_FACE_AROUSAL_BOOST":
            self.window.FUSION_FACE_AROUSAL_BOOST = value
            changeValues(fusion_face_arousal_boost=value)
        elif variableName == "FUSION_FACE_DOMINANCE_WEIGHT":
            self.window.FUSION_FACE_DOMINANCE_WEIGHT = value
            changeValues(fusion_face_dominance_weight=value)
        elif variableName == "FUSION_FACE_DOMINANCE_BOOST":
            self.window.FUSION_FACE_DOMINANCE_BOOST = value
            changeValues(fusion_face_dominance_boost=value)
        elif variableName == "FUSION_SENTIMENT_SPEED":
            self.window.FUSION_SENTIMENT_SPEED = value
            changeValues(fusion_sentiment_speed=value)
        elif variableName == "FUSION_SENTIMENT_WEIGHT":
            self.window.FUSION_SENTIMENT_WEIGHT = value
            changeValues(fusion_sentiment_weight=value)
        elif variableName == "FUSION_SENTIMENT_BOOST":
            self.window.FUSION_SENTIMENT_BOOST = value
            changeValues(fusion_sentiment_boost=value)
        elif variableName == "FUSION_POSE_SPEED":
            self.window.FUSION_POSE_SPEED = value
            changeValues(fusion_pose_speed=value)
        elif variableName == "FUSION_POSE_DOMINANCE_WEIGHT":
            self.window.FUSION_POSE_DOMINANCE_WEIGHT = value
            changeValues(fusion_pose_dominance_weight=value)
        elif variableName == "FUSION_POSE_DOMINANCE_BOOST":
            self.window.FUSION_POSE_DOMINANCE_BOOST = value
            changeValues(fusion_pose_dominance_boost=value)
        print(f"{variableName} has been changed to {value}")

    def AddDoubleSpinBox(self, SpinBoxinstance, Labelinstance, baseValue=0.0, variableName=""):
        """ Add a double spin box to the layout with the given name and base value. The method also connects the valueChanged signal to the on_double_value_changed method.
        
        Args:
            SpinBoxinstance (QDoubleSpinBox): The instance of the spin box
            Labelinstance (QLabel): The instance of the label
            baseValue (float): The base value of the spin box
            variableName (str): The name of the variable that will be changed
        """
        Labelinstance = QLabel(f"{variableName}:")
        Labelinstance.setFixedSize(300, 20)
        SpinBoxinstance = QDoubleSpinBox()
        SpinBoxinstance.setFixedSize(300, 20)
        self.layout.addWidget(Labelinstance)
        self.layout.addWidget(SpinBoxinstance)
        SpinBoxinstance.setMaximum(100000.0)
        SpinBoxinstance.setMinimum(-100000.0)
        SpinBoxinstance.setValue(baseValue)
        SpinBoxinstance.setSingleStep(0.1)
        SpinBoxinstance.valueChanged.connect(lambda value: self.on_double_value_changed(value=value, variableName=variableName))
        
    def on_int_value_changed(self, value, variableName=""):
        if variableName == "SAMPLE_RATE":
            self.window.SAMPLE_RATE = value
            changeValues(sample_rate=value)
        elif variableName == "MIC_CHUNKS":
            self.window.MIC_CHUNKS = value
            changeValues(mic_chunks=value)
        print(f"{variableName} has been changed to {value}")

    def AddIntSpinBox(self, baseValue=0, variableName=""):
        self.spinBoxLabel = QLabel(f"{variableName}")
        self.spinBoxLabel.setFixedSize(300, 20)
        self.spinBox = QSpinBox()
        self.spinBox.setFixedSize(300, 20)
        self.layout.addWidget(self.spinBoxLabel)
        self.layout.addWidget(self.spinBox)
        self.spinBox.setMaximum(48000)
        self.spinBox.setValue(baseValue)
        self.spinBox.setSingleStep(1000)
        self.spinBox.valueChanged.connect(lambda value: self.on_int_value_changed(value=value, variableName=variableName))

    def AddIp(self, baseValue='0.0.0.0', variableName=""):
        """ Add a QLineEdit to the layout with the given name and base value. The method also connects the textChanged signal to the on_text_changed_IP method.
        
        Args:
            baseValue (str): The base value of the QLineEdit
            variableName (str): The name of the QLineEdit
        """
        self.ipLabel = QLabel(f"{variableName}:")
        self.ipLabel.setFixedSize(300, 20)
        self.ipLineEdit = QLineEdit()
        self.ipLineEdit.setFixedSize(300, 20)
        self.layout.addWidget(self.ipLabel)
        self.layout.addWidget(self.ipLineEdit)
        self.ipLineEdit.setText(baseValue)
        self.ipLineEdit.textChanged.connect(lambda  text: self.on_text_changed_IP(text=text, variableName=variableName))

    def on_text_changed_IP(self, text, variableName=""):
        """Called, when text within QLineEdit is changed
        
        Args:
            text (str): The new text of the QLineEdit
            variableName (str): The name of the QLineEdit
        """
        if variableName == "UDP_IP":
            self.window.UDP_IP = text
            changeValues(udpIP=text)
        if variableName == "KAFKA_IP":
            self.window.KAFKA_IP = text
            changeValues(kafkaIP=text)
        print(f"{variableName} has been changed to {text}")

    def AddPort(self, baseValue=3000, variableName=""):
        """ Add a QLineEdit to the layout with the given name and base value. The method also connects the textChanged signal to the on_text_changed_port method.
        
        Args:
            baseValue (int): The base value of the QLineEdit
            variableName (str): The name of the QLineEdit
        """
        self.portLabel = QLabel(f"{variableName}:")
        self.portLabel.setFixedSize(300, 20)
        self.portLineEdit = QLineEdit()
        self.portLineEdit.setFixedSize(300, 20)
        self.layout.addWidget(self.portLabel)
        self.layout.addWidget(self.portLineEdit)
        self.portLineEdit.setText(str(baseValue))
        self.portLineEdit.textChanged.connect(lambda value: self.on_text_changed_port(value=value, variableName=variableName))

    def on_text_changed_port(self, value, variableName=""):
        """Called, when text within QLineEdit is changed.
        
        Args:
            value (str): The new text of the QLineEdit
            variableName (str): The name of the QLineEdit
        """
        if variableName == "UDP_PORT":
            self.window.UDP_PORT = int(value)
            changeValues(udpPort=int(value))
        if variableName == "KAFKA_PORT":
            self.window.KAFKA_PORT = int(value)
            changeValues(kafkaPort=int(value))
        print(f"{variableName} has been changed to {value}")

    def AddTopic(self, baseValue='PAD', variableName=""):
        """ Add a QLineEdit to the layout with the given name and base value. The method also connects the textChanged signal to the on_text_changed_topic method.
        
        Args:
            baseValue (str): The base value of the QLineEdit
            variableName (str): The name of the QLineEdit
        """
        self.topicLabel = QLabel(f"{variableName}:")
        self.topicLabel.setFixedSize(300, 20)
        self.topicLineEdit = QLineEdit()
        self.topicLineEdit.setFixedSize(300, 20)
        self.layout.addWidget(self.topicLabel)
        self.layout.addWidget(self.topicLineEdit)
        self.topicLineEdit.setText(baseValue)
        self.topicLineEdit.textChanged.connect(lambda value: self.on_text_changed_topic(value=value, variableName=variableName))

    def on_text_changed_topic(self, value, variableName=""):
        """Called, when text within QLineEdit is changed.
        
        Args:
            value (str): The new text of the QLineEdit
            variableName (str): The name of the QLineEdit
        """
        if variableName == "KAFKA_TOPIC":
            self.window.KAFKA_TOPIC = value
            changeValues(kafkaTopic=value)
        print(f"{variableName} has been changed to {value}")
            
        