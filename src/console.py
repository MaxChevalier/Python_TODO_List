from src.ToDoObject import ToDoObject

class Console :

    def run(self):
        """lance le projet en mode console"""
        
        print("Bienvenue sur votre gestionnaire de tâches\n\n")
        self.selectToDo()
    
    def selectToDo(self):
        """permet de selectionner une tâche ou une action"""
        
        print("Selectionner une tâche")
        allToDo = ToDoObject.get_all()
        for i in range(len(allToDo)):
            print(f'{i} - {allToDo[i]}')
        print("new - Ajouter une nouvelle tâche \n\
quit - Quitter")
        choice = input()
        if choice == "new":
            self.addToDo()
        elif choice == "quit":
            pass
        else:
            try:
                self.editToDo(allToDo[int(choice)])
            except:
                print("Erreur lors de la selection de la tâche")
                self.selectToDo()
            
    def addToDo(self):
        """permet d'ajouter une tâche"""
        
        title = input("Titre: ")
        status = "En cours"
        try:
            ToDoObject(title, status).save()
            print("Tâche ajoutée avec succès")
        except:
            print("Erreur lors de l'ajout de la tâche")
        self.selectToDo()
        
    def editToDo(self, toDo: ToDoObject):
        """
        Permet de modifier une tâche\n
        prend en paramètre la tâche à modifier
        """
        
        print("Selectionner une action\n\
1 - Marquer comme terminée\n\
2 - Supprimer\n\
3 - Modifier le titre\n\
quit - Quitter")
        choice = input()
        if choice == "1":
            toDo.status = "Terminée"
            toDo.save()
            print("Tâche marquée comme terminée")
        elif choice == "2":
            toDo.delete()
            print("Tâche supprimée")
        elif choice == "3":
            self.editTitle(toDo)
        elif choice == "quit":
            pass
        else:
            print("Erreur lors de la selection de l'action")
            self.editToDo(toDo)
            return
        self.selectToDo()
        
    