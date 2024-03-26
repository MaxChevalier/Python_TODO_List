import sys
from PySide6.QtWidgets import QApplication
from .widget.mainWindow import MainWindows

class GUI :
    def __init__(self) :
        pass
    
    def run(self):
        """lance le projet en mode gui"""
        
        app = QApplication(sys.argv)

        main_wind = MainWindows()
        main_wind.show()

        sys.exit(app.exec())
        
        