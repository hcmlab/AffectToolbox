import math
from PySide6.QtWidgets import QPushButton, QStyle, QStyleOptionButton, QStylePainter
from PySide6.QtCore import QTimer, Qt, QSize
from PySide6.QtGui import QFont, QFontMetrics
import modules.QueueSystem as qs
from GUI.rightClickWindow import RightClickWindow

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
        self.label_font = QFont("Segoe UI", 9)
        self.value_font = QFont("Consolas", 16)
        self.value_font.setBold(True)

        # Timer to update the float value every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_float)

    def sizeHint(self):
        size = super().sizeHint()
        label_metrics = QFontMetrics(self.label_font)
        value_metrics = QFontMetrics(self.value_font)
        width = max(label_metrics.horizontalAdvance(self.base_text),
                    value_metrics.horizontalAdvance("\u22120.00")) + 24
        height = label_metrics.height() + value_metrics.height() + 16
        return QSize(width, max(size.height(), height))

    def paintEvent(self, event):
        # Keep the normal button background, hover, focus and click handling.
        option = QStyleOptionButton()
        self.initStyleOption(option)
        option.text = ""
        painter = QStylePainter(self)
        painter.drawControl(QStyle.ControlElement.CE_PushButton, option)
        painter.setPen(Qt.GlobalColor.black)
        if self.isDown():
            painter.translate(1, 1)

        label_rect = self.rect().adjusted(8, 6, -8, -6)
        label_rect.setHeight(QFontMetrics(self.label_font).height())
        painter.setFont(self.label_font)
        painter.drawText(label_rect, Qt.AlignmentFlag.AlignCenter, self.base_text)

        value = self.text()[len(self.base_text):].strip()
        value = value.replace("-", "\u2212").rjust(5) if value else "\u2014"
        value_rect = self.rect().adjusted(8, label_rect.bottom() + 2, -8, -6)
        painter.setFont(self.value_font)
        painter.drawText(value_rect, Qt.AlignmentFlag.AlignCenter, value)

    def update_float(self):
        #pdates the button label to include a float value
        if self.main_window is not None and not self.main_window.buttons_widget.pipeline_running:
            self.setText(self.base_text)
            return
        config = self.button_config.get(self.key_name, None)
        if not config:
            return  # No configuration found

        show_float = False

        # Check if a parameter key is defined and active
        if config["param_key"]:
            show_float = RightClickWindow.PARAMETERS.get(config["param_key"], False)
        else:
            show_float = bool(self.property("selected"))

        if show_float:
            value = config["source"]()
            if value is not None and math.isfinite(value):
                self.setText(f"{self.base_text} {value:.2f}")
            else:
                self.setText(self.base_text)
        else:
            self.setText(self.base_text)

