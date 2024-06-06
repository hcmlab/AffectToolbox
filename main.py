from GUI.main import MainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from GUI import ClickEvents

def sub_main():
    """Main function to run the application"""
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("AffectPipeline")
    window.setWindowIcon(QIcon("./GUI/Icons/python.svg"))
    window.show() #Windowed mode
    #window.showFullScreen() #Fullscreen mode

    ClickEvents.PleasureClick(window)
    ClickEvents.ArousalClick(window)
    ClickEvents.DominanceClick(window)
    ClickEvents.ParaPleasureClick(window)
    ClickEvents.ParaArousalClick(window)
    ClickEvents.ParaDominanceClick(window)
    ClickEvents.VoiceActivityClick(window)

    ClickEvents.PlayButtonClick(window)

    app.exec()

def main():
    sub_main()
    
if __name__ == "__main__":
    main()