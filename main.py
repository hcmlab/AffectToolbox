from GUI.main import MainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

def main():
    """Main function to run the application"""
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("AffectPipeline")
    window.setWindowIcon(QIcon("./GUI/Icons/python.svg"))
    window.show() #Windowed mode
    #window.showFullScreen() #Fullscreen mode
    app.exec()
    
if __name__ == "__main__":
    main()