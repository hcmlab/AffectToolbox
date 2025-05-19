from PySide6.QtWidgets import QPushButton, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QFileDialog
from PySide6.QtCore import Qt, QTimer, QPoint, QRect, QEvent
from buttons import Buttons
from styles import active_style, inactive_style, button_stylesheet, green_stylesheet, red_stylesheet
from config_handler import load_config, save_config, deep_update
from pipeline_handler import create_pipeline
from custom_button import CustomButton
from connectionlines import ConnectionOverlay
from rightClickWindow import RightClickWindow
from connectionlines import is_valid_widget
from helpWindow import HelpWindow
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up window appearance and title
        self.setWindowTitle("AffectToolbox")
        self.setStyleSheet("background-color: black;")
        self.pipeline = None

        # Set up main layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Load styles as instance variables
        self.green_stylesheet = green_stylesheet
        self.red_stylesheet = red_stylesheet
        self.button_stylesheet = button_stylesheet
        self.active_style = active_style
        self.inactive_style = inactive_style

        # Button state flags
        self.udp_button_active = False
        self.kafka_button_active = False
        self.run_active = False
        self.fusion_button_active = False

        # Create horizontal top bar for control buttons
        top_widget = QWidget()
        top_widget.setStyleSheet("background-color: darkgrey;")
        top_button_layout = QHBoxLayout(top_widget)

        # Initialize control buttons
        self.run_button = QPushButton("Run")
        self.run_button.setStyleSheet(self.green_stylesheet)
        self.run_button.setFixedSize(80, 25)

        self.help_button = QPushButton("Help")
        self.help_button.setStyleSheet(self.button_stylesheet)
        self.help_button.setFixedSize(80, 25)

        self.udp_button = CustomButton("UDP", self, main_window=self)
        self.udp_button.setStyleSheet(self.button_stylesheet)
        self.udp_button.setFixedSize(80, 25)

        self.kafka_button = CustomButton("KAFKA", self, main_window=self)
        self.kafka_button.setStyleSheet(self.button_stylesheet)
        self.kafka_button.setFixedSize(80, 25)

        self.load_button = QPushButton("Load Config")
        self.load_button.setStyleSheet(self.button_stylesheet)
        self.load_button.setFixedSize(100, 25)

        self.save_button = QPushButton("Save Config")
        self.save_button.setStyleSheet(self.button_stylesheet)
        self.save_button.setFixedSize(100, 25)

        # Connect button actions
        self.run_button.clicked.connect(self.run)
        self.help_button.clicked.connect(self.help)
        self.udp_button.clicked.connect(self.udp_run)
        self.kafka_button.clicked.connect(self.kafka_run)
        self.load_button.clicked.connect(self.load_config)
        self.save_button.clicked.connect(self.save_config)


        # Add buttons to layout
        top_button_layout.addWidget(self.run_button)
        top_button_layout.addWidget(self.help_button)
        top_button_layout.addWidget(self.udp_button)
        top_button_layout.addWidget(self.kafka_button)
        top_button_layout.addWidget(self.load_button)
        top_button_layout.addWidget(self.save_button)

        layout.addWidget(top_widget)
    
        # Create main button area
        self.buttons_widget = Buttons(main_window=self)
        layout.addWidget(self.buttons_widget)

        self.special_clicked_map = {
            self.buttons_widget.FUSION_1: self.fusion_run
        }

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Add overlay for drawing connection lines between buttons
        self.connection_overlay = ConnectionOverlay([], parent=self.centralWidget())
        viewport = self.buttons_widget.scroll_area.viewport()
        rect = viewport.rect()
        pos = viewport.mapTo(self.centralWidget(), rect.topLeft())
        self.connection_overlay.setGeometry(QRect(pos, rect.size()))
        self.buttons_widget.scroll_area.verticalScrollBar().valueChanged.connect(self.update_overlay_position)
        self.buttons_widget.scroll_area.horizontalScrollBar().valueChanged.connect(self.update_overlay_position)
        self.connection_overlay.stackUnder(self.buttons_widget)
        self.buttons_widget.scroll_area.viewport().installEventFilter(self)

        # Define connections that should be drawn as straight lines
        self.straight_connections = {
            (self.buttons_widget.Audio.button, self.buttons_widget.Transcript.button),
            (self.buttons_widget.Video.button, self.buttons_widget.Skeleton.button),
        }

        QTimer.singleShot(1000, self.update_connections)

    def eventFilter(self, source, event):
        # Update overlay when scroll area is redrawn
        if source == self.buttons_widget.scroll_area.viewport():
            if event.type() == QEvent.Paint:  # oder QEvent.Scroll, je nach Qt-Version
                self.update_overlay_position()
        return super().eventFilter(source, event)

    def update_overlay_position(self):
        # Move the overlay to match the scroll viewport
        viewport = self.buttons_widget.scroll_area.viewport()
        rect = viewport.rect()
        pos = viewport.mapTo(self.centralWidget(), rect.topLeft())
        self.connection_overlay.setGeometry(QRect(pos, rect.size()))

        self.update_connections()
        self.connection_overlay.update()

    def update_connections(self):
        # Updates connections between widgets
        try:
            raw_connections = self.buttons_widget.get_connections()
            connection_data = []

            for source, targets in raw_connections.items():
                try:
                    if not is_valid_widget(source):
                        continue

                    s_rect = source.rect()

                    frame_offset = self.connection_overlay.mapToGlobal(self.connection_overlay.rect().topLeft())
                    source_global = source.mapToGlobal(QPoint(s_rect.right() , s_rect.center().y() ))
                    source_point = source_global - frame_offset
                    #print(f"Quelle mapped: {source_point}")
                except Exception as e:
                    print("Error (global map):", e)
                    continue

                for target in targets:
                    try:
                        if not is_valid_widget(target):
                            continue

                        t_rect = target.rect()
                        target_global = target.mapToGlobal(QPoint(t_rect.left(), t_rect.center().y()))
                        target_point = target_global - frame_offset
                    except Exception as e:
                        print("Error (global map):", e)
                        continue

                    is_active = "lightgreen" in source.styleSheet() and "lightgreen" in target.styleSheet()

                    # Use vertical line for defined straight connections
                    if (source, target) in self.straight_connections:
                        source_point = source_global = source.mapToGlobal(
                            QPoint(s_rect.center().x(), s_rect.bottom())
                        )
                        target_point = target_global = target.mapToGlobal(
                            QPoint(t_rect.center().x(), t_rect.top())
                        )
                    else:
                        source_point = source.mapToGlobal(
                            QPoint(s_rect.right(), s_rect.center().y())
                        )
                        target_point = target.mapToGlobal(
                            QPoint(t_rect.left(), t_rect.center().y())
                        )

                    # Convert to overlay coordinates
                    source_point = source_point - frame_offset
                    target_point = target_point - frame_offset

                    connection_data.append((source_point, target_point, is_active))

            self.connection_overlay.update_connections(connection_data)
            self.connection_overlay.safe_to_draw = True
            self.connection_overlay.update()

        except Exception as e:
            import traceback
            print("[update_connections] Error:", e)
            traceback.print_exc()

    def resizeEvent(self, event):
        # Resize the connection overlay when the window is resized
        super().resizeEvent(event)
        self.connection_overlay.setGeometry(self.centralWidget().contentsRect())

    def help(self):
        # Open help window
        self.help_window = HelpWindow()
        self.help_window.show()

    def start_pipeline(self):
        # Start AffectPipeline with current parameters
        print("Initializing and starting pipeline...")

        pipeline = create_pipeline()
        self.logging_module = pipeline.LOGGING_MODULE
        self.pipeline = pipeline

        # Connect buttons to logging module
        self.buttons_widget.VoiceActivity.set_logging_module(self.logging_module)
        self.buttons_widget.FaceTracking.set_logging_module(self.logging_module)
        self.buttons_widget.BodyTracking.set_logging_module(self.logging_module)

        self.pipeline.start(self)
        time.sleep(1)

        print("Pipeline started!")
        self.buttons_widget.VoiceActivity.start_status_timer()
        self.buttons_widget.FaceTracking.start_status_timer()
        self.buttons_widget.BodyTracking.start_status_timer()

        for button in self.buttons_widget.float_buttons:
            button.set_pipeline_running(True)

        # Start video stream if not running
        video_stream_widget = self.buttons_widget.Video.stream
        if not video_stream_widget.is_stream_running():
            print("Starting video stream")
            video_stream_widget.start_stream()

    def stop_pipeline(self):
        if self.pipeline is not None:
            self.pipeline.stop()
            self.pipeline = None
            for button in self.buttons_widget.float_buttons:
                if hasattr(button, "set_pipeline_running"):
                    button.set_pipeline_running(False)

    def run(self):
        # Toggle pipeline run/stop
        self.run_active = not self.run_active
        if self.run_active:
            self.run_button.setText("Stop")
            self.run_button.setStyleSheet(self.red_stylesheet)
            self.start_pipeline()
        else:
            self.run_button.setText("Run")
            self.run_button.setStyleSheet(self.green_stylesheet)
            self.stop_pipeline()

    def udp_run(self):
        # Toggle UDP state and update parameter + button style
        self.udp_button_active = not self.udp_button_active
        if self.udp_button_active:
            self.udp_button.setStyleSheet(self.green_stylesheet)
            RightClickWindow.PARAMETERS["enable_udp"] = True
        else:
            self.udp_button.setStyleSheet(self.button_stylesheet)
            RightClickWindow.PARAMETERS["enable_udp"] = False

    def kafka_run(self):
        # Toggle Kafka state and update parameter + button style
        self.kafka_button_active = not self.kafka_button_active
        if self.kafka_button_active:
            self.kafka_button.setStyleSheet(self.green_stylesheet)
            RightClickWindow.PARAMETERS["enable_kafka"] = True
        else:
            self.kafka_button.setStyleSheet(self.button_stylesheet)
            RightClickWindow.PARAMETERS["enable_kafka"] = False

    def fusion_run(self):
        # Toggle FUSION mode and update style and config
        self.fusion_button_active = not self.fusion_button_active
        if self.fusion_button_active:
            self.buttons_widget.FUSION_1.setStyleSheet(self.active_style)
            RightClickWindow.PARAMETERS["enable_fusion"] = True
        else:
            self.buttons_widget.FUSION_1.setStyleSheet(self.inactive_style)
            RightClickWindow.PARAMETERS["enable_fusion"] = False

    def load_config(self):
        # Load parameters from a JSON config file and update buttons
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Configuration", "", "JSON Files (*.json);;All Files (*)",
                                                   options=options)
        if file_path:
            config_data = load_config(file_path)
            if config_data:
                deep_update(RightClickWindow.PARAMETERS, config_data)
                print("Configuration successfully loaded:", RightClickWindow.PARAMETERS)
                self.sync_buttons_with_parameters()

    def save_config(self):
        # Save current parameters to a JSON config file
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Configuration", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_path:
            if not file_path.endswith(".json"):
                file_path += ".json"
            save_successful = save_config(file_path, RightClickWindow.PARAMETERS)
            if not save_successful:
                print("Failed to save configuration.")

    def sync_buttons_with_parameters(self):
        # Method for visualizing and activating the buttons
        # that have the value True as parameter value in the loaded .json file
        button_map = {
            "micro": self.buttons_widget.Micro,
            "audio": self.buttons_widget.Audio,
            "voiceactivity": self.buttons_widget.VoiceActivity,
            "paralinguistic": self.buttons_widget.PARALINGUISTIC,
            "transcript": self.buttons_widget.Transcript,
            "sentiment": self.buttons_widget.SENTIMENT,
            "camera": self.buttons_widget.Camera,
            "video": self.buttons_widget.Video,
            "facetracking": self.buttons_widget.FaceTracking,
            "facialexpression": self.buttons_widget.FACIALEXPRESSION,
            "skeleton": self.buttons_widget.Skeleton,
            "bodytracking": self.buttons_widget.BodyTracking,
            "pose": self.buttons_widget.POSE,
            "fusion": self.buttons_widget.FUSION_1,
            "udp": self.udp_button,
            "kafka": self.kafka_button
        }

        unimodal_results_map = {
            "fusion_use_para_v": self.buttons_widget.Pleasure_1,
            "fusion_use_para_a": self.buttons_widget.Arousal_1,
            "fusion_use_para_d": self.buttons_widget.Dominance_1,
            "fusion_use_sentiment_v": self.buttons_widget.Pleasure_2,
            "fusion_use_face_v": self.buttons_widget.Pleasure_3,
            "fusion_use_face_a": self.buttons_widget.Arousal_2,
            "fusion_use_face_d": self.buttons_widget.Dominance_2,
            "fusion_use_pose_d": self.buttons_widget.Dominance_3,
        }

        for key, button in button_map.items():
            param_key = f"enable_{key}"
            if param_key in RightClickWindow.PARAMETERS:
                enabled = RightClickWindow.PARAMETERS[param_key]

                actual_button = button.button if hasattr(button, "button") else button

                if key == "udp":
                    if enabled:
                        actual_button.setStyleSheet(self.green_stylesheet)
                        self.udp_button_active = True
                    else:
                        actual_button.setStyleSheet(self.button_stylesheet)
                        self.udp_button_active = False

                elif key == "kafka":
                    if enabled:
                        actual_button.setStyleSheet(self.green_stylesheet)
                        self.kafka_button_active = True
                    else:
                        actual_button.setStyleSheet(self.button_stylesheet)
                        self.kafka_button_active = False

                elif key == "fusion":
                    if enabled:
                        actual_button.setStyleSheet(self.active_style)
                        actual_button.setVisible(True)
                        self.buttons_widget.Pleasure_4.setStyleSheet(self.active_style)
                        self.buttons_widget.Arousal_3.setStyleSheet(self.active_style)
                        self.buttons_widget.Dominance_4.setStyleSheet(self.active_style)
                        self.buttons_widget.Pleasure_4.setVisible(True)
                        self.buttons_widget.Arousal_3.setVisible(True)
                        self.buttons_widget.Dominance_4.setVisible(True)
                        self.fusion_button_active = True
                    else:
                        actual_button.setStyleSheet(self.inactive_style)
                        self.fusion_button_active = False

                else:
                    if enabled:
                        actual_button.setStyleSheet(self.active_style)
                        button.setVisible(True)

                        if hasattr(button, "stream") and hasattr(button.stream, "start_stream"):
                            button.stream.start_stream()

                        if button in self.special_clicked_map:
                            self.special_clicked_map[button]()

                        # Set visibility recursively
                        self.buttons_widget.propagate_visibility(actual_button)
                    else:
                        actual_button.setStyleSheet(self.inactive_style)
        for param_key, button in unimodal_results_map.items():
            if param_key in RightClickWindow.PARAMETERS:
                enabled = RightClickWindow.PARAMETERS[param_key]
                if enabled:
                    button.setStyleSheet(self.active_style)
                    button.setVisible(True)
                else:
                    button.setStyleSheet(self.inactive_style)

    def closeEvent(self, event):
        # Stop pipeline when window is closed
        self.stop_pipeline()
        event.accept()
