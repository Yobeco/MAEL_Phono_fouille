import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview

class Tableview_interact(Tableview):
    # searchable=False parce que résultats filtrés ressortent quand-même avec la méthode get_rows() + Pages ne sont plus parcourables...
    def __init__(self, master=None, coldata=None, rowdata=None, paginated=True, searchable=False, **kwargs):
        super().__init__(master, coldata=coldata, rowdata=rowdata, paginated=paginated, searchable=searchable, **kwargs)

        self.master = master
        self.coldata = coldata
        self.rowdata = rowdata
        self.autofit = True

        self.fetch_selected_results()
        self.double_click_on_line()

        # Configuration de l'aspect visuel
        self.conf_columns()


        # Identifier le champ de recherche
        # self.search_entry = self.winfo_children()[0].winfo_children()[1]

        # # Fonction pour insérer le texte et déclencher la recherche
        # # Non utilisé pour le moment.
        # # À déclencher à l'instanciation de ma classe Tableview_interact
        # def trigger_search(default_text):
        #     if self.search_entry:
        #         self.search_entry.insert(0, default_text)
        #         self.search_entry.focus_set()
        #         self.search_entry.event_generate("<Return>")
        #     else:
        #         print("La structure de Tableview a changé, probablement pour un changement de version.")


    # Fonction pour récupérer les données de la ligne sélectionnée
    def double_click_on_line(self, *args):
        # Récupérer l'iid  de la ligne selectionnée
        selected = self.view.selection()
        # print(f"IID de la ligne sélectionnée : {selected}")
        row_iid = self.iidmap.get(selected[0])
        row_iid_val = row_iid.values
        # print("Données de la ligne sélectionnée :", row_iid_val)

        return row_iid_val[1]




    def conf_columns(self):
        """
        Configuration de l'aspect visuel
        """
        # Nombre de ligne par page
        self.pagesize = 20

        # Hauteur du TableView (en lignes)
        self.view.configure(height=20)

        # Position du contenu des colonnes
        self.align_column_center(cid=0)
        self.align_column_left(cid=1)

        # Position du texte des entêtes de colonnes
        self.align_heading_center(cid=0)
        self.align_heading_left(cid=1)

        # Étirer la deuxième colonne
        self.view.column(column=1, stretch=True)


    def update_table(self, data_columns, data_list):

        try:
            """ Met à jour les données sans recréer le widget """
            # 1. Reconstruire les données internes
            self.build_table_data(coldata=data_columns, rowdata=data_list)

            # 2. Recharger la vue avec nouvelles données
            self.load_table_data(clear_filters=True)

            # 3. Appliquer de nouveau les paramètres de présentation
            self.conf_columns()

        except Exception as e:
            print(f"Erreur lors de la mise à jour : {str(e)}")

    def fetch_selected_results(self, *args):
        """
        Retourne toutes les lignes du Tableview (toutes pages), excluant les lignes supprimées.
        """
        # Ne rien mettre True, sinon, ne renvoie que la première page
        # Mais ne prends pas en compte le filtre !!!
        # Vérifier que ça fonctionne !!!
        lignes_visibles = self.get_rows(visible=False, filtered=False, selected=False)
        list_result = []
        for element in lignes_visibles:
            print(element.values)
            list_result.append(element.values)

        print(f"Lignes présentes : {lignes_visibles}")

        str_result = ""

        for element in list_result:
            str_result = str_result + element[1] + "\n"

        print(f"Contenu du presse-papier :\n{str_result}")

        return str_result





if __name__ == '__main__':
    root = ttk.Window()
    root.geometry("600x600")

    coldata = [
        {"text": "n°", "stretch": False, "width": 50},
        {"text": "Mots trouvés", "stretch": True},
    ]
    rowdata = [
        ("1", "Mot 1"),
        ("2", "Mot 2"),
        ("3", "Mot 3")
    ]

    table1 = Tableview_interact(root, coldata, rowdata)
    table1.pack(expand=True, fill="both")

    root.mainloop()
