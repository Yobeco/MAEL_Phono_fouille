import ttkbootstrap as ttk
import tkinter as tk

class Matrice:
    def __init__(self, callback=None):
        # Variable dynamique du groupe des boutons radio
        self.radio_groupe = tk.StringVar(value="")

        # Fonction qui sera celle entrée en paramètre lors de l'instanciation de la classe "matrice"
        # --> self.callback devient la fonction "update_entry()" envoyée en paramètre dans l'instanciation de la classe matrice
        self.callback = callback
        self.radio_groupe.trace_add('write', self.callback)


        # Frame 'matrice_sons' déclaré comme attribut de classe pour pouvoir être manipulé
        # self.matrice_sons = None

        # Méthode pour créer / re-créer la matrice de checks
    def create_matrice(self, container):

        self.matrice_sons = ttk.Frame(container)
        self.matrice_sons.pack()

        matrice_cons = ttk.Frame(self.matrice_sons,
                                 relief='ridge',
                                 borderwidth=5,
                                 padding="7 7 7 7"
                                 )
        matrice_cons.pack(padx=(10, 10),
                          pady=(0, 10),
                          anchor="w"
                          )

        cons_titre = ttk.Label(matrice_cons,
                               text='17 consonnes :',
                               font=("Calibri", 15, "bold")
                               )
        cons_titre.grid(row=0, column=0, padx=(10, 10), pady=(0, 3), columnspan=4, sticky="ew")

        b_ckbt = ttk.Radiobutton(matrice_cons, text='[b] ballon', variable=self.radio_groupe, value="[b]")
        b_ckbt.grid(row=1, column=0, padx=(10, 10), pady=(3, 3), sticky="w")

        d_ckbt = ttk.Radiobutton(matrice_cons, text='[d] dé', variable=self.radio_groupe, value="[d]")
        d_ckbt.grid(row=1, column=1, padx=(10, 10), pady=(3, 3), sticky="w")

        f_ckbt = ttk.Radiobutton(matrice_cons, text='[f] famille', variable=self.radio_groupe, value="[f]")
        f_ckbt.grid(row=1, column=2, padx=(10, 10), pady=(3, 3), sticky="w")

        k_ckbt = ttk.Radiobutton(matrice_cons, text='[k] cabane', variable=self.radio_groupe, value="[k]")
        k_ckbt.grid(row=1, column=3, padx=(10, 10), pady=(3, 3), sticky="w")

        l_ckbt = ttk.Radiobutton(matrice_cons, text='[l] lion', variable=self.radio_groupe, value="[l]")
        l_ckbt.grid(row=2, column=0, padx=(10, 10), pady=(3, 3), sticky="w")

        m_ckbt = ttk.Radiobutton(matrice_cons, text='[m] mot', variable=self.radio_groupe, value="[m]")
        m_ckbt.grid(row=2, column=1, padx=(10, 10), pady=(3, 3), sticky="w")

        n_ckbt = ttk.Radiobutton(matrice_cons, text='[n] noir', variable=self.radio_groupe, value="[n]")
        n_ckbt.grid(row=2, column=2, padx=(10, 10), pady=(3, 3), sticky="w")

        p_ckbt = ttk.Radiobutton(matrice_cons, text='[p] panda', variable=self.radio_groupe, value="[p]")
        p_ckbt.grid(row=2, column=3, padx=(10, 10), pady=(3, 3), sticky="w")

        s_ckbt = ttk.Radiobutton(matrice_cons, text='[s] sac', variable=self.radio_groupe, value="[s]")
        s_ckbt.grid(row=3, column=0, padx=(10, 10), pady=(3, 3), sticky="w")

        t_ckbt = ttk.Radiobutton(matrice_cons, text='[t] table', variable=self.radio_groupe, value="[t]")
        t_ckbt.grid(row=3, column=1, padx=(10, 10), pady=(3, 3), sticky="w")

        g_ckbt = ttk.Radiobutton(matrice_cons, text='[g] garçon', variable=self.radio_groupe, value="[g]")
        g_ckbt.grid(row=3, column=2, padx=(10, 10), pady=(3, 3), sticky="w")

        gn_ckbt = ttk.Radiobutton(matrice_cons, text='[ɲ] gagner', variable=self.radio_groupe, value="[ɲ]")
        gn_ckbt.grid(row=3, column=3, padx=(10, 10), pady=(3, 3), sticky="w")

        j_ckbt = ttk.Radiobutton(matrice_cons, text='[ʒ] jardin', variable=self.radio_groupe, value="[ʒ]")
        j_ckbt.grid(row=4, column=0, padx=(10, 10), pady=(3, 3), sticky="w")

        r_ckbt = ttk.Radiobutton(matrice_cons, text='[ʁ] roi', variable=self.radio_groupe, value="[ʁ]")
        r_ckbt.grid(row=4, column=1, padx=(10, 10), pady=(3, 3), sticky="w")

        v_ckbt = ttk.Radiobutton(matrice_cons, text='[v] vélo', variable=self.radio_groupe, value="[v]")
        v_ckbt.grid(row=4, column=2, padx=(10, 10), pady=(3, 3), sticky="w")

        z_ckbt = ttk.Radiobutton(matrice_cons, text='[z] zoo', variable=self.radio_groupe, value="[z]")
        z_ckbt.grid(row=4, column=3, padx=(10, 10), pady=(3, 3), sticky="w")

        ch_ckbt = ttk.Radiobutton(matrice_cons, text='[ʃ] chat', variable=self.radio_groupe, value="[ʃ]")
        ch_ckbt.grid(row=5, column=0, padx=(10, 10), pady=(3, 3), sticky="w")

        matrice_voy = ttk.Frame(self.matrice_sons,
                                relief='ridge',
                                borderwidth=5,
                                padding="7 7 7 7"
                                )
        matrice_voy.pack(padx=(10, 10),
                         pady=(10, 10),
                         anchor="w"
                         )

        cons_titre = ttk.Label(matrice_voy,
                               text='13 voyelles :',
                               font=("Calibri", 15, "bold")
                               )
        cons_titre.grid(row=0, column=0, padx=(10, 10), pady=(0, 3), columnspan=4, sticky="ew")

        a_ckbt = ttk.Radiobutton(matrice_voy, text='[a] arbre', variable=self.radio_groupe, value="[a]")
        a_ckbt.grid(row=1, column=0, padx=(10, 10), pady=(3, 3), sticky="w")

        e_ckbt = ttk.Radiobutton(matrice_voy, text='[e] éléphant', variable=self.radio_groupe, value="[e]")
        e_ckbt.grid(row=1, column=1, padx=(10, 10), pady=(3, 3), sticky="w")

        i_ckbt = ttk.Radiobutton(matrice_voy, text='[i] île', variable=self.radio_groupe, value="[i]")
        i_ckbt.grid(row=1, column=2, padx=(10, 10), pady=(3, 3), sticky="w")

        o_ckbt = ttk.Radiobutton(matrice_voy, text='[o] auto', variable=self.radio_groupe, value="[o]")
        o_ckbt.grid(row=1, column=3, padx=(10, 10), pady=(3, 3), sticky="w")

        ou_ckbt = ttk.Radiobutton(matrice_voy, text='[u] ours', variable=self.radio_groupe, value="[u]")
        ou_ckbt.grid(row=2, column=0, padx=(10, 10), pady=(3, 3), sticky="w")

        oo_ckbt = ttk.Radiobutton(matrice_voy, text='[ɔ] homme', variable=self.radio_groupe, value="[ɔ]")
        oo_ckbt.grid(row=2, column=1, padx=(10, 10), pady=(3, 3), sticky="w")

        ai_ckbt = ttk.Radiobutton(matrice_voy, text='[ɛ] air', variable=self.radio_groupe, value="[ɛ]")
        ai_ckbt.grid(row=2, column=2, padx=(10, 10), pady=(3, 3), sticky="w")

        u_ckbt = ttk.Radiobutton(matrice_voy, text='[y] urgent', variable=self.radio_groupe, value="[y]")
        u_ckbt.grid(row=3, column=0, padx=(10, 10), pady=(3, 3), sticky="w")

        eu_ckbt = ttk.Radiobutton(matrice_voy, text='[ø] heureux', variable=self.radio_groupe, value="[ø]")
        eu_ckbt.grid(row=3, column=1, padx=(10, 10), pady=(3, 3), sticky="w")

        eeu_ckbt = ttk.Radiobutton(matrice_voy, text='[œ] heure', variable=self.radio_groupe, value="[œ]")
        eeu_ckbt.grid(row=3, column=2, padx=(10, 10), pady=(3, 3), sticky="w")

        on_ckbt = ttk.Radiobutton(matrice_voy, text='[ɔ̃] ombre', variable=self.radio_groupe, value="[ɔ̃]")
        on_ckbt.grid(row=4, column=0, padx=(10, 10), pady=(3, 3), sticky="w")

        in_ckbt = ttk.Radiobutton(matrice_voy, text='[ɛ̃] indien', variable=self.radio_groupe, value="[ɛ̃]")
        in_ckbt.grid(row=4, column=1, padx=(10, 10), pady=(3, 3), sticky="w")

        an_ckbt = ttk.Radiobutton(matrice_voy, text='[ɑ̃] enfant', variable=self.radio_groupe, value="[ɑ̃]")
        an_ckbt.grid(row=4, column=2, padx=(10, 10), pady=(3, 3), sticky="w")



        occur_frame = ttk.Frame(self.matrice_sons)
        occur_frame.pack(padx=(10, 10),
                         pady=(0, 0),
                         anchor="w"
                         )


if __name__ == "__main__":
    root = ttk.Window()

    exemple_matrice = Matrice()

    root.mainloop()