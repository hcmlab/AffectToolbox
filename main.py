from GUI.main import MainWindow
from PyQt6.QtWidgets import QApplication

def main():
    """Main function to run the application"""
    app = QApplication([])
    window = MainWindow()
    #window.show() #Windowed mode
    window.showFullScreen() #Fullscreen mode
    app.exec()
    
if __name__ == "__main__":
    main()