from PySide6.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QDialog)

from src.ToDoObject import ToDoObject
from .Todo import ToDoWidget

class NewTodo(QDialog):

    def __init__(self, parent=None):
        super(NewTodo, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit()
        self.button = QPushButton("Ajouter la tache")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        self.button.clicked.connect(self.addTodo)
        
    def addTodo(self):
        title = self.edit.text()
        status = "En cours"
        try:
            todo = ToDoObject(title, status)
            todo.save()
            print("Tâche ajoutée avec succès")
            self.parent().parent().scroll_layout.addWidget(ToDoWidget(todo))
        except:
            print("Erreur lors de l'ajout de la tâche")
        self.edit.clear()