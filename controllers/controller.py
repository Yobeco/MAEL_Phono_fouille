"""
Controller de l'application Phono fouille
"""

from tkinter import Button

from views.view import FormView, Tableview_interact
from models.model import ViewDataPaser, SqlRequestGen
from models.request import Request

from controllers.copy_to_clipboard_mp import copy_to_clipboard_mp

# Pour créer un chemin absolut lors du dépaquetage du fichier exécutable
import sys
import os

def get_database_path():
    """
    Création d'un chemin absolu quand le fichier executable est décompressé dans le dossier temporaire
    """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # Exécution comme un fichier unique PyInstaller détectée
        # --> le début du chemin absolu est mis dans "base_path"
        base_path = sys._MEIPASS
    else:
        # Si le script est lancé dans son environnement habituel
        # --> "base_path" est le dossier du fichier main.py
        base_path = os.path.abspath(".")
    return os.path.join(base_path, "models", "PHONOFOUILLE_2025_04_22_d.db")


class Controller:
    def __init__(self):             # Constructeur de classe --> initialiser les attributs d'un objet lors de sa création.
        # Instanciation de la vue
        self.view = FormView()
        self.table_view = self.view.data_tableview                  # Récupération de l'instance du table_view_interact

        # self.controller = Controller(self.view)
        self.bind_search_button()
        self.bind_copy_button()
        self.bind_line()
        self.view.run()

    def process_form_data(self, *args):
        # Récupère les données de la vue
        data = self.view.get_data
        # Instancier la classe ViewDataPaser (model)
        parser = ViewDataPaser(data)
        # Lancement de la méthode parse() de l'objet "parser"
        # Pour traiter le grand dictionnaire (data) généré par View
        parsed_data = parser.parse_view_data()

        # Afficher show_organized_view_data
        # parser.show_parsed_view_data()

        # Instancier un objet sql_gen de la classe SqlRequestGen
        # Avec les données parsed_data, triées par ViewDataParser
        sql_gen = SqlRequestGen(parsed_data)
        # Génère une requête SQL depuis les données triées par
        query = sql_gen.generate_request()

        print(f"Requête qui sera envoyée : {query}")
        database_path = get_database_path()


        # Instancier la classe Request
        show_results = Request(database_path, query)
        # Lancer la fonction qui affiche les résultats de la recherche
        # et qui renvoie la liste de résultats
        result_list = show_results.make_request()
        # print(result_list)

        self.view.total_var.set(len(result_list))


        data_test_list = [
            ("1", "..."),
            ("2", "..."),
            ("3", "..."),
        ]
        # Lancer update_table qui remplace l'ancien TableView par le nouveau
        self.view.data_tableview.update_table(self.view.data_columns, result_list)


    def bind_search_button(self, *args):
        # Observer les clics sur le bouton "Rechercher" pour lancer la recherche
        self.view.cherch_but.bind("<Button-1>", self.process_form_data)

    def result_to_clipboard(self, *args):
        str_list = ""
        # Récupérer les lignes présentes dans la liste de résultats
        str_list = self.table_view.fetch_selected_results()
        # Les envoyer dans le presse-papier
        copy_to_clipboard_mp(str_list)

    def bind_copy_button(self, *args):
        # Observer les clics sur le bouton "Copier" pour récupérer les résultats
        self.view.copier_but.bind("<Button-1>", self.result_to_clipboard)

    def fetch_one_line(self, *args):
        # Récupérer le mot de la ligne sélectionner
        double_click_on_line = self.table_view.double_click_on_line()
        # Mettre ce mot dans le presse-papier
        copy_to_clipboard_mp(double_click_on_line)


    def bind_line(self, *args):
        # Observer les clics sur la zone des lignes du tableview
        self.view.data_tableview.view.bind('<Double-1>', self.fetch_one_line)

