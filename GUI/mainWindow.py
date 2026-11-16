from PySide6.QtWidgets import QPushButton, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, QTimer, QPoint, QRect, QEvent
from GUI.buttons import Buttons
from GUI.styles import active_style, inactive_style, button_stylesheet, green_stylesheet, red_stylesheet
from GUI.config_handler import load_config, save_config, deep_update
from GUI.pipeline_handler import create_pipeline
from GUI.custom_button import CustomButton
from GUI.connectionlines import ConnectionOverlay
from GUI.rightClickWindow import RightClickWindow
from GUI.connectionlines import is_valid_widget
from GUI.helpWindow import HelpWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up window appearance and title
        self.setWindowTitle("AffectToolbox")
        self.setStyleSheet("background-color: black;")
        self.pipeline = None
        self.logging_module = None

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
        self.run_active = False

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
        self._preview_containers = (
            self.buttons_widget.Audio, self.buttons_widget.Transcript,
            self.buttons_widget.Video, self.buttons_widget.FaceTracking,
            self.buttons_widget.FaceMesh, self.buttons_widget.Skeleton,
            self.buttons_widget.BodyTracking,
        )
        self._status_buttons = (
            self.buttons_widget.VoiceActivity, self.buttons_widget.FaceTracking.button,
            self.buttons_widget.BodyTracking.button, self.buttons_widget.FaceMesh.button,
        )
        layout.addWidget(self.buttons_widget)

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
        self.sync_buttons_with_parameters()

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

                    is_active = (
                        self.buttons_widget.is_selected(source)
                        and self.buttons_widget.is_selected(target)
                    )

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
        if self.pipeline is not None:
            raise RuntimeError("Stop the current pipeline before starting another one.")
        self._set_configuration_enabled(False)
        self.pipeline = create_pipeline()
        self.logging_module = self.pipeline.LOGGING_MODULE
        try:
            for button in self._status_buttons:
                button.set_logging_module(self.logging_module)
            self.buttons_widget.FaceMesh.button.set_pipeline(self.pipeline)
            self.pipeline.start(self)
        except Exception:
            self.stop_pipeline()
            raise

        self.buttons_widget.set_pipeline_running(True)
        for button in self._status_buttons:
            button.start_status_timer()
        for button in self.buttons_widget.float_buttons:
            button.timer.start(1000)
        self._update_run_button()

    def stop_pipeline(self):
        self.buttons_widget.set_pipeline_running(False)
        for button in self._status_buttons:
            button.timer.stop()
            button.set_logging_module(None)
            button.set_status("grey")
        self.buttons_widget.FaceMesh.button.set_pipeline(None)
        for button in self.buttons_widget.float_buttons:
            button.timer.stop()
            button.setText(button.base_text)

        if self.pipeline is not None:
            # Keep the reference if shutdown fails so cleanup can be retried.
            self.pipeline.stop()
            self.pipeline = None
        self.logging_module = None
        self.START = False
        self._update_run_button()

    def _update_run_button(self):
        self.run_active = self.pipeline is not None
        self.run_button.setText("Stop" if self.run_active else "Run")
        self.run_button.setStyleSheet(self.red_stylesheet if self.run_active else self.green_stylesheet)
        self._set_configuration_enabled(not self.run_active)
        self._update_output_buttons()
        self.update_connections()

    def run(self):
        try:
            if self.pipeline is None:
                self.start_pipeline()
            else:
                self.stop_pipeline()
        except Exception as error:
            QMessageBox.warning(self, "Pipeline error", str(error))
        finally:
            self._update_run_button()

    def _set_configuration_enabled(self, enabled):
        # Lock controls individually so preview labels keep their normal colours.
        for button in self.buttons_widget.findChildren(QPushButton):
            button.setEnabled(enabled)
        plot = self.buttons_widget.Audio.stream.plot_widget
        plot.setMenuEnabled(enabled)
        plot.setMouseEnabled(x=enabled, y=enabled)
        for button in (self.udp_button, self.kafka_button, self.load_button, self.save_button):
            button.setEnabled(enabled)

    def _update_output_buttons(self):
        for button, key in ((self.udp_button, "enable_udp"), (self.kafka_button, "enable_kafka")):
            self.buttons_widget.set_selected(button, RightClickWindow.PARAMETERS[key])

    def udp_run(self):
        params = RightClickWindow.PARAMETERS
        params["enable_udp"] = not params["enable_udp"]
        self.buttons_widget.previews_enabled = True
        self.buttons_widget.refresh_selections()
        self._update_output_buttons()

    def kafka_run(self):
        params = RightClickWindow.PARAMETERS
        params["enable_kafka"] = not params["enable_kafka"]
        self.buttons_widget.previews_enabled = True
        self.buttons_widget.refresh_selections()
        self._update_output_buttons()

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
        self.buttons_widget.previews_enabled = True
        RightClickWindow.PARAMETERS["show_face_mesh"] = RightClickWindow.PARAMETERS["enable_face_mesh_loop"]
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
            "face_mesh_loop": self.buttons_widget.FaceMesh,
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

        params = RightClickWindow.PARAMETERS
        for key, component in button_map.items():
            selected = params.get(f"enable_{key}", False)
            button = component.button if hasattr(component, "button") else component
            self.buttons_widget.set_selected(button, selected)
            if selected:
                component.setVisible(True)
                self.buttons_widget.propagate_visibility(button)

        for key, button in unimodal_results_map.items():
            selected = params.get(key, False)
            self.buttons_widget.set_selected(button, selected)
            if selected:
                button.setVisible(True)

        for button in (self.buttons_widget.Pleasure_4, self.buttons_widget.Arousal_3, self.buttons_widget.Dominance_4):
            self.buttons_widget.set_selected(button, params["enable_fusion"])
            if params["enable_fusion"]:
                button.setVisible(True)
        self.buttons_widget.refresh_selections()
        self._update_output_buttons()
        self.update_connections()

    def closeEvent(self, event):
        try:
            self.stop_pipeline()
        except Exception as error:
            QMessageBox.warning(self, "Shutdown incomplete", str(error))
            event.ignore()
            return
        event.accept()
