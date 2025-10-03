import tkinter as tk
from tkinter import Tk
import pyperclip

def copy_to_clipboard_mp(text):
    text = str(text)

    # Essayer d'abord pyperclip : module de gestion du presse-papier multi-plateforme
    try:
        print("Utilisation de 'pyperclip'")
        # Envoie de la variable dans le presse-papier de l'OS en cours
        pyperclip.copy(text)
        return
    except pyperclip.PyperclipException:
        pass

    # Repli sur Tkinter si problème avec pyperclip
    try:
        print("Utilisation de 'TKinter clipboard'")
        # Créer une instance de fenêtre pour utiliser les méthodes clipboard_xxx() associées
        root = Tk()
        # cacher la fenêtre
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()  # Forcer le traitement immédiat de tous les événements en attente
        root.destroy()
    except (tk.TclError, AttributeError):
        raise RuntimeError("Échec de l'accès au presse-papier")