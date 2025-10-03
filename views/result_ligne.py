import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Result_ligne(ttk.Frame):
    def __init__(self, found_word, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.found_word = found_word

        # Case à cocher
        self.checkbox_var = tk.BooleanVar()
        self.checkbox = ttk.Checkbutton(self,
                                        text="",
                                        variable=self.checkbox_var
                                        )
        self.checkbox.pack(side=LEFT, padx=5, pady=0)

        # Bouton
        self.bouton = ttk.Button(self,
                                 text=self.found_word,
                                 command=self.bouton_clique,
                                 bootstyle="dark-link"
                                 )
        self.bouton.pack(side=LEFT, padx=5, pady=0)

    def bouton_clique(self):
        if self.checkbox_var.get():
            print("Case cochée et bouton cliqué !")
        else:
            print("Bouton cliqué !")

if __name__ == "__main__":
    # Exemple d'utilisation
    fenetre = ttk.Window("Exemple", "litera")
    checkbox_bouton = Result_ligne("Mot trouvé", fenetre)
    checkbox_bouton.pack(padx=20, pady=20)

    fenetre.mainloop()