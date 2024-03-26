import json
from random import randint


class ToDoObject:
    """
    Object représentant une tâche
    Attributs:
    - title: str, titre de la tâche
    - status: str, status de la tâche (En cours ou Terminé)
    - id: int, identifiant unique de la tâche
    """
        
    def __init__(self, title: str, status: str, id: int = -1):
        self.title = title
        self.status = status
        self.id = id
        
    def __str__(self):
        return f'{self.title} - {self.status}'
    
    @classmethod
    def get_all(cls) -> list:
        """Récupère toutes les tâches à partir du fichier data.json et les retourne sous forme de liste d'objets ToDoObject"""
        with open('data.json') as f:
            data_json = json.load(f)
        return [ToDoObject(**data) for data in data_json.values()]
    
    def save(self):
        """Sauvegarde la tâche dans le fichier data.json et lui attribue un identifiant unique s'il n'en a pas déjà un"""
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas, initialisez une liste vide
            data = dict()

        if self.id == -1:
            while self.id == -1 or self.id in data.keys():
                self.id = hex(randint(0, 65536))
        data[self.id] = vars(self)

        with open('data.json', 'w') as f:
            json.dump(data, f)
            
    def delete(self):
        """Supprime la tâche du fichier data.json"""
        with open('data.json', 'r') as f:
            data = json.load(f)
        data.pop(self.id)
        with open('data.json', 'w') as f:
            json.dump(data, f)