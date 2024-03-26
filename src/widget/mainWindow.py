from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QListWidget, QListWidgetItem)
from src.widget.newTodo import NewTodo
from src.ToDoObject import ToDoObject
from src.widget.Todo import ToDoWidget

class MainWindows(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projet")
        self.resize(800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.Vbox = QVBoxLayout(self.central_widget)
        
        self.NewTodoWidget = NewTodo()
        self.Vbox.addWidget(self.NewTodoWidget)
        
        self.list_todo = QVBoxLayout()
        
        data = ToDoObject.get_all()
        for todo in data:
            
            todo_widget = ToDoWidget(todo)
            self.list_todo.addWidget(todo_widget)
        self.Vbox.addLayout(self.list_todo)
        
        
        
        
        