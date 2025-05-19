from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPainterPath, QPen, QColor
from PySide6.QtCore import QPointF, Qt

# function to validate whether a widget is usable for drawing connections
def is_valid_widget(widget):
    try:
        if widget is None:
            return False
        if not widget.isVisible():
            return False
        geom = widget.geometry()
        if geom.width() <= 0 or geom.height() <= 0:
            return False
        return True
    except Exception as e:
        print(f"Error checking widget {widget}:", e)
        return False

# This widget draws connection lines between pairs of points
class ConnectionOverlay(QWidget):
    def __init__(self, connections, parent=None):
        super().__init__(parent)
        self.connections = connections or [] # List of tuples
        self.safe_to_draw = False

        # Ensure the widget does not interfere with mouse events or background rendering
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background: transparent;")

    def update_connections(self, connection_data):
        # Updates the list of connections to draw
        if not isinstance(connection_data, list):
            print("Invalid input – expected list")
            import traceback
            traceback.print_stack()
            return

        valid = True
        for item in connection_data:
            if not isinstance(item, tuple) or len(item) != 3:
                print("Invalid entry:", item)
                valid = False
        if not valid:
            print("Update aborted due to invalid data")
            return

        self.connections = connection_data
        self.update()

    def paintEvent(self, event):
        if not self.safe_to_draw:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for item in self.connections:
            if not isinstance(item, tuple) or len(item) != 3:
                print("Invalid connection item skipping:", item)
                continue

            source_point, target_point, is_active = item

            try:
                # Set pen color based on active status
                color = QColor("green") if is_active else QColor(180, 180, 180)
                pen = QPen(color, 2)
                painter.setPen(pen)

                # Calculate Bezier control points for smooth curve
                dx = (target_point.x() - source_point.x()) * 0.5
                cp1 = QPointF(source_point.x() + dx, source_point.y())
                cp2 = QPointF(target_point.x() - dx, target_point.y())

                path = QPainterPath()
                path.moveTo(source_point)
                path.cubicTo(cp1, cp2, target_point)
                painter.drawPath(path)
            except Exception as e:
                print("Error while drawing connection:", e)


        painter.end()
