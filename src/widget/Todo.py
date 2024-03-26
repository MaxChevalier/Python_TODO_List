from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget, QLabel, QPushButton, QHBoxLayout)
from src.ToDoObject import ToDoObject


class ToDoWidget (QWidget) :
    
    def __init__(self, ToDo: ToDoObject, parent=None) -> None:
        super(ToDoWidget, self).__init__(parent)
        self.ToDo = ToDo
        self.title = QLabel(ToDo.title)
        self
        self.status = QPushButton(ToDo.status)
        self.status.setMaximumWidth(100)
        self.status.setMinimumWidth(100)
        self.delete = QPushButton("🗑")
        self.delete.setMaximumWidth(30)
        self.delete.setMinimumWidth(30)
        self.delete.clicked.connect(self.deleteToDo)
        self.status.clicked.connect(self.changeStatus)
        layout = QHBoxLayout()
        layout.addWidget(self.status)
        layout.addWidget(self.delete)
        layout.addWidget(self.title)
        self.setLayout(layout)
    
    def deleteToDo(self):
        self.ToDo.delete()
        self.deleteLater()
        
    def changeStatus(self):
        if self.ToDo.status == "En cours":
            self.ToDo.status = "Terminé"
        else:
            self.ToDo.status = "En cours"
        self.ToDo.save()
        self.status.setText(self.ToDo.status)
        
    
        
        