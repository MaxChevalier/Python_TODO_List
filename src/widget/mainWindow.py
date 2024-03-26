from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QScrollArea)
from PySide6.QtCore import Qt

from .newTodo import NewTodo
from src.ToDoObject import ToDoObject
from .Todo import ToDoWidget

class MainWindows(QMainWindow):
    """
    fenetre principale de l'application qui contient:
    - le formulaire pour ajouter une tâche
    - la liste des tâches
    """
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projet")
        self.resize(800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.Vbox = QVBoxLayout(self.central_widget)
        
        self.NewTodoWidget = NewTodo()
        self.Vbox.addWidget(self.NewTodoWidget)
        
        # Créer un QScrollArea pour contenir la liste des tâches
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # Permettre à son contenu d'être redimensionnable
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_area.setWidget(self.scroll_widget)
        
        self.Vbox.addWidget(self.scroll_area)
        
        # Ajouter les tâches à la QVBoxLayout à l'intérieur du QScrollArea
        data = ToDoObject.get_all()
        for todo in data:
            todo_widget = ToDoWidget(todo)
            self.scroll_layout.addWidget(todo_widget)
            
        # Définir le QScrollArea comme widget à l'intérieur du QVBoxLayout
        self.Vbox.addWidget(self.scroll_area)
        
        
        
        
        