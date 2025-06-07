# Entry point of the application
import sys
from PySide6.QtWidgets import QApplication
from GUI.startWindow import StartWindow

# Check if the script is run directly
if __name__ == "__main__":
    # Create the Qt application instance
    app = QApplication(sys.argv)
    # Create and show the start window
    start_window = StartWindow()
    start_window.show()
    # Start the Qt event loop and exit when the application is closed
    sys.exit(app.exec())
