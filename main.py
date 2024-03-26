"""
    démare le projet en appelant la fonction main
    le fichier doit etre executé avec l'un des argument ci-joint
    - "console" pour lancer le projet en mode console
    - "gui" pour lancer le projet en mode gui
"""
import sys
from src.console import Console
from src.gui import GUI

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == "console":
            Console().run()
        elif sys.argv[1] == "gui":
            GUI().run()
        else:
            print("Argument invalide")
    else:
        print("Argument manquant")