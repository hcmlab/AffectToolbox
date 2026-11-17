from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QVBoxLayout, QScrollArea, QSpacerItem
from PySide6.QtCore import Qt
from GUI.rightClickWindow import RightClickWindow
from GUI.custom_button import CustomButton
from GUI.floatButton import FloatButton
from GUI.imageButton import ImageStreamContainer
import modules.QueueSystem as qs
from GUI.audioButton import AudioStreamContainer
from GUI.transcriptButton import TranscriptContainer
from GUI.statusButton import StatusButton
from GUI.connectionlines import is_valid_widget
from GUI.styles import active_style, inactive_style, button_stylesheet

class Buttons (QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.pipeline_running = False
        self.previews_enabled = True
        self.setWindowTitle("AffectToolbox")
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Load styles from external stylesheets
        self.button_stylesheet = button_stylesheet
        self.active_style = active_style
        self.inactive_style = inactive_style

        # Apply default widget and button styling
        self.setStyleSheet("""
    QWidget {
        background-color: transparent;
    }
    QPushButton {
        background-color: lightgrey;
        border: 1px darkgrey;
        padding: 6px;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: lightblue;
    }

    QPushButton#SENSORS, 
    QPushButton#DATASTREAMS, 
    QPushButton#ACTIVITYCHECK, 
    QPushButton#ANALYSIS, 
    QPushButton#UNIMODALRESULTS, 
    QPushButton#FUSION_2, 
    QPushButton#MULTIMODALRESULTS {
        background-color: #1E90FF;
    }

    QPushButton#SENSORS:hover, 
    QPushButton#DATASTREAMS:hover, 
    QPushButton#ACTIVITYCHECK:hover, 
    QPushButton#ANALYSIS:hover, 
    QPushButton#UNIMODALRESULTS:hover, 
    QPushButton#FUSION_2:hover, 
    QPushButton#MULTIMODALRESULTS:hover {
        background-color: lightblue;
    }
""")
        self.windows = {}

        # Initialize sensor-related buttons for microphone input
        self.Micro = CustomButton("Micro", self, main_window=self)
        self.Micro.clicked.connect(lambda: self.toggle_button(self.Micro))
        self.Micro.base_text = "Micro"

        self.Audio = AudioStreamContainer("Audio", main_window=self.main_window)
        self.Audio.button.clicked.connect(lambda: self.toggle_button(self.Audio.button))
        self.Audio.setVisible(False)
        self.Audio.base_text = "Audio"

        self.Transcript = TranscriptContainer("Transcript", qs.TRANSCRIPT_SPEECH, main_window=self)
        self.Transcript.button.clicked.connect(lambda: self.toggle_button(self.Transcript.button))
        self.Transcript.setVisible(False)
        self.Transcript.base_text = "Transcript"

        self.VoiceActivity = StatusButton("VoiceActivity", self, main_window=self)
        self.VoiceActivity.clicked.connect(lambda: self.toggle_button(self.VoiceActivity))
        self.VoiceActivity.setVisible(False)
        self.VoiceActivity.base_text = "VoiceActivity"

        self.PARALINGUISTIC = CustomButton("PARALINGUISTIC", self, main_window=self)
        self.PARALINGUISTIC.clicked.connect(lambda: self.toggle_button(self.PARALINGUISTIC))
        self.PARALINGUISTIC.setVisible(False)
        self.PARALINGUISTIC.base_text = "PARALINGUISTIC"

        self.SENTIMENT = CustomButton("SENTIMENT", self, main_window=self)
        self.SENTIMENT.clicked.connect(lambda: self.toggle_button(self.SENTIMENT))
        self.SENTIMENT.setVisible(False)
        self.SENTIMENT.base_text = "SENTIMENT"

        self.Pleasure_1 = FloatButton("Pleasure", "Pleasure_1", main_window=self.main_window)
        self.Pleasure_1.clicked.connect(lambda: self.toggle_button(self.Pleasure_1))
        self.Pleasure_1.setVisible(False)

        self.Arousal_1 = FloatButton("Arousal", "Arousal_1", main_window=self.main_window)
        self.Arousal_1.clicked.connect(lambda: self.toggle_button(self.Arousal_1))
        self.Arousal_1.setVisible(False)

        self.Dominance_1 = FloatButton("Dominance", "Dominance_1", main_window=self.main_window)
        self.Dominance_1.clicked.connect(lambda: self.toggle_button(self.Dominance_1))
        self.Dominance_1.setVisible(False)

        self.Pleasure_2 = FloatButton("Pleasure", "Pleasure_2", main_window=self.main_window)
        self.Pleasure_2.clicked.connect(lambda: self.toggle_button(self.Pleasure_2))
        self.Pleasure_2.setVisible(False)

        #Buttons für Sensor: Kamera
        self.Camera = CustomButton("Camera", self, main_window=self)
        self.Camera.clicked.connect(lambda: self.toggle_button(self.Camera))
        self.Camera.base_text = "Camera"

        self.Video = ImageStreamContainer("Video", qs.IMAGE_FACE_RAW, main_window=self.main_window)
        self.Video.stream.setStyleSheet("border: 2px solid green; border-radius: 4px;")
        self.Video.button.clicked.connect(lambda: self.toggle_button(self.Video.button))
        self.Video.setVisible(False)
        self.Video.base_text = "Video"

        face_mesh_button = StatusButton("FaceMesh", parent=self, main_window=self.main_window)
        self.FaceMesh = ImageStreamContainer(
            "FaceMesh", qs.IMAGE_FACE_MESH,
            main_window=self.main_window, button=face_mesh_button, rate_key="FACE_MESH_RATE"
        )
        self.FaceMesh.stream.setStyleSheet("border: 2px solid green; border-radius: 4px;")
        self.FaceMesh.button.clicked.connect(lambda: self.toggle_button(self.FaceMesh.button))
        self.FaceMesh.setVisible(False)
        self.FaceMesh.base_text = "FaceMesh"

        self.Skeleton = ImageStreamContainer("Skeleton", qs.IMAGE_BODY_SKEL, main_window=self.main_window)
        self.Skeleton.stream.setStyleSheet("border: 2px solid green; border-radius: 4px;")
        self.Skeleton.button.clicked.connect(lambda: self.toggle_button(self.Skeleton.button))
        self.Skeleton.setVisible(False)
        self.Skeleton.base_text = "Skeleton"

        face_tracking_button = StatusButton("FaceTracking", parent=self, main_window=self.main_window)
        self.FaceTracking = ImageStreamContainer(
            "FaceTracking", qs.IMAGE_FACE_PREPROCESSED,
            main_window=self.main_window, button=face_tracking_button
        )
        self.FaceTracking.stream.setStyleSheet("border: 2px solid green; border-radius: 4px;")
        self.FaceTracking.button.clicked.connect(lambda: self.toggle_button(self.FaceTracking.button))
        self.FaceTracking.setVisible(False)
        self.FaceTracking.base_text = "FaceTracking"

        body_tracking_button = StatusButton("BodyTracking", parent=self, main_window=self.main_window)
        self.BodyTracking = ImageStreamContainer(
            "BodyTracking", qs.IMAGE_BODY_SKEL_BLACK,
            main_window=self.main_window, button=body_tracking_button
        )
        self.BodyTracking.stream.setStyleSheet("border: 2px solid green; border-radius: 4px;")
        self.BodyTracking.button.clicked.connect(lambda: self.toggle_button(self.BodyTracking.button))
        self.BodyTracking.setVisible(False)
        self.BodyTracking.base_text = "BodyTracking"

        self.FACIALEXPRESSION = CustomButton("FACIALEXPRESSION", self, main_window=self)
        self.FACIALEXPRESSION.clicked.connect(lambda: self.toggle_button(self.FACIALEXPRESSION))
        self.FACIALEXPRESSION.setVisible(False)
        self.FACIALEXPRESSION.base_text = "FACIALEXPRESSION"

        self.POSE = CustomButton("POSE", self, main_window=self)
        self.POSE.clicked.connect(lambda: self.toggle_button(self.POSE))
        self.POSE.setVisible(False)
        self.POSE.base_text = "POSE"

        self.Pleasure_3 = FloatButton("Pleasure", "Pleasure_3", main_window=self.main_window)
        self.Pleasure_3.clicked.connect(lambda: self.toggle_button(self.Pleasure_3 ))
        self.Pleasure_3.setVisible(False)

        self.Arousal_2 = FloatButton("Arousal", "Arousal_2", main_window=self.main_window)
        self.Arousal_2.clicked.connect(lambda: self.toggle_button(self.Arousal_2))
        self.Arousal_2.setVisible(False)

        self.Dominance_2 = FloatButton("Dominance", "Dominance_2", main_window=self.main_window)
        self.Dominance_2.clicked.connect(lambda: self.toggle_button(self.Dominance_2))
        self.Dominance_2.setVisible(False)

        self.Dominance_3 = FloatButton("Dominance", "Dominance_3", main_window=self.main_window)
        self.Dominance_3.clicked.connect(lambda: self.toggle_button(self.Dominance_3))
        self.Dominance_3.setVisible(False)

        #Buttons FUSION
        self.FUSION_1 = CustomButton("FUSION", self, main_window=self)
        self.FUSION_1.clicked.connect(lambda: self.toggle_button(self.FUSION_1))
        self.FUSION_1.setVisible(False)
        self.FUSION_1.base_text = "FUSION"
        self.Pleasure_4 = FloatButton("Pleasure", "Pleasure_4", active_stylesheet=self.main_window.green_stylesheet, main_window=self.main_window)
        self.Pleasure_4.clicked.connect(lambda: self.toggle_button(self.Pleasure_4))
        self.Pleasure_4.setVisible(False)
        self.Arousal_3 = FloatButton("Arousal", "Arousal_3", active_stylesheet=self.main_window.green_stylesheet, main_window=self.main_window)
        self.Arousal_3.clicked.connect(lambda: self.toggle_button(self.Arousal_3))
        self.Arousal_3.setVisible(False)
        self.Dominance_4 = FloatButton("Dominance", "Dominance_4", active_stylesheet=self.main_window.green_stylesheet, main_window=self.main_window)
        self.Dominance_4.clicked.connect(lambda: self.toggle_button(self.Dominance_4))
        self.Dominance_4.setVisible(False)

        #Header Buttons
        self.SENSORS = QPushButton("SENSORS")
        self.SENSORS.setObjectName("SENSORS")
        self.DATASTREAMS = QPushButton("DATA STREAMS")
        self.DATASTREAMS.setObjectName("DATASTREAMS")
        self.ACTIVITYCHECK = QPushButton("ACTIVITY CHECK")
        self.ACTIVITYCHECK.setObjectName("ACTIVITYCHECK")
        self.ANALYSIS = QPushButton("ANALYSIS")
        self.ANALYSIS.setObjectName("ANALYSIS")
        self.UNIMODALRESULTS = QPushButton("UNIMODAL RESULTS")
        self.UNIMODALRESULTS.setObjectName("UNIMODALRESULTS")
        self.FUSION_2 = QPushButton("FUSION")
        self.FUSION_2.setObjectName("FUSION_2")
        self.MULTIMODALRESULTS = QPushButton("MULTIMODAL RESULTS")
        self.MULTIMODALRESULTS.setObjectName("MULTIMODALRESULTS")

        #Layout
        grid_layout = QGridLayout()

        # Add Buttons to the layout
        #Header Buttons
        grid_layout.addWidget(self.SENSORS, 0, 0)
        grid_layout.addWidget(self.DATASTREAMS, 0, 1)
        grid_layout.addWidget(self.ACTIVITYCHECK, 0, 2)
        grid_layout.addWidget(self.ANALYSIS, 0, 3)
        grid_layout.addWidget(self.UNIMODALRESULTS, 0, 4)
        grid_layout.addWidget(self.FUSION_2, 0, 5)
        grid_layout.addWidget(self.MULTIMODALRESULTS, 0, 6)


        #Micro Buttons
        grid_layout.addWidget(self.Micro, 3, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Audio, 3, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.VoiceActivity, 2, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.PARALINGUISTIC, 3, 3, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Pleasure_1, 2, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Arousal_1, 3, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Dominance_1, 4, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Transcript, 7, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.SENTIMENT, 7, 3, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Pleasure_2, 7, 4, alignment=Qt.AlignmentFlag.AlignHCenter)

        #Camera Buttons
        grid_layout.addWidget(self.Camera, 12, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.FaceMesh, 11, 3, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Video, 12, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.FaceTracking, 11, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.FACIALEXPRESSION, 12, 3, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Pleasure_3, 11, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Arousal_2, 12, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Dominance_2, 13, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Skeleton, 16, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.BodyTracking, 15, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.POSE, 16, 3, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Dominance_3, 16, 4, alignment=Qt.AlignmentFlag.AlignHCenter)

        #Fusion Buttons
        grid_layout.addWidget(self.FUSION_1, 9, 5, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Pleasure_4, 8, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Arousal_3, 9, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.Dominance_4, 10, 6, alignment=Qt.AlignmentFlag.AlignHCenter)

        #List with dependencies of the buttons when activated
        self.button_dependencies = {
            self.Micro: [self.Audio.button],
            self.Audio.button: [self.Transcript.button, self.VoiceActivity, self.PARALINGUISTIC],
            self.PARALINGUISTIC: [self.Pleasure_1, self.Arousal_1, self.Dominance_1],
            self.Transcript.button: [self.SENTIMENT],
            self.SENTIMENT: [self.Pleasure_2],
            self.Camera: [self.Video.button],
            self.Video.button: [self.Skeleton.button, self.FaceTracking.button, self.FACIALEXPRESSION],
            self.FaceTracking.button: [self.FaceMesh.button],
            self.FACIALEXPRESSION: [self.Pleasure_3, self.Arousal_2, self.Dominance_2],
            self.Skeleton.button: [self.BodyTracking.button, self.POSE],
            self.POSE: [self.Dominance_3]
        }

        #List with visible-dependencies of the buttons when activated
        self.button_dependencies_visible = {
            self.Micro: [self.Audio],
            self.Audio.button: [self.Transcript, self.VoiceActivity, self.PARALINGUISTIC],
            self.PARALINGUISTIC: [self.Pleasure_1, self.Arousal_1, self.Dominance_1],
            self.Transcript.button: [self.SENTIMENT],
            self.SENTIMENT: [self.Pleasure_2],
            self.Camera: [self.Video],
            self.Video.button: [self.Skeleton, self.FaceTracking, self.FACIALEXPRESSION],
            self.FaceTracking.button: [self.FaceMesh],
            self.FACIALEXPRESSION: [self.Pleasure_3, self.Arousal_2, self.Dominance_2],
            self.Skeleton.button: [self.BodyTracking, self.POSE],
            self.POSE: [self.Dominance_3],
            self.Pleasure_1: [self.FUSION_1, self.Pleasure_4, self.Arousal_3, self.Dominance_4],
            self.Arousal_1: [self.FUSION_1, self.Pleasure_4, self.Arousal_3, self.Dominance_4],
            self.Dominance_1: [self.FUSION_1, self.Pleasure_4, self.Arousal_3, self.Dominance_4],
            self.Pleasure_2: [self.FUSION_1, self.Pleasure_4, self.Arousal_3, self.Dominance_4],
            self.Pleasure_3: [self.FUSION_1, self.Pleasure_4, self.Arousal_3, self.Dominance_4],
            self.Arousal_2: [self.FUSION_1, self.Pleasure_4, self.Arousal_3, self.Dominance_4],
            self.Dominance_2: [self.FUSION_1, self.Pleasure_4, self.Arousal_3, self.Dominance_4],
            self.Dominance_3: [self.FUSION_1, self.Pleasure_4, self.Arousal_3, self.Dominance_4],
            self.FUSION_1: [self.Pleasure_4, self.Arousal_3, self.Dominance_4],
        }

        #List with dependencies of the buttons when deactivated
        self.button_dependencies_deactivate = {
            self.Micro: [self.Audio, self. Transcript, self.VoiceActivity, self.PARALINGUISTIC, self.SENTIMENT, self.Pleasure_1, self.Arousal_1, self.Dominance_1, self.Pleasure_2],
            self.Audio.button: [self.Transcript, self.SENTIMENT, self.Pleasure_2, self.VoiceActivity, self.PARALINGUISTIC, self.Pleasure_1, self.Arousal_1, self.Dominance_1],
            self.PARALINGUISTIC: [self.Pleasure_1, self.Arousal_1, self.Dominance_1],
            self.Transcript.button: [self.SENTIMENT, self.Pleasure_2],
            self.SENTIMENT: [self.Pleasure_2],
            self.Camera: [self.Video, self.Skeleton, self.FaceMesh, self.FaceTracking, self.FACIALEXPRESSION, self.BodyTracking, self.POSE, self.Pleasure_3, self.Arousal_2, self.Dominance_2, self.Dominance_3],
            self.Video.button: [self.Skeleton, self.FaceMesh, self.BodyTracking, self.POSE, self.Dominance_3, self.FaceTracking, self.FACIALEXPRESSION, self.Pleasure_3, self.Arousal_2, self.Dominance_2],
            self.FaceTracking.button: [self.FaceMesh],
            self.FACIALEXPRESSION: [self.Pleasure_3, self.Arousal_2, self.Dominance_2],
            self.Skeleton.button: [self.BodyTracking, self.POSE, self.Dominance_3],
            self.POSE: [self.Dominance_3],
            self.FUSION_1: [self.Pleasure_4, self.Arousal_3, self.Dominance_4]
        }

        #List with the headings and their corresponding buttons
        self.header_to_buttons = {
            self.SENSORS: [self.Micro, self.Camera],
            self.DATASTREAMS: [self.Audio.button, self.Transcript.button, self.Video.button, self.Skeleton.button],
            self.ACTIVITYCHECK: [self.VoiceActivity, self.FaceTracking.button, self.BodyTracking.button],
            self.ANALYSIS: [self.PARALINGUISTIC, self.SENTIMENT, self.FaceMesh.button, self.FACIALEXPRESSION, self.POSE],
            self.UNIMODALRESULTS: [self.Pleasure_1, self.Arousal_1, self.Dominance_1, self.Pleasure_2, self.Pleasure_3,
                                   self.Arousal_2, self.Dominance_2, self.Dominance_3],
            self.FUSION_2: [self.FUSION_1],
            self.MULTIMODALRESULTS: [self.Pleasure_4, self.Arousal_3, self.Dominance_4],
        }

        #List with the headings and the buttons that should be visible when clicking
        self.header_clicked = {
            self.SENSORS: [self.Micro, self.Camera],
            self.DATASTREAMS: [self.Audio, self.Transcript, self.Video, self.Skeleton],
            self.ACTIVITYCHECK: [self.VoiceActivity, self.FaceTracking, self.BodyTracking],
            self.ANALYSIS: [self.PARALINGUISTIC, self.SENTIMENT, self.FaceMesh, self.FACIALEXPRESSION, self.POSE],
            self.UNIMODALRESULTS: [self.Pleasure_1, self.Arousal_1, self.Dominance_1, self.Pleasure_2, self.Pleasure_3,
                                   self.Arousal_2, self.Dominance_2, self.Dominance_3],
            self.FUSION_2: [self.FUSION_1],
            self.MULTIMODALRESULTS: [self.Pleasure_4, self.Arousal_3, self.Dominance_4],
        }

        #Dictionary that assigns the buttons to their individual parameters
        self.button_to_parameter_mapping = {
            self.FaceMesh.button: "enable_face_mesh_loop",
            self.Pleasure_1: "fusion_use_para_v",
            self.Arousal_1: "fusion_use_para_a",
            self.Dominance_1: "fusion_use_para_d",
            self.Pleasure_2: "fusion_use_sentiment_v",
            self.Pleasure_3: "fusion_use_face_v",
            self.Arousal_2: "fusion_use_face_a",
            self.Dominance_2: "fusion_use_face_d",
            self.Dominance_3: "fusion_use_pose_d",
        }
        #List of buttons that can display a float value
        self.float_buttons = [
            self.Pleasure_1, self.Arousal_1, self.Dominance_1,
            self.Pleasure_2, self.Pleasure_3, self.Arousal_2, self.Dominance_2,
            self.Dominance_3, self.Pleasure_4, self.Arousal_3, self.Dominance_4
        ]

        #Stretch grid layout columns for responsive design
        for col in range(7):
            grid_layout.setColumnStretch(col, 1)

        content_widget = QWidget()
        content_widget.setLayout(grid_layout)

        #Add layout to a scrollable widget
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(content_widget)

        #Add vertical spacers to structure layout better
        spacer1 = QSpacerItem(0, 20)  # 20 Pixel hoher Abstand
        grid_layout.addItem(spacer1, 1, 0, 1, -1)  # Zwischen erster und zweiter Zeile
        spacer2 = QSpacerItem(0, 40)
        grid_layout.addItem(spacer2, 8, 7, 1, -1)
        spacer3 = QSpacerItem(0, 40)
        grid_layout.addItem(spacer3, 11, 10, 1, -1)

        # Final layout assembly
        self.adjust_button_sizes()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

        #Auto clicked method to make Buttons visible
        self.create_auto_click_methods()

        #Used to make Buttons visible when Header Button is clicked
        def make_cascading_show_handler(target_header):
            def handler(_=None):
                for header in self.header_clicked:
                    for b in self.header_clicked[header]:
                        b.setVisible(True)
                    if header == target_header:
                        break

            return handler

        for header in self.header_clicked:
            header.clicked.connect(make_cascading_show_handler(header))

    def adjust_button_sizes(self):
        #  Dynamically adjust the width of each button depending on its header

        for header, buttons in self.header_to_buttons.items():
            header_width = header.width()
            target_width = int(header_width * 0.6)
            streams_width = int(header_width * 0.85)

            for btn in buttons:
                mini_width = btn.sizeHint().width()
                if btn in self.header_to_buttons[self.DATASTREAMS]:
                    mini_width = streams_width
                # Take the larger of mini_width or target_width
                min_width = max(mini_width, target_width)
                btn.setMinimumWidth(min_width)
                btn.setMaximumWidth(min_width)


    def resizeEvent(self, event):
        #Overridden resize event to update button sizes
        super().resizeEvent(event)
        self.adjust_button_sizes()

    def create_auto_click_methods(self):
        for button, dependent_buttons in self.button_dependencies_visible.items():
            button.clicked.connect(self.make_dependent_buttons_visible_factory(button, dependent_buttons))

    def make_dependent_buttons_visible_factory(self, source_button, targets):
        def handler():
            # Only make it visible when the button has just become active
            if self.is_selected(source_button):
                for t in targets:
                    t.setVisible(True)

        return handler

    #Used to sync Buttons when config ist loaded
    def propagate_visibility(self, source_button):
        targets = self.button_dependencies_visible.get(source_button, [])
        for target in targets:
            if hasattr(target, "setVisible"):
                target.setVisible(True)
            elif hasattr(target, "parent") and isinstance(target.parent(), QWidget):
                target.parent().setVisible(True)

    def _parameter_key(self, button):
        if button in self.button_to_parameter_mapping:
            return self.button_to_parameter_mapping[button]
        key = f"enable_{button.base_text.lower()}"
        return key if key in RightClickWindow.PARAMETERS else None

    def is_selected(self, button):
        key = self._parameter_key(button)
        if key is not None:
            return bool(RightClickWindow.PARAMETERS[key])
        return bool(button.property("selected"))

    def set_selected(self, button, selected):
        selected = bool(selected)
        key = self._parameter_key(button)
        if key is not None:
            RightClickWindow.PARAMETERS[key] = selected
        button.setProperty("selected", selected)
        button.setStyleSheet(self.active_style if selected else self.inactive_style)
        if button is self.FaceMesh.button:
            RightClickWindow.PARAMETERS["show_face_mesh"] = selected
        if not selected:
            if isinstance(button, StatusButton):
                button.set_status("grey")
            if isinstance(button, FloatButton):
                button.setText(button.base_text)

        container = button.parentWidget()
        if hasattr(container, "stream"):
            if selected and self.previews_enabled:
                container.stream.start_stream()
            elif selected:
                container.stream.pause_stream()
            else:
                container.stream.stop_stream()

    def set_pipeline_running(self, running):
        self.pipeline_running = running
        self.previews_enabled = running
        self.refresh_selections()

    def refresh_selections(self):
        for buttons in self.header_to_buttons.values():
            for button in buttons:
                self.set_selected(button, self.is_selected(button))

    def toggle_button(self, button):
        if not button.isEnabled():
            return
        self.previews_enabled = True
        selected = not self.is_selected(button)
        self.set_selected(button, selected)
        if selected:
            for dependent in self.button_dependencies.get(button, []):
                dependent.setVisible(True)
                if button is self.FUSION_1:
                    self.set_selected(dependent, True)
            self.activate_dependencies(button)
        else:
            for dependent in self.button_dependencies_deactivate.get(button, []):
                self.fully_deactivate_button(dependent)

        self.refresh_selections()
        if self.main_window and hasattr(self.main_window, "connection_overlay"):
            self.main_window.update_connections()

    def activate_dependencies(self, button):
        for parent_button, dependent_buttons in self.button_dependencies.items():
            if button in dependent_buttons:
                self.set_selected(parent_button, True)
                container = parent_button.parentWidget()
                if hasattr(container, "stream"):
                    container.setVisible(True)
                self.activate_dependencies(parent_button)

    def fully_deactivate_button(self, component):
        if hasattr(component, "button"):
            component.deactivate()
            button = component.button
        else:
            component.setVisible(False)
            button = component
        self.set_selected(button, False)

    def get_connections(self):
        #Returns all valid connection lines between buttons based on defined dependencies
        all_connections = {source: list(targets) for source, targets in self.button_dependencies.items()}

        extra_connections = {
        self.VoiceActivity: [self.PARALINGUISTIC],
        self.FaceTracking.button: [self.FACIALEXPRESSION],
        self.BodyTracking.button: [self.POSE],
        self.Pleasure_1: [self.FUSION_1],
        self.Pleasure_2: [self.FUSION_1],
        self.Pleasure_3: [self.FUSION_1],
        self.Arousal_1: [self.FUSION_1],
        self.Arousal_2: [self.FUSION_1],
        self.Dominance_1: [self.FUSION_1],
        self.Dominance_2: [self.FUSION_1],
        self.Dominance_3: [self.FUSION_1],
        self.FUSION_1:[self.Pleasure_4, self.Arousal_3, self.Dominance_4],
        }

        for source, extra_targets in extra_connections.items():
            if source in all_connections:
                all_connections[source].extend(extra_targets)
            else:
                all_connections[source] = extra_targets

        connections = {}

        for source, targets in all_connections.items():
            valid_targets = []
            if not is_valid_widget(source):
                continue
            for target in targets:
                if is_valid_widget(target):
                    valid_targets.append(target)

            if valid_targets:
                connections[source] = valid_targets

        return connections
