from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QTimer
import modules.QueueSystem as qs
from rightClickWindow import RightClickWindow

class FloatButton(QPushButton):
    """
    A custom QPushButton that periodically
    fetches float values from predefined queues
    """
    @staticmethod
    def safe_last(queue):
        #Returns the last element of a queue, or None if the queue is empty
        return queue[-1] if len(queue) > 0 else None

    # Configuration mapping for each button label
    button_config = {
        "Pleasure_1": {
            "param_key": "fusion_use_para_v",
            "source": lambda: FloatButton.safe_last(qs.VALENCE_SPEECH),
        },
        "Arousal_1": {
            "param_key": "fusion_use_para_a",
            "source": lambda: FloatButton.safe_last(qs.AROUSAL_SPEECH),
        },
        "Dominance_1": {
            "param_key": "fusion_use_para_d",
            "source": lambda: FloatButton.safe_last(qs.DOMINANCE_SPEECH),
        },
        "Pleasure_2": {
            "param_key": "fusion_use_sentiment_v",
            "source": lambda: FloatButton.safe_last(qs.VALENCE_SENTIMENT),
        },
        "Pleasure_3": {
            "param_key": "fusion_use_face_v",
            "source": lambda: FloatButton.safe_last(qs.VALENCE_FACE),
        },
        "Arousal_2": {
            "param_key": "fusion_use_face_a",
            "source": lambda: FloatButton.safe_last(qs.AROUSAL_FACE),
        },
        "Dominance_2": {
            "param_key": "fusion_use_face_d",
            "source": lambda: FloatButton.safe_last(qs.DOMINANCE_FACE),
        },
        "Dominance_3": {
            "param_key": "fusion_use_pose_d",
            "source": lambda: FloatButton.safe_last(qs.DOMINANCE_POSE),
        },
        "Pleasure_4": {
            "param_key": None,
            "source": lambda: FloatButton.safe_last(qs.FUSION)[0] if qs.FUSION else None,
        },
        "Arousal_3": {
            "param_key": None,
            "source": lambda: FloatButton.safe_last(qs.FUSION)[1] if qs.FUSION else None,
        },
        "Dominance_4": {
            "param_key": None,
            "source": lambda: FloatButton.safe_last(qs.FUSION)[2] if qs.FUSION else None,
        }
    }

    def __init__(self, label_text, name, active_stylesheet=None, main_window=None):
        super().__init__(label_text)
        self.base_text = label_text # Text shown on the button
        self.key_name = name # Key used to access button_config
        self.main_window = main_window
        self.active_stylesheet = active_stylesheet

        # Timer to update the float value every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_float)
        self.timer.start(1000)

    def update_float(self):
        #pdates the button label to include a float value
        config = self.button_config.get(self.key_name, None)
        if not config:
            return  # No configuration found

        show_float = False

        # Check if a parameter key is defined and active
        if config["param_key"]:
            show_float = RightClickWindow.PARAMETERS.get(config["param_key"], False)
        else:
            # Fallback: if no param_key, rely on active style
            if self.active_stylesheet and "lightgreen" in self.styleSheet():
                show_float = True

        if show_float:
            value = config["source"]()
            if value is not None:
                self.setText(f"{self.base_text} {value:.2f}")
            else:
                self.setText(self.base_text)
        else:
            self.setText(self.base_text)

