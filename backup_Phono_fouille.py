"""
pip install numpy sounddevice

Crée une copie de tout le contenu d'un dossier vers un autre dossier
en excluant une liste d'éléments
"""

import os
import shutil
from datetime import datetime
import numpy as np
import sounddevice as sd

def save(source, destination, exceptions):
    # Créer le dossier de destination s'il n'existe pas
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source):
        # Chemin complet de l'élément
        s = os.path.join(source, item)
        d = os.path.join(destination, item)

        # Ignorer les éléments dans les exceptions
        if item in exceptions:
            continue

        # Copier le dossier ou le fichier
        if os.path.isdir(s):
            shutil.copytree(s, d, ignore=shutil.ignore_patterns(*exceptions))
        else:
            shutil.copy2(s, d)

def beep(frequency, duration):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, sample_rate)
    sd.wait()

    print(f"Sauvegarde de 'Phono_fouille' réussie !")

if __name__ == "__main__":
    # Chemin du dossier source (le même que celui du script)
    source_dir = os.path.dirname(os.path.abspath(__file__))

    # Chemin du dossier où faire la sauvegarde
    destination_base_dir = os.path.join(source_dir, "../Backup_Phono_fouille")

    # Créer le nom du nouveau dossier selon la date et l'heure actuelle
    date_heure = datetime.now().strftime("%Y-%m-%d_%H-%M")
    destination_dir = os.path.join(destination_base_dir, f"Phono_fouille_{date_heure}")

    # Liste des exceptions
    exceptions = ["__pycache__",
                  "Backup_Phono_fouille",
                  "Captures d'écran",
                  "Doc",
                  "Essai",
                  "OBS",
                  "venv_phono",
                  "backup_Phono_fouille.py",
                  "Création requête",
                  "Essais_SQLalchemy",
                  "DB.Browser.for.SQLite-v3.13.1-x86.64-v2.AppImage"
                  ]

    # Sauvegarder les fichiers et dossiers
    save(source_dir, destination_dir, exceptions)

    # Émettre un bip sonore à 440 Hz pendant 1 seconde
    beep(440, 0.5)
