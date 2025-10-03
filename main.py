# Phono fouille
# Copyright (c) 2025 Yonnel Bécognée
# Distribué sous Licence Libre Non Commerciale : BY-SA-NC.
# Voir le fichier README.md pour plus d'informations.

import os
import sys

# Obtenir le chemin absolu du répertoire courant (où se trouve main.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Ajouter le répertoire racine au PYTHONPATH
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from controllers.controller import Controller

if __name__ == "__main__":
    controller = Controller()
    # controller.process_form_data()