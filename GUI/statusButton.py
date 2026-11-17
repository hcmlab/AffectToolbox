from PySide6.QtCore import QTimer
from GUI.custom_button import CustomButton

class StatusButton(CustomButton):
    """
    A custom button that visually reflects system status using colored circle symbols.
    Status is updated automatically via a timer or can be set manually.
    """

    # Mapping of status keywords to emoji circles
    CIRCLES = {
        "grey": "⚪",
        "green": "🟢",
        "yellow": "🟡",
        "red": "🔴"
    }

    def __init__(self, label_text, parent=None, main_window=None):
        super().__init__(label_text, parent=parent, main_window=main_window)
        self.base_text = label_text
        self.current_status = "grey"
        self.pipeline = None
        self.update_text()

        # Timer to regularly check and update status
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.trafficLight)

    def start_status_timer(self):
        # Starts the internal timer for automatic status updates every second
        self.timer.start(100 if self.base_text == "VoiceActivity" else 1000)

    def update_text(self):
        # Updates the button label to include the status circle
        circle = self.CIRCLES.get(self.current_status, "⚪")
        self.setText(f"{self.base_text} {circle}")

    def set_status(self, status_color: str):
        # Manually sets the current status if the color is valid
        if status_color in self.CIRCLES:
            self.current_status = status_color
            self.update_text()
        else:
            print(f"Invalid status '{status_color}'")

    def set_logging_module(self, logging_module):
        #Links an external module that provides real-time tracking status
        self.logging_module = logging_module

    def set_pipeline(self, pipeline):
        self.pipeline = pipeline

    def trafficLight(self):
        #Checks system status from the logging module and updates the button's state
        if self.base_text == "FaceMesh":
            if not self.property("selected") or self.pipeline is None or not self.pipeline.FACE_MESH_LOOP:
                self.set_status("grey")
            elif self.pipeline._face_mesh_detected:
                self.set_status("green")
            else:
                self.set_status("yellow")
            return

        if getattr(self, "logging_module", None) is None:
            return

        # If the button is not currently active, reset status to grey
        if not self.property("selected"):
            self.set_status("grey")
            return

        log = self.logging_module
        status = "green"

        # Check specific conditions depending on the button's label
        if self.base_text == "VoiceActivity":
            if not log.TRACKING_VOICE:
                status = "yellow"
            if not log.VOICE_OK:
                status = "red"

        elif self.base_text == "FaceTracking":
            if not log.TRACKING_FACE:
                status = "yellow"
            if not log.CAMERA_OK:
                status = "red"

        elif self.base_text == "BodyTracking":
            if not log.TRACKING_BODY:
                status = "yellow"
            if not log.BODY_OK:
                status = "red"

        self.set_status(status)



