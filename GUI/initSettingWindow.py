from PySide6.QtCore import Qt
from GUI.rightClickWindow import RightClickWindow

def InitSettingWindow(button):
    # Open right-click settings window for a specific widget
    dlg = RightClickWindow(name=button.base_text)
    dlg.setWindowTitle(f"{button.base_text} Settings")
    dlg.setWindowModality(Qt.ApplicationModal)
    dlg.exec()  # blocked until window is closed
    if button.base_text == "FaceMesh" and button.main_window is not None:
        button.main_window.sync_buttons_with_parameters()
