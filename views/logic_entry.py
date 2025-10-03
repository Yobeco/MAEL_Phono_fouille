import ttkbootstrap as ttk
import tkinter as tk

# Pour valider les entrées de lettres
import re

#################################################
#   Class pour créer un duo ComboBox + entry
#################################################
class Logic_entry:
    def __init__(self, container,
                 matr_inst,
                 log_entr_type,  # "son" / "ltr"
                 combo_list,
                 combo_var,
                 entry_var,
                 entry_w,
                 entry_valid=False
                 ):

        self.container = container          # Cadre où instancier
        self.matr_inst = matr_inst          # Matrice concernée
        self.logic_entry_type = log_entr_type  # Type de Logic_entry (son ou ltr)
        self.combo_list = combo_list        # Liste disponible dans le combobox
        self.combo_var = combo_var          # Variable dynamique associée au Combobox
        self.entry_var = entry_var          # Variable dynamique associée à l'Entry
        self.entry_w = entry_w              # Largeur de l'entrée (en chr)
        self.entry_valid = entry_valid      # True : active la validation (lettres seulement) False par défaut

        self.occur_comb_var = ttk.StringVar(value="1")
        self.radio_var = tk.StringVar()     # Variable dynamique du groupe des 3 boutons radio

        # Cadre qui contiendra le Combobox, l'Entry puis les boutons radio
        self.logic_entry_frame = ttk.Frame(self.container)


        # Cadre pour les entrées du haut : Combobox et Entry
        self.entrys_frame = ttk.Frame(self.logic_entry_frame)


        # Cadre pour les boutons radio du bas
        self.radios_frame = ttk.Frame(self.logic_entry_frame)


        #################################################
        #    Création du Combobox
        #################################################

        self.logic_combo = ttk.Combobox(self.entrys_frame,
                                        values=self.combo_list,  # Liste des valeurs disponibles
                                        textvariable=self.combo_var,  # Variable dynamique affectée
                                        width=4,
                                        style='primary.TCombobox'
                                        )


        ########################################################
        #    Création de l'entrée de texte (son ou lettres)
        ########################################################

        # Fonction de validation pour restreindre les entrées aux lettres
        def validate_entry(content):
            pattern = re.compile(r"^[a-zA-ZÀ-ÿ]*$")  # Regex pour les lettres minuscules et majuscules
            return pattern.match(content) is not None

        # Enregistrer la fonction de validation --> je ne comprends pas bien...
        validate_command = self.container.register(validate_entry)

        # Filtrer si self.entry_val == True
        if self.entry_valid == True:
            self.entr_choice = ttk.Entry(self.entrys_frame,
                                         textvariable=self.entry_var,  # Valeur affectée
                                         width=self.entry_w,
                                         style='primary.TEntry',
                                         validate = "key",  # Lancer la validation lorsqu'on presse une touche
                                         validatecommand=(validate_command, "%P") # %P représente ce que contiendrait le widget Entry si la frappe ou l'édition en cours était acceptée.
                                         )
        else :
            self.entr_choice = ttk.Entry(self.entrys_frame,
                                         textvariable=self.entry_var,  # Valeur affectée
                                         width=self.entry_w,
                                         style='primary.TEntry',
                                         )


        # Configurer le texte en Bold le texte dans l'entry
        self.entr_choice.configure(font=('TkDefaultFont', 12, 'bold'))
        # Modification de la couleur du texte en bleu
        self.entr_choice.configure(foreground='blue')  # Ou fg='blue'

        # L'entrée de texte est désactivée si le combobox précédent est nul
        def change_state_entry(*args):
            if self.combo_var.get():  # Si la variable n'est' pas nulle
                self.entr_choice.configure(state='normal', style="primary.TEntry")
            else:  # Si la variable est nulle
                self.entry_var.set("")
                self.entr_choice.configure(state='disabled', style="secondary.TEntry")

        # Lancer la fonction au démarrage
        change_state_entry()

        # Suivre l'état des variables dynamiques pour relancer la fonction
        self.combo_var.trace_add('write', change_state_entry)

        ########################################################
        #    Création du label du nombre d'occurrences
        ########################################################

        self.occur_comb = ttk.Combobox(self.entrys_frame,
                                  values=["1", "2", "3"],          # Liste des valeurs disponibles
                                  textvariable=self.occur_comb_var,     # Variable dynamique affectée
                                  width=1,
                                  style='primary.TCombobox'
                                  )



        #################################################
        #    Création des boutons radio de position
        #################################################

        """
        Un son ou une lettre ne peut pas être à la fois en 1ère, 2ème ou 3ème position
        Idée général pour qu'un seul radio ne soit coché par instance :
        1- Utiliser un dictionnaire pour suivre l'état des radio.
        2- Si une autre case est déjà True dans cette instance, passer à False les valeurs des radio que je ne suis pas en train de cocher
        """

        self.deb_label = ttk.Label(self.radios_frame,
                                   text="< "
                                   )


        self.deb_radio = ttk.Radiobutton(self.radios_frame,
                                         variable=self.radio_var,
                                         value="deb",     # value différente en fonction de l'instance
                                         command=None,
                                         bootstyle = "primary"
                                         )


        self.mil_radio = ttk.Radiobutton(self.radios_frame,
                                           variable=self.radio_var,
                                           value="mil",
                                           command=None,
                                           bootstyle = "primary"
                                           )


        self.fin_radio = ttk.Radiobutton(self.radios_frame,
                                         variable=self.radio_var,
                                         value="fin",
                                         command=None,
                                         bootstyle = "primary"
                                         )


        self.fin_label = ttk.Label(self.radios_frame,
                                   text=">"
                                   )

        # Pour afficher une instance de Logic_entry au démarrage
        self.show_logic_entry()

        # Suivi de la valeur de occur_comb_var --> désactiver les boutons radio si > 1
        def desactiv_radio(*args):
            if int(self.occur_comb_var.get()) > 1:
                self.radio_var.set("")
                self.deb_radio.configure(state='disabled', style="secondary.TRadiobutton")
                self.mil_radio.configure(state='disabled', style="secondary.TRadiobutton")
                self.fin_radio.configure(state='disabled', style="secondary.TRadiobutton")
            else:
                self.deb_radio.configure(state='normal', style="primary.TRadiobutton")
                self.mil_radio.configure(state='normal', style="primary.TRadiobutton")
                self.fin_radio.configure(state='normal', style="primary.TRadiobutton")

        self.occur_comb_var.trace_add("write", desactiv_radio)


    # Fonction pour afficher Logic_Entry
    def show_logic_entry(self):
        self.logic_entry_frame.pack(side="left")
        self.entrys_frame.pack()
        self.radios_frame.pack()
        self.logic_combo.pack(side='left', padx=(7, 2), pady=(5, 5))
        self.entr_choice.pack(side='left', padx=(2, 2), pady=(5, 5))
        self.occur_comb.pack(padx=(2, 7), pady=(0, 0), side='left')
        self.deb_label.pack(side='left')
        self.deb_radio.pack(side='left')
        self.mil_radio.pack(side='left')
        self.fin_radio.pack(side='left')
        self.fin_label.pack(side='left')


    def hide_logic_entry(self):
        self.logic_entry_frame.pack_forget()
        self.entrys_frame.pack_forget()
        self.radios_frame.pack_forget()
        self.logic_combo.pack_forget()
        self.entr_choice.pack_forget()
        self.occur_comb.pack_forget()
        self.deb_label.pack_forget()
        self.deb_radio.pack_forget()
        self.mil_radio.pack_forget()
        self.fin_radio.pack_forget()
        self.fin_label.pack_forget()






if __name__ == "__main__":
    root = ttk.Window()

    root.mainloop()