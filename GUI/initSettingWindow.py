from PySide6.QtCore import Qt
from GUI.rightClickWindow import RightClickWindow

def InitSettingWindow(button):
    # Open right-click settings window for a specific widget
    dlg = RightClickWindow(name=button.base_text)
    dlg.setWindowTitle(f"{button.base_text} Settings")
    dlg.setWindowModality(Qt.ApplicationModal)
    dlg.exec()  # blocked until window is closed