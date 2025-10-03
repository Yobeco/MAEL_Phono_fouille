"""
https://www.xanthium.in/convert-tkinter-ttkbootstrap-gui-python-script-windows-executable-using-pyinstaller

"""
import ttkbootstrap as ttk
import tkinter as tk

from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip

# Classe affichant la matrice de cases à cocher
from views.matrice_sons import Matrice
# Class pour créer un duo ComboBox + entry
from views.logic_entry import Logic_entry
# Class d'un élément de la liste des résultats
from views.tableview_interact import Tableview_interact

# Largeur de la première colonne des étiquettes (en chr)
larg_etiq = 8


"""
###### FENÊTRE PRINCIPALE ######
"""
class FormView:

    def __init__(self):

        self.root = ttk.Window(themename="cosmo")   # darkly / cosmo / superhero
        # Importer les styles depuis le fichier config_style.py
        self.root.resizable(False, False)

        # Configuration de la fenêtre principale
        self.root.title("Phono fouille - V 0.1")
        # Changer la couleur de fond de la fenêtre
        self.root.configure(padx=0, pady=0)

        ##############################################################
        ######   Frame général pour fond de couleur    ######

        self.col_fond = ttk.Frame(self.root,
                                         padding="20 5 20 10"    # gauche, haut, droite, bas
                                         )
        self.col_fond.pack(fill='both', expand=True)

        ##############################################################
        ######   Niveau marron    ######

        # Création d'un Label personnalisé pour le cadre principal
        self.label_root = ttk.Label(self.col_fond,
                                    text="Recherche de mots :",
                                    font=("Arial", 20),
                                    bootstyle="primary"
                                    )

        # labelwidget=label pour utiliser un label personnalisé
        self.frame_root = ttk.LabelFrame(self.col_fond,
                                         labelwidget=self.label_root,
                                         bootstyle="primary"
                                         )
        self.frame_root.pack(fill='both', expand=True, pady = 10)

        ###############################################################
        ######   Niveau Rose    ######

        frame_a = ttk.Frame(self.frame_root, relief='flat')
        frame_a.pack(fill='both', expand=True, side='left')

        frame_b = ttk.Frame(self.frame_root, relief='flat')
        frame_b.pack(fill='both', expand=True, side='left')

        ###############################################################
        ######   Niveau vert    ######

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #      Colonne de gauche
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        # ---------------------------------------------
        """ Source :  choix de la DB """

        frame_a0 = ttk.Frame(frame_a, relief='flat', width=800)
        frame_a0.pack(anchor="w")

        frame_source = ttk.Frame(frame_a0,
                              relief='flat',
                              width=larg_etiq
                              )
        frame_source.pack(side='left', padx = (10,10), pady = (10,10))

        source_label = ttk.Label(frame_source,
                                text='Source :',
                                font = ("Arial", 15)
                                 )
        source_label.pack()

        # Définir des variables dynamiques pour le checkbox "Lemmes uniquement"
        self.lem_chk_var = tk.BooleanVar(value=False)

        lem_chk = ttk.Checkbutton(frame_source,
                                    text='Lem. uniq.',
                                    variable=self.lem_chk_var
                                    )
        def show_lem_chk():
            lem_chk.pack()

        def hide_lem_chk():
            lem_chk.pack_forget()

        # Tooltip sur lem_chk
        ToolTip(lem_chk, text="Lemmes uniquement\n⟶ Aucun mot accordé")

        # Variable dynamique pour les boutons radio de la source
        self.db_var = tk.StringVar(value="lexique")

        minlex_radio = ttk.Radiobutton(frame_a0,
                                       text='MiniLex',
                                       variable = self.db_var,
                                       value ='minilex'
                                       )
        minlex_radio.pack(side='left', padx = (10,10), pady = (10,10))

        # Tooltip sur minlex_radio
        ToolTip(minlex_radio, text="Minimum de 1200 mots en fin de Cycle 1.\n⟶ AMLA nord")

        lexique_radio = ttk.Radiobutton(frame_a0,
                                        text='Lexique',
                                        variable = self.db_var,
                                        value ='lexique'
                                        )
        lexique_radio.pack(side='left', padx=(10, 10), pady=(5, 5))

        # Tooltip sur minlex_radio
        ToolTip(lexique_radio, text="Plus de 142 000 mots.\n⟶ http://www.lexique.org")

        sep0 = ttk.Separator(frame_a,
                             bootstyle="primary")
        sep0.pack(anchor="w", fill="x")

        # ---------------------------------------------
        """ Difficulté :  choix de la fréquence """

        frame_a1 = ttk.Frame(frame_a, relief='flat')
        frame_a1.pack(anchor="w")

        source_label = ttk.Label(frame_a1,
                                 text='Difficulté :',
                                 font=("Arial", 15),
                                 width=larg_etiq
                                 )
        source_label.pack(side='left', padx=(10, 10), pady=(10, 10))

        #-----------------------------------------------------------
        #   Version de "Difficultés" pour Minima Lexical
        #-----------------------------------------------------------

        # Définir des variables dynamiques pour chaque case à cocher et les initialiser à True
        self.niv1_var = tk.BooleanVar(value=True)
        self.niv2_var = tk.BooleanVar(value=True)
        self.niv3_var = tk.BooleanVar(value=True)

        niv1_ckbt = ttk.Checkbutton(frame_a1,
                                       text='Niveau 1',
                                       variable=self.niv1_var
                                       )

        niv2_ckbt = ttk.Checkbutton(frame_a1,
                                        text='Niveau 2',
                                       variable=self.niv2_var
                                        )

        niv3_ckbt = ttk.Checkbutton(frame_a1,
                                  text='Niveau 3',
                                  variable=self.niv3_var
                                  )

        # -----------------------------------------------------------
        #   Version de "Difficultés" pour Lexique
        # -----------------------------------------------------------

        # Définir des variables dynamiques pour chaque case à cocher et les initialiser
        # à leur valeur "onvalue" pour qu'elles soient cochées au démarrage (1/0 par défaut.)
        self.tr_courant_var = tk.BooleanVar(value=True)
        self.courant_var = tk.BooleanVar(value=True)
        self.as_rare_var = tk.BooleanVar(value=True)
        self.rare_var = tk.BooleanVar(value=True)

        tr_courant_ckbt = ttk.Checkbutton(frame_a1,
                                    text='Très courant',
                                    variable=self.tr_courant_var
                                    )

        courant_ckbt = ttk.Checkbutton(frame_a1,
                                    text='Courant',
                                    variable=self.courant_var
                                    )

        as_rare_ckbt = ttk.Checkbutton(frame_a1,
                                       text='Assez rare',
                                       variable=self.as_rare_var
                                       )

        rare_ckbt = ttk.Checkbutton(frame_a1,
                                    text='Rare',
                                    variable=self.rare_var
                                    )


        sep1 = ttk.Separator(frame_a, bootstyle="primary")
        sep1.pack(anchor="w", fill="x")

        # ---------------------------------------------
        """ Sons : choix des sons """

        frame_a2 = ttk.Frame(frame_a, relief='flat')
        frame_a2.pack(anchor="w")

        sons_label = ttk.Label(frame_a2,
                                 text='Sons :',
                                 font=("Arial", 15),
                                 width=larg_etiq
                                 )
        sons_label.pack(side='left', padx=(10, 0), pady=(10, 10))

        # Cadre qui recevra matrice_sons
        self.contener_sons = ttk.Frame(frame_a2)
        self.contener_sons.pack(side='left', padx=(10, 10), pady=(0, 0))

        # Cadre qui recevra matrice_sons
        self.choix_sons = ttk.Frame(self.contener_sons)
        self.choix_sons.pack(fill='both', expand=True, padx=(10, 10),pady=(0, 0))


        # Fonction pour faire apparaitre les logic_entry au fur et à mesure
        # L'instance de logic_entry suivante n'est visible que si l'entrée précédente n'est pas nulle
        def toggle_logic_entry(inst_ant, inst_target, *args):
            if inst_ant.entry_var.get():  # Si la variable de l' "entry" antérieur n'est' pas nulle
                inst_target.show_logic_entry()
            else:  # Si la variable est nulle
                if inst_target.logic_combo:
                    inst_target.hide_logic_entry()
                    inst_target.combo_var.set("")
                    inst_target.entry_var.set("")


        #################################################
        #    Configuration du logic_entry 1 --> son
        #################################################

        # Créer une instance "son1" de la classe "matrice"
        # La fonction "self.update_entry" est envoyée en paramètre à la classe "matrice" comme callback
        self.son1 = Matrice(self.update_entry_1)
        # Instancier la matrice self.son1.matrice_sons dans le cadre "contener_sons"
        self.son1.create_matrice(self.contener_sons)
        # Cacher la matrice self.son1.matrice_sons au démarrage
        self.son1.matrice_sons.pack_forget()

        # Choix disponibles dans la liste
        combo_liste1 = ["", "avec", "sans"]
        # Variable du ComboBox du logic_entry
        self.logic_sons_combo_1_var = ttk.StringVar(value="avec")
        # Variable de l'entry du logic_entry
        self.son_1_var = ttk.StringVar(value="")

        # Instanciation de Logic_entry
        self.logic_entry_son_1 = Logic_entry(self.choix_sons,  # Cadre conteneur
                                             self.son1,  # Instance de matrice concernée
                                             "son",
                                             combo_liste1,  # Options disponibles
                                             self.logic_sons_combo_1_var,  # Variable dynamique véhiculant la valeur du combobox
                                             self.son_1_var,  # Variable dynamique véhiculant la valeur de l'entry
                                             3,
                                             False
                                             )

        # Tooltip sur logic_entry_son_1.radios_frame
        ToolTip(self.logic_entry_son_1.radios_frame, text="Position dans le mot :\n< début |  milieu  | fin >\n                     uniqu.")
        # Tooltip sur occur_comb
        ToolTip(self.logic_entry_son_1.occur_comb, text="Nombre d'occurrences\ndu son dans le mots")


        #################################################
        #    Configuration du logic_entry 2 --> son
        #################################################

        # Créer une instance "son2" de la classe "matrice"
        self.son2 = Matrice(self.update_entry_2)
        # Instancier la matrice self.son2.matrice_sons dans le cadre "contener_sons"
        self.son2.create_matrice(self.contener_sons)
        # Cacher la matrice self.son2.matrice_sons au démarrage
        self.son2.matrice_sons.pack_forget()

        # Choix disponibles dans la liste
        combo_liste2 = ["", "et", "ou", "sans"]
        # Variable du ComboBox du logic_entry
        self.logic_sons_combo_2_var = ttk.StringVar(value="et")
        # Variable de l'entry du logic_entry
        self.son_2_var = ttk.StringVar(value="")

        # Instanciation de Logic_entry
        self.logic_entry_son_2 = Logic_entry(self.choix_sons,  # Cadre conteneur
                                             self.son2,  # Instance de matrice concernée
                                             "son",
                                             combo_liste2,  # Options disponibles
                                             self.logic_sons_combo_2_var,  # Var dyn véhiculant la valeur du combobox
                                             self.son_2_var,  # Variable dynamique véhiculant la valeur de l'entry
                                             3,
                                             False
                                             )

        # Ne pas afficher au démarrage
        self.logic_entry_son_2.hide_logic_entry()

        # Suivre l'état de la variable dynamique de l'entrée précédente pour faire apparaitre / disparaitre l'instance de logic_entry
        self.logic_entry_son_1.entry_var.trace_add('write',
                                                   lambda name, index, mode,
                                                          inst_ant=self.logic_entry_son_1,
                                                          inst_target=self.logic_entry_son_2:
                                                toggle_logic_entry(inst_ant, inst_target)
                                                   )

        #################################################
        #    Configuration du logic_entry 3 --> son
        #################################################

        # Créer une instance "son2" de la classe "matrice"
        self.son3 = Matrice(self.update_entry_3)
        # Instancier la matrice self.son2.matrice_sons dans le cadre "contener_sons"
        self.son3.create_matrice(self.contener_sons)
        # Cacher la matrice self.son2.matrice_sons au démarrage
        self.son3.matrice_sons.pack_forget()

        # Choix disponibles dans la liste
        combo_liste3 = ["", "et", "ou", "sans"]
        # Variable du ComboBox du logic_entry
        self.logic_sons_combo_3_var = ttk.StringVar(value="et")
        # Variable de l'entry du logic_entry
        self.son_3_var = ttk.StringVar(value="")

        # Instanciation de Logic_entry
        self.logic_entry_son_3 = Logic_entry(self.choix_sons,  # Cadre conteneur
                                             self.son3,  # Instance de matrice concernée
                                             "son",
                                             combo_liste3,  # Options disponibles
                                             self.logic_sons_combo_3_var,  # Var dyn véhiculant la valeur du combobox
                                             self.son_3_var,  # Variable dynamique véhiculant la valeur de l'entry
                                             3,
                                             False
                                             )

        # Ne pas afficher au démarrage
        self.logic_entry_son_3.hide_logic_entry()

        # Suivre l'état de la variable dynamique de l'entrée précédente pour faire apparaitre / disparaitre l'instance de logic_entry
        self.logic_entry_son_2.entry_var.trace_add('write',
                                                   lambda name, index, mode,
                                                          inst_ant=self.logic_entry_son_2,
                                                          inst_target=self.logic_entry_son_3:
                                                   toggle_logic_entry(inst_ant, inst_target)
                                                   )


        #################################################
        #    Configuration du logic_entry 4 --> son
        #################################################

        # Créer une instance "son4" de la classe "matrice"
        self.son4 = Matrice(self.update_entry_4)
        # Instancier la matrice self.son4.matrice_sons dans le cadre "contener_sons"
        self.son4.create_matrice(self.contener_sons)
        # Cacher la matrice self.son4.matrice_sons au démarrage
        self.son4.matrice_sons.pack_forget()

        # Choix disponibles dans la liste
        combo_liste4 = ["", "et", "ou", "sans"]
        # Variable du ComboBox du logic_entry
        self.logic_sons_combo_4_var = ttk.StringVar(value="et")
        # Variable de l'entry du logic_entry
        self.son_4_var = ttk.StringVar(value="")

        # Instanciation de Logic_entry
        self.logic_entry_son_4 = Logic_entry(self.choix_sons,  # Cadre conteneur
                                             self.son4,  # Instance de matrice concernée
                                             "son",
                                             combo_liste4,  # Options disponibles
                                             self.logic_sons_combo_4_var,  # Var dyn véhiculant la valeur du combobox
                                             self.son_4_var,  # Variable dynamique véhiculant la valeur de l'entry
                                             3,
                                             False
                                             )
        # Ne pas afficher au démarrage
        self.logic_entry_son_4.hide_logic_entry()

        # Suivre l'état de la variable dynamique de l'entrée précédente
        self.logic_entry_son_3.entry_var.trace_add('write',
                                                   lambda name, index, mode,
                                                          inst_ant=self.logic_entry_son_3,
                                                          inst_target=self.logic_entry_son_4:
                                                toggle_logic_entry(inst_ant, inst_target)
                                                   )

        ##############################################
        #   Gestion du comportement des radio son
        ##############################################

        sep2 = ttk.Separator(frame_a, bootstyle="primary")
        sep2.pack(anchor="w", fill="x")

        # ---------------------------------------------
        """ Lettres : choix des lettres """

        frame_a3 = ttk.Frame(frame_a, relief='flat')
        frame_a3.pack(anchor="w")

        frame_ltr = ttk.Frame(frame_a3,
                              relief='flat',
                              width=larg_etiq
                              )
        frame_ltr.pack(side='left', padx=(10, 10), pady=(10, 10))

        self.choix_lettres = ttk.Frame(frame_a3)
        self.choix_lettres.pack(side='left', padx=(10, 10), pady=(0, 0))


        source_label = ttk.Label(frame_ltr,
                                 text='Lettres :',
                                 font=("Arial", 15)
                                 )
        source_label.pack()

        # Définir des variables dynamiques pour le checkbox "Lemmes uniquement"
        self.acc_chk_var = tk.BooleanVar(value=False)

        acc_chk = ttk.Checkbutton(frame_ltr,
                                  text='Ign. acc.',
                                  variable=self.acc_chk_var
                                  )
        acc_chk.pack()

        # Tooltip sur lem_chk
        ToolTip(acc_chk, text="Ignorer les accents\nChercher 'e' trouvera\n⟶ 'é', 'è', 'ê', 'ë'")

        #################################################
        #   Configuration du logic_entry 1 --> lettres
        #################################################

        # Choix disponibles dans la liste
        combo_liste_ltr_1 = ["", "avec", "sans"]
        # Variable du ComboBox du logic_entry
        self.logic_ltr_combo_1_var = ttk.StringVar(value="avec")
        # Variable de l'entry du logic_entry
        self.ltr_1_var = ttk.StringVar(value="")

        # Instanciation de Logic_entry
        self.logic_entry_ltr_1 = Logic_entry(self.choix_lettres,  # Cadre conteneur
                                             None,  # Instance de matrice concernée
                                             "ltr",
                                             combo_liste_ltr_1,  # Options disponibles
                                             self.logic_ltr_combo_1_var,
                                             # Variable dynamique véhiculant la valeur du combobox
                                             self.ltr_1_var,  # Variable dynamique véhiculant la valeur de l'entry
                                             7,
                                             True
                                             )

        #################################################
        #   Configuration du logic_entry 2 --> lettres
        #################################################

        # Choix disponibles dans la liste
        combo_liste_ltr_2 = ["", "et", "ou", "sans"]
        # Variable du ComboBox du logic_entry
        self.logic_ltr_combo_2_var = ttk.StringVar(value="et")
        # Variable de l'entry du logic_entry
        self.ltr_2_var = ttk.StringVar(value="")

        # Instanciation de Logic_entry
        self.logic_entry_ltr_2 = Logic_entry(self.choix_lettres,  # Cadre conteneur
                                             None,  # Instance de matrice concernée
                                             "ltr",
                                             combo_liste_ltr_2,  # Options disponibles
                                             self.logic_ltr_combo_2_var,  # Var dyn véhiculant la valeur du combobox
                                             self.ltr_2_var,  # Variable dynamique véhiculant la valeur de l'entry
                                             7,
                                             True
                                             )

        # Ne pas afficher au démarrage
        self.logic_entry_ltr_2.hide_logic_entry()

        # Suivre l'état de la variable dynamique de l'entrée précédente pour faire apparaitre / disparaitre l'instance de logic_entry
        self.logic_entry_ltr_1.entry_var.trace_add('write',
                                               lambda name, index, mode,
                                                      inst_ant=self.logic_entry_ltr_1,
                                                      inst_target=self.logic_entry_ltr_2:
                                               toggle_logic_entry(inst_ant, inst_target)
                                               )

        #################################################
        #   Configuration du logic_entry 3 --> lettres
        #################################################

        # Choix disponibles dans la liste
        combo_liste_ltr_3 = ["", "et", "ou", "sans"]
        # Variable du ComboBox du logic_entry
        self.logic_ltr_combo_3_var = ttk.StringVar(value="et")
        # Variable de l'entry du logic_entry
        self.ltr_3_var = ttk.StringVar(value="")

        # Instanciation de Logic_entry
        self.logic_entry_ltr_3 = Logic_entry(self.choix_lettres,  # Cadre conteneur
                                             None,  # Instance de matrice concernée
                                             "ltr",
                                             combo_liste_ltr_3,  # Options disponibles
                                             self.logic_ltr_combo_3_var,  # Var dyn véhiculant la valeur du combobox
                                             self.ltr_3_var,  # Variable dynamique véhiculant la valeur de l'entry
                                             7,
                                             True
                                             )
        # Ne pas afficher au démarrage
        self.logic_entry_ltr_3.hide_logic_entry()

        # Suivre l'état de la variable dynamique de l'entrée précédente
        self.logic_entry_ltr_2.entry_var.trace_add('write',
                                               lambda name, index, mode,
                                                      inst_ant=self.logic_entry_ltr_2,
                                                      inst_target=self.logic_entry_ltr_3:
                                               toggle_logic_entry(inst_ant, inst_target)
                                               )


        sep3 = ttk.Separator(frame_a, bootstyle="primary")
        sep3.pack(anchor="w", fill="x")

        # ---------------------------------------------
        """ Nombre de syllabes """

        frame_a4 = ttk.Frame(frame_a, relief='flat')
        frame_a4.pack(anchor="w")

        syll_label = ttk.Label(frame_a4,
                               text='Nb. Syll. :',
                               font=("Arial", 15),
                                 width=larg_etiq
                               )
        syll_label.pack(side='left', padx=(10, 0), pady=(10, 10))

        choix_syll = ttk.Frame(frame_a4)
        choix_syll.pack(side='left', padx=(10, 10), pady=(10, 10))

        #################################################
        #   Configuration de l'entrée minimun syllabes
        #################################################

        self.entr_min_syll_var = ttk.IntVar(value=1)
        self.entr_max_syll_var = ttk.IntVar(value=9)

        # ------------------------------------------
        # Validation de MIN et MAX

        # Fonction de validation pour les entrées numériques inférieures
        def validate_min_max(*args):  # *args car l'évènement envoie des arguments
            try:
                min_val = self.entr_min_syll_var.get()
                max_val = self.entr_max_syll_var.get()
                if min_val < max_val:
                    print("Validation réussie !")
                else:
                    self.entr_max_syll_var.set(min_val)     # Remettre la valeur du min dans le max
            except ValueError:
                print("Erreur : Valeurs non entières.")

        # Surveiller les changements des variables entr_min_syll_var et entr_max_syll_var
        self.entr_min_syll_var.trace_add("write", validate_min_max)
        self.entr_max_syll_var.trace_add("write", validate_min_max)


        min_label = ttk.Label(choix_syll,
                               text='Min :',
                               font=("Arial", 11)
                               )
        min_label.pack(side='left', padx=(10, 10), pady=(10, 10))

        self.entr_min_syll = ttk.Combobox(choix_syll,
                                width=10,
                                values=("1","2","3","4","5","6","7","8","9"),
                                textvariable=self.entr_min_syll_var,
                                style="primary.TCombobox",
                                validate = "key",    # Pourquoi ça fonctionne alors que c'est un clic ?
                                validatecommand=validate_min_max
                                )
        self.entr_min_syll.pack(side='left', padx=(5, 5), pady=(5, 5))


        #################################################
        #   Configuration de l'entrée maximum syllabes
        #################################################

        max_label = ttk.Label(choix_syll,
                              text='Max :',
                              font=("Arial", 11)
                              )
        max_label.pack(side='left', padx=(10, 10), pady=(10, 10))

        self.entr_max_syll = ttk.Combobox(choix_syll,
                                width=10,
                                values=("1","2","3","4","5","6","7","8","9"),
                                textvariable=self.entr_max_syll_var,
                                style="primary.TCombobox",
                                validate = "key",    # Pourquoi ça fonctionne alors que c'est un clic ?
                                validatecommand=validate_min_max
                                )
        self.entr_max_syll.pack(side='left', padx=(5, 5), pady=(5, 5))


        sep4 = ttk.Separator(frame_a, bootstyle="primary")
        sep4.pack(anchor="w", fill="x")

        # ---------------------------------------------
        """ Natures : choix de la classe grammaticale """

        frame_a5 = ttk.Frame(frame_a, relief='flat')
        frame_a5.pack(anchor="w")

        nature_label = ttk.Label(frame_a5,
                                 text='Natures :',
                                 font=("Arial", 15),
                                 width=larg_etiq
                                 )
        nature_label.pack(side='left', padx=(10, 10), pady=(10, 10))

        # Définir des variables dynamiques pour chaque nature dans la DB Lexique
        self.nom_var_lex = tk.BooleanVar(value=True)
        self.vb_var_lex = tk.BooleanVar(value=True)
        self.adj_var_lex = tk.BooleanVar(value=True)
        self.adv_var_lex = tk.BooleanVar(value=True)
        self.arti_var_lex = tk.BooleanVar(value=True)
        self.pron_var_lex = tk.BooleanVar(value=True)
        self.conj_var_lex = tk.BooleanVar(value=True)
        self.prep_var_lex = tk.BooleanVar(value=True)
        self.onom_var_lex = tk.BooleanVar(value=False)
        self.pron_var_lex = tk.BooleanVar(value=True)


        choix_nat = ttk.Frame(frame_a5, relief='flat')
        choix_nat.pack(anchor="w")

        choix_nat_a = ttk.Frame(choix_nat, relief='flat')
        choix_nat_a.pack(anchor="w")

        choix_nat_b = ttk.Frame(choix_nat, relief='flat')
        choix_nat_b.pack(anchor="w")

        nom_ckbt_lex = ttk.Checkbutton(choix_nat_a,
                                       text='Nom',
                                       variable=self.nom_var_lex
                                       )

        vb_ckbt_lex = ttk.Checkbutton(choix_nat_a,
                                    text='Verbe',
                                    variable=self.vb_var_lex
                                    )

        adj_ckbt_lex = ttk.Checkbutton(choix_nat_a,
                                    text='Adjectif',
                                    variable=self.adj_var_lex
                                    )

        adv_ckbt_lex = ttk.Checkbutton(choix_nat_a,
                                   text='Adv.',
                                   variable=self.adv_var_lex
                                   )

        art_ckbt_lex = ttk.Checkbutton(choix_nat_a,
                                       text='Article',
                                       variable=self.arti_var_lex
                                       )

        pro_ckbt_lex = ttk.Checkbutton(choix_nat_b,
                                       text='Pronom',
                                       variable=self.pron_var_lex
                                       )

        conj_ckbt_lex = ttk.Checkbutton(choix_nat_b,
                                        text='Conjonc.',
                                        variable=self.conj_var_lex
                                        )

        prep_ckbt_lex = ttk.Checkbutton(choix_nat_b,
                                    text='Prépos.',
                                    variable=self.prep_var_lex
                                    )

        ono_ckbt_lex = ttk.Checkbutton(choix_nat_b,
                                    text='Onom.',
                                    variable=self.onom_var_lex
                                    )

        # Définir des variables dynamiques pour chaque nature dans la DB Minimum Lexical
        self.nom_var_minilex = tk.BooleanVar(value=True)
        self.vb_var_minilex = tk.BooleanVar(value=True)
        self.adj_var_minilex = tk.BooleanVar(value=True)
        self.pttm_var_minilex = tk.BooleanVar(value=True)

        nom_ckbt_minilex = ttk.Checkbutton(choix_nat,
                                       text='Noms',
                                       variable=self.nom_var_minilex
                                       )

        vb_ckbt_minilex = ttk.Checkbutton(choix_nat,
                                      text='Verbes',
                                      variable=self.vb_var_minilex
                                      )

        adj_ckbt_minilex = ttk.Checkbutton(choix_nat,
                                       text='Adjectifs',
                                       variable=self.adj_var_minilex
                                       )

        pttm_ckbt_minilex = ttk.Checkbutton(choix_nat,
                                       text='Petits mots',
                                       variable=self.pttm_var_minilex
                                       )


        sep5 = ttk.Separator(frame_a, bootstyle="primary")
        sep5.pack(anchor="w", fill="x")

        # -------------------------------------------------------------
        """ Genres --> à n'utiliser que pour les noms, adj. et det. """

        frame_a6 = ttk.Frame(frame_a, relief='flat')
        frame_a6.pack(anchor="w")

        genre_label = ttk.Label(frame_a6,
                                 text='Genres :',
                                 font=("Arial", 15),
                                 width=larg_etiq
                                 )
        genre_label.pack(side='left', padx=(10, 10), pady=(10, 10))

        # Définir des variables dynamiques pour chaque case à cocher et les initialiser à True
        self.masc_var = tk.BooleanVar(value=False)
        self.fem_var = tk.BooleanVar(value=False)

        masc_ckbt = ttk.Checkbutton(frame_a6,
                                   text='Masculin',
                                   variable=self.masc_var
                                   )


        fem_ckbt = ttk.Checkbutton(frame_a6,
                                  text='Féminin',
                                  variable=self.fem_var
                                  )

        genre_com_label = ttk.Label(frame_a6,
                                 text='(Si pertinent...)',
                                 font=("Arial", 9),
                                 width=14
                                 )



        sep6 = ttk.Separator(frame_a, bootstyle="primary")
        sep6.pack(anchor="w", fill="x")

        # -------------------------------------------------------------
        """ 15 Thèmes --> Uniquement pour MiniLex 
        
        frame_a70a
        # espace
        # temps
        # maison
        # ecole
        
        frame_a70b
        # nature
        # jardin
        # activ_phy
        # moi_autres
        
        frame_a70c
        # transports
        # cuisine
        # metiers
        # musique
        
        frame_a70d
        # pron_autres
        # maths_raison
        # question
        
        """

        frame_a7 = ttk.Frame(frame_a, relief='flat')
        frame_a7.pack(anchor="w")

        them_label = ttk.Label(frame_a7,
                                 text='Thèmes :',
                                 font=("Arial", 15),
                                 width=larg_etiq
                                 )
        them_label.pack(side='left', padx=(10, 10), pady=(10, 10))



        # Définir des variables dynamiques pour chaque case à cocher et les initialiser à True
        self.espace_var = tk.BooleanVar(value=True)
        self.temps_var = tk.BooleanVar(value=True)
        self.maison_var = tk.BooleanVar(value=True)
        self.ecole_var = tk.BooleanVar(value=True)

        self.nature_var = tk.BooleanVar(value=True)
        self.jardin_var = tk.BooleanVar(value=True)
        self.activ_phy_var = tk.BooleanVar(value=True)
        self.moi_autres_var = tk.BooleanVar(value=True)

        self.transports_var = tk.BooleanVar(value=True)
        self.cuisine_var = tk.BooleanVar(value=True)
        self.metiers_var = tk.BooleanVar(value=True)
        self.musique_var = tk.BooleanVar(value=True)

        self.pron_autres_var = tk.BooleanVar(value=True)
        self.maths_raison_var = tk.BooleanVar(value=True)
        self.question_var = tk.BooleanVar(value=True)

        frame_a70 = ttk.Frame(frame_a7)
        frame_a70a = ttk.Frame(frame_a70)
        frame_a70b = ttk.Frame(frame_a70)
        frame_a70c = ttk.Frame(frame_a70)
        frame_a70d = ttk.Frame(frame_a70)


        # frame_a70a

        espace_ckbt = ttk.Checkbutton(frame_a70a,
                                      text='Espace',
                                      variable=self.espace_var
                                      )

        temps_ckbt = ttk.Checkbutton(frame_a70a,
                                     text='Temps',
                                     variable=self.temps_var
                                     )

        maison_ckbt = ttk.Checkbutton(frame_a70a,
                                      text='Maison',
                                      variable=self.maison_var
                                      )

        ecole_ckbt = ttk.Checkbutton(frame_a70a,
                                     text='École',
                                     variable=self.ecole_var
                                     )

        # frame_a70b

        nature_ckbt = ttk.Checkbutton(frame_a70b,
                                      text='Nature',
                                      variable=self.nature_var
                                      )

        jardin_ckbt = ttk.Checkbutton(frame_a70b,
                                      text='Jardin',
                                      variable=self.jardin_var
                                      )

        activ_phy_ckbt = ttk.Checkbutton(frame_a70b,
                                   text='Act. physique',
                                   variable=self.activ_phy_var
                                   )

        moi_autres_ckbt = ttk.Checkbutton(frame_a70b,
                                          text='Moi & autres',
                                          variable=self.moi_autres_var
                                          )

        # frame_a70c

        transports_ckbt = ttk.Checkbutton(frame_a70c,
                                      text='transports',
                                      variable=self.transports_var
                                      )

        cuisine_ckbt = ttk.Checkbutton(frame_a70c,
                                  text='Cuisine',
                                  variable=self.cuisine_var
                                  )

        metiers_ckbt = ttk.Checkbutton(frame_a70c,
                                      text='Métiers',
                                      variable=self.metiers_var
                                      )

        musique_ckbt = ttk.Checkbutton(frame_a70c,
                                   text='Musique',
                                   variable=self.musique_var
                                   )

        # frame_a70d

        pron_autres_ckbt = ttk.Checkbutton(frame_a70d,
                                       text='Pronoms & autres',
                                       variable=self.pron_autres_var
                                       )

        maths_raison_ckbt = ttk.Checkbutton(frame_a70d,
                                     text='Maths et raison.',
                                     variable=self.maths_raison_var
                                     )

        question_ckbt = ttk.Checkbutton(frame_a70d,
                                            text='Questions',
                                            variable=self.question_var
                                            )


        def show_themes():
            frame_a70.pack(fill='both', expand=True)
            frame_a70a.pack(fill='x', expand=True)
            frame_a70b.pack(fill='x', expand=True)
            frame_a70c.pack(fill='x', expand=True)
            frame_a70d.pack(fill='x', expand=True)

            espace_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))
            temps_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))
            maison_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))
            ecole_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))

            nature_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))
            jardin_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))
            activ_phy_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))
            moi_autres_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))

            transports_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))
            cuisine_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))
            metiers_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))
            musique_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))

            pron_autres_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))
            maths_raison_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))
            question_ckbt.pack(side='left', padx=(10, 10), pady=(5, 5))



        def hide_themes():
            frame_a70.forget()
            frame_a70a.forget()
            frame_a70b.forget()
            frame_a70c.forget()

            espace_ckbt.forget()
            temps_ckbt.forget()
            maison_ckbt.forget()
            ecole_ckbt.forget()

            nature_ckbt.forget()
            jardin_ckbt.forget()
            activ_phy_ckbt.forget()
            moi_autres_ckbt.forget()

            transports_ckbt.forget()
            cuisine_ckbt.forget()
            metiers_ckbt.forget()
            musique_ckbt.forget()

            pron_autres_ckbt.forget()
            musique_ckbt.forget()
            maths_raison_ckbt.forget()


        # show_themes()

        ######################################################
        #    Choix de l'interface "Difficulté" à afficher
        ######################################################

        def show_diff_lexique():
            """ Afficher l'interface pour la db "Lexique" """
            niv1_ckbt.forget()
            niv2_ckbt.forget()
            niv3_ckbt.forget()
            tr_courant_ckbt.pack(side='left', padx=(10, 10), pady=(10, 10))
            courant_ckbt.pack(side='left', padx=(10, 10), pady=(10, 10))
            as_rare_ckbt.pack(side='left', padx=(10, 10), pady=(10, 10))
            rare_ckbt.pack(side='left', padx=(10, 10), pady=(10, 10))

        def show_diff_minilex():
            """ Afficher l'interface pour la db "Minima Lexical" """
            tr_courant_ckbt.forget()
            courant_ckbt.forget()
            as_rare_ckbt.forget()
            rare_ckbt.forget()
            niv1_ckbt.pack(side='left', padx=(10, 10), pady=(10, 10))
            niv2_ckbt.pack(side='left', padx=(10, 10), pady=(10, 10))
            niv3_ckbt.pack(side='left', padx=(10, 10), pady=(10, 10))

        ######################################################
        #    Choix de l'interface "Natures" à afficher
        ######################################################

        def show_natures_lex():
            choix_nat_a.pack(anchor="w")
            choix_nat_b.pack(anchor="w")
            nom_ckbt_lex.pack(side='left', padx=(10, 10), pady=(10, 10))
            vb_ckbt_lex.pack(side='left', padx=(10, 10), pady=(10, 10))
            adj_ckbt_lex.pack(side='left', padx=(10, 10), pady=(10, 10))
            pro_ckbt_lex.pack(side='left', padx=(10, 10), pady=(10, 10))
            conj_ckbt_lex.pack(side='left', padx=(10, 10), pady=(10, 10))
            adv_ckbt_lex.pack(side='left', padx=(10, 10), pady=(10, 10))
            art_ckbt_lex.pack(side='left', padx=(10, 10), pady=(10, 10))
            prep_ckbt_lex.pack(side='left', padx=(10, 10), pady=(10, 10))
            ono_ckbt_lex.pack(side='left', padx=(10, 10), pady=(10, 10))

            nom_ckbt_minilex.pack_forget()
            vb_ckbt_minilex.pack_forget()
            adj_ckbt_minilex.pack_forget()
            pttm_ckbt_minilex.pack_forget()


        def show_natures_minilex():
            choix_nat_a.pack_forget()
            choix_nat_b.pack_forget()
            nom_ckbt_lex.pack_forget()
            vb_ckbt_lex.pack_forget()
            adj_ckbt_lex.pack_forget()
            art_ckbt_lex.pack_forget()
            pro_ckbt_lex.pack_forget()
            conj_ckbt_lex.pack_forget()
            adv_ckbt_lex.pack_forget()
            prep_ckbt_lex.pack_forget()
            ono_ckbt_lex.pack_forget()

            nom_ckbt_minilex.pack(side='left', padx=(10, 10), pady=(10, 10))
            vb_ckbt_minilex.pack(side='left', padx=(10, 10), pady=(10, 10))
            adj_ckbt_minilex.pack(side='left', padx=(10, 10), pady=(10, 10))
            pttm_ckbt_minilex.pack(side='left', padx=(10, 10), pady=(10, 10))

        ######################################
        # Gestion du genre
        ######################################

        def show_genre():
            if not fem_ckbt.winfo_ismapped():
                fem_ckbt.pack(side='left', padx=(10, 10), pady=(10, 10))
            if not masc_ckbt.winfo_ismapped():
                masc_ckbt.pack(side='left', padx=(10, 10), pady=(10, 10))
            if not genre_com_label.winfo_ismapped():
                genre_com_label.pack(side='left', padx=(10, 10), pady=(10, 10))


        def hide_genre():
            if masc_ckbt.winfo_ismapped():
                masc_ckbt.pack_forget()
            if fem_ckbt.winfo_ismapped():
                fem_ckbt.pack_forget()
            if genre_com_label.winfo_ismapped():
                genre_com_label.pack_forget()

        # Si genre possible : True
        self.genre_poss = tk.BooleanVar()

        # Tester si le genre est possible
        def is_genre_possible():

            # True si aucune des cases de la liste n'est cochée
            if self.db_var.get() == "lexique":
                local_genre_poss = not (self.vb_var_lex.get()
                                or self.adv_var_lex.get()
                                or self.arti_var_lex.get()
                                or self.pron_var_lex.get()
                                or self.conj_var_lex.get()
                                or self.prep_var_lex.get()
                                or self.onom_var_lex.get()
                                or self.lem_chk_var.get()      # lem_chk ne doit pas être coché
                                )
                self.genre_poss.set(local_genre_poss)

            if self.db_var.get() == "minilex":
                local_genre_poss = not (self.vb_var_minilex.get()
                                or self.pttm_var_minilex.get()
                                or self.lem_chk_var.get()      # lem_chk ne doit pas être coché
                                )
                self.genre_poss.set(local_genre_poss)


        # Afficher le genre si genre_poss est True
        def gest_genre(*args):

            is_genre_possible()

            if self.genre_poss.get():
                show_genre()
            else:
                hide_genre()

        # Suivre les variables des cases à cocher.
        # Si elles sont True (cochées) ne pas afficher le genre, et ne pas en tenir compte...
        self.vb_var_lex.trace_add("write", gest_genre)
        self.adv_var_lex.trace_add("write", gest_genre)
        self.arti_var_lex.trace_add("write", gest_genre)
        self.pron_var_lex.trace_add("write", gest_genre)
        self.conj_var_lex.trace_add("write", gest_genre)
        self.prep_var_lex.trace_add("write", gest_genre)
        self.onom_var_lex.trace_add("write", gest_genre)

        self.pttm_var_minilex.trace_add("write", gest_genre)
        self.vb_var_minilex.trace_add("write", gest_genre)

        # Ne pas afficher le genre pour les lemmes
        self.lem_chk_var.trace_add('write', gest_genre)


        ######################################
        # Choix de la base de données
        ######################################


        def toggle_db(*args):
            """ Afficher la bonne interface """
            if self.db_var.get() == "lexique":
                show_diff_lexique()
                hide_themes()
                show_lem_chk()
                show_natures_lex()
            else :
                show_diff_minilex()
                show_themes()
                hide_lem_chk()
                show_natures_minilex()

        # Afficher au démarrage l'interface par défaut
        toggle_db()

        # Surveiller les changements de db_var pour ajuster l'interface
        self.db_var.trace_add("write", toggle_db)


        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #      Colonne de droite
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        self.frame_b0 = ttk.Frame(frame_b,
                                  bootstyle = "light"
                                  )
        self.frame_b0.pack(padx=(20, 20),
                           pady=(0, 10),
                           expand=True,
                           fill="both"
                           )

        self.data_columns = [
            {"text": "n°", "stretch": False, "width": 60},
            {"text": "Mots trouvés", "stretch": True}
        ]

        self.data_list = [
            ("1", "...")
        ]

        self.make_data_tableview(self.data_columns, self.data_list)

        result_nb_frame = tk.Frame(frame_b)
        result_nb_frame.pack(expand=True, fill="both")

        # Sous-frame pour aligner et centrer les widgets
        center_frame = tk.Frame(result_nb_frame)
        center_frame.pack(expand=True)

        self.total_var = tk.IntVar(value=0)

        mots_label = ttk.Label(center_frame,
                                 text='Total : ',
                                 font=("Arial", 12)
                                 )
        mots_label.pack(side="left", padx=(5, 0))

        nb_mots_label = ttk.Label(center_frame,
                               textvariable=self.total_var,
                               font=("Arial", 12)
                               )
        nb_mots_label.pack(side="left", padx=(5, 0))

        mots_label = ttk.Label(center_frame,
                                text=' mots',
                                font=("Arial", 12)
                                )
        mots_label.pack(side="left", padx=(5, 0))


        frame_b1 = ttk.Frame(frame_a, relief='flat')
        frame_b1.pack(anchor="center", expand=True, fill="both")

        self.cherch_but = ttk.Button(frame_b,
                                text="Rechercher"
                                )
        self.cherch_but.pack(side='left',
                        anchor="center", expand=True, fill="x",
                        padx=(30, 15),
                        pady=(10, 20)
                        )

        self.copier_but = ttk.Button(frame_b,
                                text="Copier la liste"
                                )
        self.copier_but.pack(side='left',
                        anchor="center", expand=True, fill="x",
                        padx=(15, 30),
                        pady=(10, 20)
                         )

        # Tooltip sur lem_chk
        ToolTip(self.copier_but, text="Double-cliquez sur un mot\npour ne copier que lui.")


        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #     Instanciation des matrices de sons
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        # Créer une instance "son3" de la classe "matrice"
        self.son3 = Matrice(self.update_entry_3)
        # Instancier la matrice self.son3.matrice_sons dans le cadre "contener_sons"
        self.son3.create_matrice(self.contener_sons)
        # Cacher la matrice self.son3.matrice_sons au démarrage
        self.son3.matrice_sons.pack_forget()


        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #     Écoute des événements
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        def show_matrice_cond(event, sonx, logic_entry_x):
            # Ne faire apparaître les matrices que si l'entry est 'normal'
            if str(logic_entry_x.cget('state')) == 'normal':
                self.show_matrice(event, sonx, self.liste_instances)


        # Associer toute la fenêtre (et ses enfants) à hide_matrice avec un clic souris.
        self.root.bind("<Button-1>", self.hide_matrice)
        # Associer logic_entry_1.entr_choice à show_matrice avec un clic souris.
        self.logic_entry_son_1.entr_choice.bind("<Button-1>", lambda event: show_matrice_cond(event, self.son1, self.logic_entry_son_1.entr_choice))
        # Associer logic_entry_2.entr_choice à show_matrice avec un clic souris.
        self.logic_entry_son_2.entr_choice.bind("<Button-1>", lambda event: show_matrice_cond(event, self.son2, self.logic_entry_son_2.entr_choice))
        # Associer logic_entry_3.entr_choice à show_matrice avec un clic souris.
        self.logic_entry_son_3.entr_choice.bind("<Button-1>", lambda event: show_matrice_cond(event, self.son3, self.logic_entry_son_3.entr_choice))
        # Associer logic_entry_4.entr_choice à show_matrice avec un clic souris.
        self.logic_entry_son_4.entr_choice.bind("<Button-1>", lambda event: show_matrice_cond(event, self.son4, self.logic_entry_son_4.entr_choice))

        # Liste des instances possibles pour escamoter toutes les matrices_sons sauf celle à afficher
        self.liste_instances = [self.son1, self.son2, self.son3, self.son4]

        ###########################################################################
        #       Définition des fonctions de suivi des variables dynamiques
        #       des boutons radio des sons et des lettres
        ###########################################################################

        """
        Beaucoup de redondances. J'ai essayé de factoriser, mais j'ai perdu
        beaucoup de temps alors je laisse comme ça pour le moment
        """

        # Pour mémoriser la valeur des sons (pour toggle)
        self.previous_value_son_1 = ''
        self.previous_value_son_2 = ''
        self.previous_value_son_3 = ''
        self.previous_value_son_4 = ''

        # Pour mémoriser la valeur des lettres (pour toggle)
        self.previous_value_ltr_1 = ''
        self.previous_value_ltr_2 = ''
        self.previous_value_ltr_3 = ''


        # --> Factoriser toggle_son_x ??? (pas réussi...)
        # Fonctions pour basculer les boutons radio des sons
        def toggle_son_1():
            # Vérifier si le bouton cliqué est déjà sélectionné
            current_value = self.logic_entry_son_1.radio_var.get()
            if current_value == self.previous_value_son_1:
                self.logic_entry_son_1.radio_var.set('')  # Décoche le bouton radio
                self.previous_value_son_1 = ''
            else:
                self.previous_value_son_1 = current_value  # Stocke la dernière valeur sélectionnée

        def toggle_son_2():
            # Vérifier si le bouton cliqué est déjà sélectionné
            current_value = self.logic_entry_son_2.radio_var.get()
            if current_value == self.previous_value_son_2:
                self.logic_entry_son_2.radio_var.set('')  # Décoche le bouton radio
                self.previous_value_son_2 = ''
            else:
                self.previous_value_son_2 = current_value  # Stocke la dernière valeur sélectionnée

        def toggle_son_3():
            # Vérifier si le bouton cliqué est déjà sélectionné
            current_value = self.logic_entry_son_3.radio_var.get()
            if current_value == self.previous_value_son_3:
                self.logic_entry_son_3.radio_var.set('')  # Décoche le bouton radio
                self.previous_value_son_3 = ''
            else:
                self.previous_value_son_3 = current_value  # Stocke la dernière valeur sélectionnée

        def toggle_son_4():
            # Vérifier si le bouton cliqué est déjà sélectionné
            current_value = self.logic_entry_son_4.radio_var.get()
            if current_value == self.previous_value_son_4:
                self.logic_entry_son_4.radio_var.set('')  # Décoche le bouton radio
                self.previous_value_son_4 = ''
            else:
                self.previous_value_son_4 = current_value  # Stocke la dernière valeur sélectionnée

        # Fonctions pour basculer les boutons radio des lettres
        def toggle_ltr_1():
            # Vérifier si le bouton cliqué est déjà sélectionné
            current_value = self.logic_entry_ltr_1.radio_var.get()
            if current_value == self.previous_value_ltr_1:
                self.logic_entry_ltr_1.radio_var.set('')  # Décoche le bouton radio
                self.previous_value_ltr_1 = ''
            else:
                self.previous_value_ltr_1 = current_value  # Stocke la dernière valeur sélectionnée

        def toggle_ltr_2():
            # Vérifier si le bouton cliqué est déjà sélectionné
            current_value = self.logic_entry_ltr_2.radio_var.get()
            if current_value == self.previous_value_ltr_2:
                self.logic_entry_ltr_2.radio_var.set('')  # Décoche le bouton radio
                self.previous_value_ltr_2 = ''
            else:
                self.previous_value_ltr_2 = current_value  # Stocke la dernière valeur sélectionnée

        def toggle_ltr_3():
            # Vérifier si le bouton cliqué est déjà sélectionné
            current_value = self.logic_entry_ltr_3.radio_var.get()
            if current_value == self.previous_value_ltr_3:
                self.logic_entry_ltr_3.radio_var.set('')  # Décoche le bouton radio
                self.previous_value_ltr_3 = ''
            else:
                self.previous_value_ltr_3 = current_value  # Stocke la dernière valeur sélectionnée


        # Fonction pour changer le style des radio
        def appliquer_style_radio(widget, style):
            """
            Applique un style à tous les boutons radio contenus dans un widget,
            y compris les sous-widgets (récursif).

            Args:
                widget: Le widget à partir duquel appliquer le style.
                style: Le style à appliquer (par exemple, "primary.Radiobutton").
            """
            for enfant in widget.winfo_children():
                if isinstance(enfant, ttk.Radiobutton):
                    enfant.configure(bootstyle=style)  # Applique le style
                appliquer_style_radio(enfant, style)  # Appel récursif pour les enfants


        def is_same_pos_sons(*args):
            # Liste des valeurs prises par les radio son
            radio_pos_list_sons = [self.logic_entry_son_1.radio_var.get(),
                             self.logic_entry_son_2.radio_var.get(),
                            self.logic_entry_son_3.radio_var.get(),
                             self.logic_entry_son_4.radio_var.get()
                             ]

            # Booléen pour vérifier s'il y plus d'un "deb" ou plus d'un "mil" ou plus d'un "fin" dans la liste
            is_sup_one = ((radio_pos_list_sons.count("deb") > 1)
                        or (radio_pos_list_sons.count("mil") > 1)
                        or (radio_pos_list_sons.count("fin") > 1))

            if is_sup_one:
                # print("Au moins deux positions identiques")
                appliquer_style_radio(self.choix_sons, "danger")
            else:
                # print("Aucune position identique")
                appliquer_style_radio(self.choix_sons, "primary")

        def is_same_pos_ltrs(*args):
            # Liste des valeurs prises par les radio son
            radio_pos_list_ltrs = [self.logic_entry_ltr_1.radio_var.get(),
                             self.logic_entry_ltr_2.radio_var.get(),
                            self.logic_entry_ltr_3.radio_var.get()
                                   ]

            # Booléen pour vérifier s'il y plus d'un "deb" ou plus d'un "mil" ou plus d'un "fin" dans la liste
            is_sup_one = ((radio_pos_list_ltrs.count("deb") > 1)
                        or (radio_pos_list_ltrs.count("mil") > 1)
                        or (radio_pos_list_ltrs.count("fin") > 1))

            if is_sup_one:
                # print("Au moins deux positions identiques")
                appliquer_style_radio(self.choix_lettres, "danger")
            else:
                # print("Aucune position identique")
                appliquer_style_radio(self.choix_lettres, "primary")


        # Pour lancer en même temps la fonction pour basculer les boutons
        # et celle qui change le style en cas de doublon de position
        def chg_radio_son_1(*args):
            toggle_son_1()
            is_same_pos_sons()

        def chg_radio_son_2(*args):
            toggle_son_2()
            is_same_pos_sons()

        def chg_radio_son_3(*args):
            toggle_son_3()
            is_same_pos_sons()

        def chg_radio_son_4(*args):
            toggle_son_4()
            is_same_pos_sons()

        def chg_radio_ltr_1(*args):
            toggle_ltr_1()
            is_same_pos_ltrs()

        def chg_radio_ltr_2(*args):
            toggle_ltr_2()
            is_same_pos_ltrs()

        def chg_radio_ltr_3(*args):
            toggle_ltr_3()
            is_same_pos_ltrs()

        # Suivi de la variable dynamique radio_var de chacune des instances
        self.logic_entry_son_1.radio_var.trace_add("write", chg_radio_son_1)
        self.logic_entry_son_2.radio_var.trace_add("write", chg_radio_son_2)
        self.logic_entry_son_3.radio_var.trace_add("write", chg_radio_son_3)
        self.logic_entry_son_4.radio_var.trace_add("write", chg_radio_son_4)

        self.logic_entry_ltr_1.radio_var.trace_add("write", chg_radio_ltr_1)
        self.logic_entry_ltr_2.radio_var.trace_add("write", chg_radio_ltr_2)
        self.logic_entry_ltr_3.radio_var.trace_add("write", chg_radio_ltr_3)

    ###############################################################
    #       Définition des fonctions lancées par les bind
    ###############################################################

    def show_matrice(self, event, son, liste):
        """ Afficher "matrice_sons" """
        # print("Demande d'affichage de la matrice effectuée")
        # Effacer toutes les instances
        for instance in liste:
            instance.matrice_sons.pack_forget()

        # Afficher l'instance demandée
        son.matrice_sons.pack(side='left', padx=10, pady=10)

        return "break" # Ne pas propager l'événement --> la fonction ne transmet pas l'événement à root
        # Sinon, <Button-1> sur l'entry est aussi reçu par root et les deux bind sont activés.


    def hide_matrice(self, event):
        """ Escamoter toutes les "matrice_sons" sauf si le widget cliqué appartient à une matrice_sons """
        # print("Demande d'escamotage de la matrice effectuée.")

        # Obtenir le widget qui a déclenché l'événement
        widget = event.widget

        # Parcourir la hiérarchie des parents du widget cliqué (jusqu'au parent principal : root)
        # --> ne pas exécuter .pack_forget() si le widget appartient à "matrice_sons"
        while widget != self.root:
            if ((widget == self.son1.matrice_sons)
                    or (widget == self.son2.matrice_sons)
                    or (widget == self.son3.matrice_sons)
                    or (widget == self.son4.matrice_sons)
            ):
                # print("Escamotage non réalisé !")
                return  # Arrêter "hide_matrice()" si le widget a pour parent "matrice_sons"
            widget = widget.master  # Passer au parent supérieur

        if self.son1.matrice_sons.winfo_ismapped():
            self.son1.matrice_sons.pack_forget()
        if self.son2.matrice_sons.winfo_ismapped():
            self.son2.matrice_sons.pack_forget()
        if self.son3.matrice_sons.winfo_ismapped():
            self.son3.matrice_sons.pack_forget()
        if self.son4.matrice_sons.winfo_ismapped():
            self.son4.matrice_sons.pack_forget()

    # Fonction pour mettre à jour l'entry avec la variable correspondant à la case cachée.
    # Elle sera passée en paramètre lors de l'instanciation de la classe "matrice"
    # Afin de pouvoir être exécutée depuis l'instance "son1"
    def update_entry_1(self, *args):
        value = self.son1.radio_groupe.get()  # Récupérer la valeur sélectionnée
        if value:
            self.logic_entry_son_1.entr_choice.delete(0, tk.END)
            self.logic_entry_son_1.entr_choice.insert(0, value)

    def update_entry_2(self, *args):
        value = self.son2.radio_groupe.get()  # Récupérer la valeur sélectionnée
        if value:
            self.logic_entry_son_2.entr_choice.delete(0, tk.END)
            self.logic_entry_son_2.entr_choice.insert(0, value)

    def update_entry_3(self, *args):
        value = self.son3.radio_groupe.get()  # Récupérer la valeur sélectionnée
        if value:
            self.logic_entry_son_3.entr_choice.delete(0, tk.END)
            self.logic_entry_son_3.entr_choice.insert(0, value)

    def update_entry_4(self, *args):
        value = self.son4.radio_groupe.get()  # Récupérer la valeur sélectionnée
        if value:
            self.logic_entry_son_4.entr_choice.delete(0, tk.END)
            self.logic_entry_son_4.entr_choice.insert(0, value)

    def make_data_tableview(self, dat_col, dat_list):
        # Créer l'instance du tableau
        # Initialiser le Tableview_interact sans données au démarrage

        self.data_tableview = Tableview_interact(self.frame_b0, dat_col, dat_list)
        self.data_tableview.pack(fill=BOTH, expand=True)

    # Servira pour afficher la réponse dans la liste de réponses --> à implémenter
    # def display_data(self, data):
    #     print(f"Info : {data['message']}")

    ##################################################################
    #     Exposition des variables dynamiques vers le controller
    ##################################################################

    @property
    def get_data(self):
        """ Récupération des valeurs de l'interface
            mises à disposition du controller
        """
        dico_data = {
            "choosen_db" : self.db_var.get(),
            "lem_uniq" : self.lem_chk_var.get(),

            # La difficulté "Lexique"
            "tr_courant" : self.tr_courant_var.get(),
            "courant" : self.courant_var.get(),
            "as_rare" : self.as_rare_var.get(),
            "rare" : self.rare_var.get(),

            # La difficulté "MiniLex"
            "niv_1": self.niv1_var.get(),
            "niv_2": self.niv2_var.get(),
            "niv_3": self.niv3_var.get(),

            # Les sons
            "logic_son_1" : self.logic_sons_combo_1_var.get(),
            "son_1" : self.son_1_var.get(),
            "son_1_pos" : self.logic_entry_son_1.radio_var.get(),
            "qqt_son_1" : self.logic_entry_son_1.occur_comb_var.get(),

            "logic_son_2": self.logic_sons_combo_2_var.get(),
            "son_2": self.son_2_var.get(),
            "son_2_pos": self.logic_entry_son_2.radio_var.get(),
            "qqt_son_2": self.logic_entry_son_2.occur_comb_var.get(),

            "logic_son_3": self.logic_sons_combo_3_var.get(),
            "son_3": self.son_3_var.get(),
            "son_3_pos": self.logic_entry_son_3.radio_var.get(),
            "qqt_son_3": self.logic_entry_son_3.occur_comb_var.get(),

            "logic_son_4": self.logic_sons_combo_4_var.get(),
            "son_4": self.son_4_var.get(),
            "son_4_pos": self.logic_entry_son_4.radio_var.get(),
            "qqt_son_4": self.logic_entry_son_4.occur_comb_var.get(),

            # Les lettres
            "ign_acc" : self.acc_chk_var.get(),

            "logic_ltr_1" : self.logic_ltr_combo_1_var.get(),
            "ltr_1" : self.ltr_1_var.get(),
            "ltr_1_pos": self.logic_entry_ltr_1.radio_var.get(),
            "qqt_ltr_1": self.logic_entry_ltr_1.occur_comb_var.get(),

            "logic_ltr_2": self.logic_ltr_combo_2_var.get(),
            "ltr_2": self.ltr_2_var.get(),
            "ltr_2_pos": self.logic_entry_ltr_2.radio_var.get(),
            "qqt_ltr_2": self.logic_entry_ltr_2.occur_comb_var.get(),

            "logic_ltr_3": self.logic_ltr_combo_3_var.get(),
            "ltr_3": self.ltr_3_var.get(),
            "ltr_3_pos": self.logic_entry_ltr_3.radio_var.get(),
            "qqt_ltr_3": self.logic_entry_ltr_3.occur_comb_var.get(),

            # Nombre de syllabes
            "min_syll" : self.entr_min_syll_var.get(),
            "max_syll" : self.entr_max_syll_var.get(),

            # Natures de Lexique
            "nom_lex" : self.nom_var_lex.get(),
            "vb_lex" : self.vb_var_lex.get(),
            "adj_lex" : self.adj_var_lex.get(),
            "adv_lex" : self.adv_var_lex.get(),
            "arti_lex" : self.arti_var_lex.get(),
            "pron_lex" : self.pron_var_lex.get(),
            "conj_lex" : self.conj_var_lex.get(),
            "prep_lex" : self.prep_var_lex.get(),
            "onom_lex" : self.onom_var_lex.get(),

            # Natures de Minima Lexical
            "nom_minilex": self.nom_var_minilex.get(),
            "vb_minilex": self.vb_var_minilex.get(),
            "adj_minilex": self.adj_var_minilex.get(),
            "pttm_minilex": self.pttm_var_minilex.get(),

            # Genre
            "masc" : self.masc_var.get(),
            "fem" : self.fem_var.get(),
            "genre_poss" : self.genre_poss.get(),

            # Thème (MiniLex)
            "espace": self.espace_var.get(),
            "temps" : self.temps_var.get(),
            "maison" : self.maison_var.get(),
            "ecole" : self.ecole_var.get(),

            "nature" : self.nature_var.get(),
            "jardin" : self.jardin_var.get(),
            "activ_phy" : self.activ_phy_var.get(),
            "moi_autres" : self.moi_autres_var.get(),

            "transports" : self.transports_var.get(),
            "cuisine" : self.cuisine_var.get(),
            "metiers" : self.metiers_var.get(),
            "musique" : self.musique_var.get(),

            "pron_autres" : self.pron_autres_var.get(),
            "maths_raison" : self.maths_raison_var.get(),
            "question": self.question_var.get()

        }
        # Renvoie vers le Controller
        return dico_data





    ###################################################################################
    # Méthode pour lancer l'appli :
    # --> On peut l'étendre plus tard sans modifier main.py
    # --> En POO, les classes doivent encapsuler leurs propres comportements
    ###################################################################################

    def run(self):
        self.root.mainloop()






if __name__ == "__main__":

    phono_search_go = FormView()

    # Démarrer l'application avec le root.mainloop() de la méthode run
    try:
        # Démarrer l'application avec le root.mainloop() de la méthode run
        phono_search_go.run()
    except:
        print("ERROR")
    finally:
        pass
        # Fermer la connexion à la base de données lorsque l'application se termine
        # Toujours exécuté, pour libérer des ressources comme les connexions à la base de données.
        # app.mill.db.close()
