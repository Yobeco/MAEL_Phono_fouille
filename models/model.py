from models.quit_accent import accent_dict, remove_accents

# Création des dictionnaires intermédiaires pour boucler
class ViewDataPaser:
    """
    Un grand dictionnaire est généré par l'interface.
    Classer pour séparer en plusieurs petits dictionnaires : un par section
    --> plus clair
    --> plus facile pour générer la requête. Chaque petit dictionnaire sera iterable
    --> possiblilté de joindre les différentes parties pour créer une requête générale
    """
    def __init__(self, view_data):
        self.dic_view_data_source = {}                  # Dictionnaire regroupant les infos où chercher les informations
        self.make_view_data_source(view_data)           # Lancer la fonction pour renseigner ce dictionnaire

        self.dic_view_data_diffic_lex = {}              # Dictionnaire regroupant les infos sur la difficulté de la DB Lexique
        self.make_view_data_diffic_lex(view_data)

        self.dic_view_data_diffic_minilex = {}          # Dictionnaire regroupant les infos sur la difficulté de la DB Minimum Lexical
        self.make_view_data_diffic_minilex(view_data)

        self.dic_view_data_sons = {}                    # Dictionnaire regroupant les infos sur les sons
        self.make_view_data_sons(view_data)

        self.dic_view_data_ltrs = {}                    # Dictionnaire regroupant les infos sur les lettres
        self.make_view_data_ltrs(view_data)

        self.dic_view_data_nbsyll = {}                  # Dictionnaire regroupant les infos sur le nombre de syllabes
        self.make_view_data_nbsyll(view_data)

        self.dic_view_data_nat_lex = {}                 # Dictionnaire regroupant les infos sur la nature des mots de DB Lexique
        self.make_view_data_nat_lex(view_data)

        self.dic_view_data_nat_minilex = {}             # Dictionnaire regroupant les infos sur la nature des mots de DB Minimum Lexical
        self.make_view_data_nat_minilex(view_data)

        self.dic_view_data_gender = {}                  # Dictionnaire regroupant les infos sur le genre
        self.make_view_data_gender(view_data)

        self.dic_view_data_them = {}                    # Dictionnaire regroupant les infos sur le thème
        self.make_view_data_them(view_data)

    def make_view_data_source(self, view_data):
        """
        Création du dictionnaire des infos nécessaires pour débuter la recherche
        :param view_data: Le grand dictionnaire généré par l'interface
        :return: None
        """
        self.dic_view_data_source.update({"choosen_db": view_data["choosen_db"],
                                     "lem_uniq" : view_data["lem_uniq"]
                                          })

    def make_view_data_diffic_lex(self, view_data):
        """
        Création du dictionnaire des infos de fréquence des mots de Lexique
        :param view_data: Le grand dictionnaire généré par l'interface
        :return: None
        """
        self.dic_view_data_diffic_lex.update({"tr_courant": view_data["tr_courant"],
                                        "courant" : view_data["courant"],
                                        "as_rare": view_data["as_rare"],
                                        "rare": view_data["rare"]
                                              })

    def make_view_data_diffic_minilex(self, view_data):
        """
        Création du dictionnaire des infos de fréquence des mots de Minimum Lexical
        :param view_data: Le grand dictionnaire généré par l'interface
        :return: None
        """
        self.dic_view_data_diffic_minilex.update({"niv_1": view_data["niv_1"],
                                                    "niv_2": view_data["niv_2"],
                                                    "niv_3": view_data["niv_3"]
                                                  })

    def make_view_data_sons(self, view_data):
        """
        Création du dictionnaire des sons à chercher
        :param view_data: Le grand dictionnaire généré par l'interface
        :return: None
        """
        self.dic_view_data_sons.update({"son_1": [view_data["logic_son_1"], view_data["son_1"], view_data["son_1_pos"], view_data["qqt_son_1"]],
                                        "son_2": [view_data["logic_son_2"], view_data["son_2"], view_data["son_2_pos"], view_data["qqt_son_2"]],
                                        "son_3": [view_data["logic_son_3"], view_data["son_3"], view_data["son_3_pos"], view_data["qqt_son_3"]],
                                        "son_4": [view_data["logic_son_4"], view_data["son_4"], view_data["son_4_pos"], view_data["qqt_son_4"]]
                                        })

    def make_view_data_ltrs(self, view_data):
        """
        Création du dictionnaire des lettres à chercher
        :param view_data: Le grand dictionnaire généré par l'interface
        :return: None
        """
        self.dic_view_data_ltrs.update({"ign_acc" : view_data["ign_acc"],
                                        "ltr_1": [view_data["logic_ltr_1"], view_data["ltr_1"], view_data["ltr_1_pos"], view_data["qqt_ltr_1"]],
                                        "ltr_2": [view_data["logic_ltr_2"], view_data["ltr_2"], view_data["ltr_2_pos"], view_data["qqt_ltr_2"]],
                                        "ltr_3": [view_data["logic_ltr_3"], view_data["ltr_3"], view_data["ltr_3_pos"], view_data["qqt_ltr_3"]]
                                        })

    def make_view_data_nbsyll(self, view_data):
        """
        Création du dictionnaire du nombre de syllables
        :param view_data: Le grand dictionnaire généré par l'interface
        :return: None
        """
        self.dic_view_data_nbsyll.update({"min_syll": view_data["min_syll"],
                                          "max_syll" : view_data["max_syll"]
                                          })

    def make_view_data_nat_lex(self, view_data):
        """
        Création du dictionnaire des natures de mots de Lexique
        :param view_data: Le grand dictionnaire généré par l'interface
        :return: None
        """
        self.dic_view_data_nat_lex.update({"nom_lex": view_data["nom_lex"],
                                            "vb_lex": view_data["vb_lex"],
                                            "adj_lex": view_data["adj_lex"],
                                            "adv_lex": view_data["adv_lex"],
                                            "arti_lex": view_data["arti_lex"],
                                            "pron_lex": view_data["pron_lex"],
                                            "conj_lex": view_data["conj_lex"],
                                            "prep_lex": view_data["prep_lex"],
                                            "onom_lex": view_data["onom_lex"]
                                          })

    def make_view_data_nat_minilex(self, view_data):
        """
        Création du dictionnaire des natures de mots de Minimum Lexical
        :param view_data: Le grand dictionnaire généré par l'interface
        :return: None
        """
        self.dic_view_data_nat_minilex.update({"nom_minilex": view_data["nom_minilex"],
                                           "vb_minilex": view_data["vb_minilex"],
                                           "adj_minilex": view_data["adj_minilex"],
                                           "pttm_minilex": view_data["pttm_minilex"]
                                           })

    def make_view_data_gender(self, view_data):
        """
        Création du dictionnaire du genre des mots
        :param view_data: Le grand dictionnaire généré par l'interface
        :return: None
        """
        self.dic_view_data_gender.update({"masc": view_data["masc"],
                                           "fem": view_data["fem"],
                                           "genre_poss" : view_data["genre_poss"],
                                           })

    def make_view_data_them(self, view_data):
        """
        Création du dictionnaire des thèmes de Minimum Lexical
        :param view_data: Le grand dictionnaire généré par l'interface
        :return: None
        """
        self.dic_view_data_them.update({"espace": view_data["espace"],
                                        "temps": view_data["temps"],
                                        "maison": view_data["maison"],
                                        "ecole": view_data["ecole"],
                                        "nature": view_data["nature"],
                                        "jardin": view_data["jardin"],
                                        "activ_phy": view_data["activ_phy"],
                                        "moi_autres": view_data["moi_autres"],
                                        "transports": view_data["transports"],
                                        "cuisine": view_data["cuisine"],
                                        "metiers": view_data["metiers"],
                                        "musique": view_data["musique"],
                                        "pron_autres": view_data["pron_autres"],
                                        "maths_raison": view_data["maths_raison"],
                                        "question": view_data["question"]
                                           })
        # print(f"Informations sur les thèmes pour MiniLex : {self.dic_view_data_them}")

    def parse_view_data(self):
        """
        Crée et renvoie un dictionnaire contenant les dictionnaires de données par section
        C'est lui qui sera analysé pour créer la requête
        :return: None
        """
        parsed_view_data = {
                "source" : self.dic_view_data_source,
                "diffic_lex" : self.dic_view_data_diffic_lex,
                "diffic_minilex" : self.dic_view_data_diffic_minilex,
                "sons" : self.dic_view_data_sons,
                "ltrs" : self.dic_view_data_ltrs,
                "nbsyll" : self.dic_view_data_nbsyll,
                "nat_lex" : self.dic_view_data_nat_lex,
                "nat_minilex" : self.dic_view_data_nat_minilex,
                "gender" : self.dic_view_data_gender,
                "them" : self.dic_view_data_them,
        }

        return parsed_view_data

    def show_parsed_view_data(self):
        """
        Affiche dans le terminal les données de l'interface
        de manière organisée par section
        """
        data = self.parse_view_data()
        for key, value in data.items():
            print(f"{key} : {value}")

class SqlRequestGen:
    """
    Classe qui va élaborer la requête SQL à partir des informations du formulaire
    Chaque section va générer un fragment de la requête sql (d'abord f-string, puis placeholder + tuple)
    Tuples :
    --> Placer ces éléments dans un tableau
    --> Joindre tous les éléments de ce tableau et joindre les tuples
    --> envoyer la requête
    """
    def __init__(self, parsed_data):
        self.parsed_data = parsed_data


    def generate_request(self):

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #                 Source de données
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        attribut = ""       # aussi appelé colonne / champ
        table = ""
        # 1ère partie de la requête :
        sql_request_source = ""

        # Choix de la table
        if self.parsed_data["source"]["choosen_db"] == "lexique" :
            table = "lexique383"
        elif self.parsed_data["source"]["choosen_db"] == "minilex":
            table = "minilex1"      # Table à introduire dans le DB

        # Choix de la colonne à consulter
        if self.parsed_data["source"]["lem_uniq"] and table == "lexique383":
            attribut = "lemme"
        elif self.parsed_data["source"]["lem_uniq"] and table == "minilex1":
            attribut = "ortho"       # Appeler la colonne FR --> fr
        elif not self.parsed_data["source"]["lem_uniq"] and table == "lexique383":
            attribut = "ortho"
        elif not self.parsed_data["source"]["lem_uniq"] and table == "minilex1":
            attribut = "ortho"       # ortho quelque-soit l'état de la case "lem_uniq"

        # placerholder pas possible pour les noms de tables et de colonnes.
        # Création d'une liste blanche pour éviter les injections SQL
        table_white_liste = ["lexique383", "minilex1"]
        attribut_white_liste = ["ortho", "lemme", "fr"]

        # Vérification de la liste blanche
        if (attribut in attribut_white_liste) and (table in table_white_liste):
            sql_source = f'''SELECT DISTINCT {attribut} FROM {table} WHERE '''
        else:
            raise ValueError("Nom de table ou d'attribut non valide")

        print(f"sql_source --> {sql_source}")

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #           Difficulté pour la DB Lexique
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        # Va uniquement choisir les valeurs entre "min" et "max"
        # choix -->  X . . X   identique à   X X X X
        # Technique :
        # À chaque case cochée correspond une liste
        # 1- On ajoute les listes des cases cochées
        # 2- On récupère le plus petit et le plus grand nombre de la liste obtenu --> fourchette
        # -*-> REMPLACER les f-string par des placeholder !

        """
        Fréquences par million d’occurrences partagées en 4 quarts (ajusté empiriquement)
                     |    0    |     1/4   |    2/4    |    3/4    |    4/4    |
        freqfilm2    |    0    |    0.02   |    0.08   |    0.42   |   25984   |
        freqlemfilm2 |    0    |    0.02   |    0.17   |    1.15   |   32237   |
                           <-rare->  <-as_rare-> <-courant-> <-tr_courant->
        """

        all_chkbox = []
        chkbox_rare = [[0, 0.02], [0, 0.02]]
        chkbox_as_rare = [[0.02, 0.08], [0.02, 0.17]]
        chkbox_courant = [[0.08, 0.42], [0.17, 1.15]]
        chkbox_tr_courant = [[0.42, 25984], [1.15, 32237]]

        def ortho_lem_choice(ortho_or_lem):
            """
            Fonction pour choisir les valeurs des fréquences de freqfilms2 ou de freqlemfilms2
            :param ortho_or_lem: 0 --> freqfilms2   /   1 --> freqlemfilms2
            :return: la liste contenant toutes les valeurs des listes (chekbox) selectionnées
            """
            loc_all_chkbox = []
            if self.parsed_data["diffic_lex"]["tr_courant"]:
                loc_all_chkbox = loc_all_chkbox + chkbox_tr_courant[ortho_or_lem]
            if self.parsed_data["diffic_lex"]["courant"]:
                loc_all_chkbox = loc_all_chkbox + chkbox_courant[ortho_or_lem]
            if self.parsed_data["diffic_lex"]["as_rare"]:
                loc_all_chkbox = loc_all_chkbox + chkbox_as_rare[ortho_or_lem]
            if self.parsed_data["diffic_lex"]["rare"]:
                loc_all_chkbox = loc_all_chkbox + chkbox_rare[ortho_or_lem]

            return loc_all_chkbox

        # Si "Lemmes seulement" coché, choisir les fréquences de "freqlemfilms2" --> Valeurs de chkbox_xxxx[1],
        # sinon, choisir les fréquences de "freqfilms2" --> Valeurs de chkbox_xxxx[0],
        if self.parsed_data["source"]["lem_uniq"]:
            all_chkbox = ortho_lem_choice(1)
        else:
            all_chkbox = ortho_lem_choice(0)

        # Pour voir la liste dans l'ordre
        all_chkbox.sort()
        print(f"all_chkbox : {all_chkbox}")

        # Création du tuple min / max pour le placeholder
        min_max_freq = (min(all_chkbox), max(all_chkbox))

        print(f"Valeurs de min_max_freq : {min_max_freq}")

        sql_diffic_lex = f"""freqfilms2 BETWEEN {min_max_freq[0]} AND {min_max_freq[1]}"""

        sql_diffic_lex = "(" + sql_diffic_lex + ") "

        print(f"sql_diffic_lex --> {sql_diffic_lex}")

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #         Difficulté pour la DB Minima Lexical
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        sql_diffic_minilex = ""

        if self.parsed_data["diffic_minilex"]["niv_1"]:
            sql_diffic_minilex = sql_diffic_minilex + "niv = 1 "
        if self.parsed_data["diffic_minilex"]["niv_2"]:
            sql_diffic_minilex = sql_diffic_minilex + "OR niv = 2 "
        if self.parsed_data["diffic_minilex"]["niv_3"]:
            sql_diffic_minilex = sql_diffic_minilex + "OR niv = 3"

        sql_diffic_minilex = "(" + sql_diffic_minilex + ")"

        print(sql_diffic_minilex)

        """
        Exemple de requête plus concise
        SELECT DISTINCT ortho
        FROM lexique383
        WHERE niv IN (1, 2, 3)
        
        --> À adapter avec les placeholder !
        """

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #                 Gestion des sons
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        # Dictionnaire des correspondances entre la syntaxe
        # de l'API et celle de la DB Lexique
        dic_api_to_lex = {
                    "[a]" : ["a"],
                    "[e]" : ["e"],
                    "[i]" : ["i", "j"],         # Chercher i trouve aussi 'i' le "ill"
                    "[o]" : ["o"],
                    "[u]" : ["u", "w"],         # Chercher u trouve aussi le 'ou' de "oui"
                    "[ɔ]" : ["O"],
                    "[ɛ]" : ["E"],
                    "[y]" : ["y", "8"],         # Chercher le son 'y' trouve aussi le 'u' de "huit"
                    "[ø]" : ["2", "°", "3"],    # Chercher le son 'eu' trouve aussi les schwas '°' et '3'
                    "[œ]" : ["9"],
                    "[ɔ̃]" : ["§"],
                    "[ɛ̃]" : ["5", "1"],         # Chercher le son 'in' trouve aussi le son "un"
                    "[ɑ̃]" : ["@"],
                    "[b]" : ["b"],
                    "[d]" : ["d"],
                    "[f]" : ["f"],
                    "[k]" : ["k"],
                    "[l]" : ["l"],
                    "[m]" : ["m"],
                    "[n]" : ["n"],
                    "[p]" : ["p"],
                    "[s]" : ["s"],
                    "[t]" : ["t"],
                    "[g]" : ["g"],
                    "[ɲ]" : ["N"],
                    "[ʒ]" : ["Z"],
                    "[ʁ]" : ["R"],
                    "[v]" : ["v"],
                    "[z]" : ["z"],
                    "[ʃ]" : ["S"]
                    }

        # --> attribut = lemme, lemme_fr ou ortho selon que lem_chekbox est coché

        def conv_logic(colonne, sql_req_x_logic):
            """
            Créer la logique en fonction des combobox
            :param colonne: "phon"--> pour chercher les sons   / "ortho" --> pour chercher les lettres phon
                            CRÉER UNE COLONNE phonlem --> pour ne pas trouver l'infinitif des verbes -mâmes en recherche de lemmes
            :param sql_req_x_logic: Ce qui est renvoyé part le combobox
            :return: Syntaxe logique au format SQLite3
            """
            # Première parenthèse inutile mais non gênante si un seul graphème par phonème
            # Devient indispensable pour 2 ou 3 graphèmes par phonème
            if (sql_req_x_logic == "avec") or (sql_req_x_logic == "et"):
                sql_req_x_logic = f"AND (({colonne} "     # PB !!!
            if sql_req_x_logic == "ou":
                sql_req_x_logic = f"OR (({colonne} "
            if sql_req_x_logic == "sans":
                sql_req_x_logic = f"AND (({colonne} NOT "

            return sql_req_x_logic


        def conv_req_lex_api(sql_sons_x_son_api):
            """
            Convertir le code API de l'interface en code Lexique grâce au dictionnaire dic_api_to_lex
            :param sql_sons_x_son_api: Symbole API renvoyé par l'interface
            :return: Notation propre à la DB Lexique
            """
            # Tape au clavier au lieu de chercher dans le tableau
            # Ne fonctionne que pour ce qui est présent sur le clavier... pas les ø et ə ou ɛ...
            if sql_sons_x_son_api[0] != "[":
                sql_sons_x_son_api = "[" + sql_sons_x_son_api + "]"

            sql_req_sons_x_son_lex = dic_api_to_lex[sql_sons_x_son_api]
            return sql_req_sons_x_son_lex


        def determ_position(sql_pos, sql_req_son_lex, colonne, nb_sons_for_graph, occur_var):
            """
            Fonction qui termine la syntax SQL3 en positionnant la lettre ou le son
            selon le bouton radio coché sous le Widget Logic_entry
            :param occur_var: Nombre d'occurrences dans le mot
            :param sql_pos: Paramètre renvoyé par le contenu de l'entry
            :param sql_req_son_lex: Notation de la DB Lexique du son coché
            :param colonne: Attribut que l'on renvoie
            :param nb_sons_for_graph:
            :return: la fin de la syntaxe avec LIKE pour préciser l'emplacement
            """

            def one_occur(occur_son_var):
                """
                Quand un seul graphème pour le phonème recherché
                Exemple : [b] --> [b]
                :return: l'extrait de requête correspondant
                """
                local_sql_req_pos = ""
                if occur_son_var == "1":
                    # Si aucune position spécifiée
                    if not sql_pos:
                        local_sql_req_pos = f"LIKE '%{sql_req_son_lex[0]}%')) "
                    if sql_pos == "deb":
                        local_sql_req_pos = f"LIKE '{sql_req_son_lex[0]}%')) "
                    if sql_pos == "fin":
                        local_sql_req_pos = f"LIKE '%{sql_req_son_lex[0]}')) "
                    if sql_pos == "mil":
                        local_sql_req_pos = f"LIKE '%{sql_req_son_lex[0]}%' AND {colonne} NOT LIKE '{sql_req_son_lex[0]}%' AND {colonne} NOT LIKE '%{sql_req_son_lex[0]}')) "

                if occur_son_var == "2":
                    # Aucune position spécifiable
                    local_sql_req_pos = f"LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%')) "

                if occur_son_var == "3":
                    # Aucune position spécifiable
                    local_sql_req_pos = f"LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%')) "

                return local_sql_req_pos


            def two_occur():
                """
                Quand deux graphèmes pour le phonème recherché (par simplification)
                Exemple : "[ɛ̃]" : ["5", "1"]
                :return: l'extrait de requête correspondant
                """
                local_sql_req_pos = ""
                if occur_var == "1":
                    # Si aucune position spécifiée
                    if not sql_pos:
                        local_sql_req_pos = f"LIKE '%{sql_req_son_lex[0]}%' OR {colonne} LIKE '%{sql_req_son_lex[1]}%')) "
                    if sql_pos == "deb":
                        local_sql_req_pos = f"LIKE '{sql_req_son_lex[0]}%' OR {colonne} LIKE '{sql_req_son_lex[1]}%')) "
                    if sql_pos == "fin":
                        local_sql_req_pos = f"LIKE '%{sql_req_son_lex[0]}' OR {colonne} LIKE '%{sql_req_son_lex[1]}')) "
                    if sql_pos == "mil":
                        local_sql_req_pos = (f"LIKE '%{sql_req_son_lex[0]}%' AND {colonne} NOT LIKE '{sql_req_son_lex[0]}%' AND {colonne} NOT LIKE '%{sql_req_son_lex[0]}') "
                                             + f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%' AND {colonne} NOT LIKE '{sql_req_son_lex[1]}%' AND {colonne} NOT LIKE '%{sql_req_son_lex[1]}')) ")

                if occur_var == "2":
                    local_sql_req_pos = (f"LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[1]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[0]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[1]}%')"
                                         f") ")

                if occur_var == "3":
                    local_sql_req_pos = (f"LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%{sql_req_son_lex[1]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[1]}%{sql_req_son_lex[0]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[1]}%{sql_req_son_lex[1]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[0]}%{sql_req_son_lex[1]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[1]}%{sql_req_son_lex[0]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[1]}%{sql_req_son_lex[1]}%')"
                                         f") ")

                return local_sql_req_pos



            def three_occur():
                """
                Quand trois graphèmes pour le phonème recherché (par simplification)
                Exemple : "[ø]" : ["2", "°", "3"]
                :return: l'extrait de requête correspondant
                """
                local_sql_req_pos = ""
                if occur_var == "1":
                    # Si aucune position spécifiée
                    if not sql_pos:
                        local_sql_req_pos = f"LIKE '%{sql_req_son_lex[0]}%' OR {colonne} LIKE '%{sql_req_son_lex[1]}%' OR {colonne} LIKE '%{sql_req_son_lex[2]}%')) "
                    if sql_pos == "deb":
                        local_sql_req_pos = f"LIKE '{sql_req_son_lex[0]}%' OR {colonne} LIKE '{sql_req_son_lex[1]}%' OR {colonne} LIKE '{sql_req_son_lex[2]}%')) "
                    if sql_pos == "fin":
                        local_sql_req_pos = f"LIKE '%{sql_req_son_lex[0]}' OR {colonne} LIKE '%{sql_req_son_lex[1]}' OR {colonne} LIKE '%{sql_req_son_lex[2]}')) "
                    if sql_pos == "mil":
                        local_sql_req_pos = (f"LIKE '%{sql_req_son_lex[0]}%' AND {colonne} NOT LIKE '{sql_req_son_lex[0]}%' AND {colonne} NOT LIKE '%{sql_req_son_lex[0]}') "
                                             + f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%' AND {colonne} NOT LIKE '{sql_req_son_lex[1]}%' AND {colonne} NOT LIKE '%{sql_req_son_lex[1]}')"
                                             + f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%' AND {colonne} NOT LIKE '{sql_req_son_lex[2]}%' AND {colonne} NOT LIKE '%{sql_req_son_lex[2]}')) ")

                if occur_var == "2":
                    local_sql_req_pos = (f"LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[1]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[2]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[0]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[1]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[2]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%{sql_req_son_lex[0]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%{sql_req_son_lex[1]}%') "
                                         f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%{sql_req_son_lex[2]}%')"
                                         f") ")

                # 27 combinaisons possibles des 3 graphèmes
                if occur_var == "3":
                    local_sql_req_pos = (f"LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%{sql_req_son_lex[1]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%{sql_req_son_lex[2]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[1]}%{sql_req_son_lex[0]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[1]}%{sql_req_son_lex[1]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[1]}%{sql_req_son_lex[2]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[2]}%{sql_req_son_lex[0]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[2]}%{sql_req_son_lex[1]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[0]}%{sql_req_son_lex[2]}%{sql_req_son_lex[2]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[0]}%{sql_req_son_lex[1]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[0]}%{sql_req_son_lex[2]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[1]}%{sql_req_son_lex[0]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[1]}%{sql_req_son_lex[1]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[1]}%{sql_req_son_lex[2]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[2]}%{sql_req_son_lex[0]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[2]}%{sql_req_son_lex[1]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[1]}%{sql_req_son_lex[2]}%{sql_req_son_lex[2]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%{sql_req_son_lex[0]}%{sql_req_son_lex[0]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%{sql_req_son_lex[0]}%{sql_req_son_lex[1]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%{sql_req_son_lex[0]}%{sql_req_son_lex[2]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%{sql_req_son_lex[1]}%{sql_req_son_lex[0]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%{sql_req_son_lex[1]}%{sql_req_son_lex[1]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%{sql_req_son_lex[1]}%{sql_req_son_lex[2]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%{sql_req_son_lex[2]}%{sql_req_son_lex[0]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%{sql_req_son_lex[2]}%{sql_req_son_lex[1]}%') "
                                        f"OR ({colonne} LIKE '%{sql_req_son_lex[2]}%{sql_req_son_lex[2]}%{sql_req_son_lex[2]}%')"
                                        f") ")

                if occur_var == "3":
                    pass

                return local_sql_req_pos

            sql_req_pos = ""


            if nb_sons_for_graph == 1:
                sql_req_pos = one_occur(occur_var)
            if nb_sons_for_graph == 2:
                sql_req_pos = two_occur()
            if nb_sons_for_graph == 3:
                sql_req_pos = three_occur()

            return sql_req_pos

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #                 Recherche de sons
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        # Pour tous les sons
        colonne_sons = ""     # Dans quelle colonne chercher
        if self.parsed_data['source']["lem_uniq"]:
            colonne_sons = "phon_lem"
        else:
            colonne_sons = "phon"


        ########################################
        # Recherche du son 1
        ########################################

        # Récupération des valeurs renvoyées par l'interface
        sql_son_1_logic = self.parsed_data['sons']["son_1"][0]
        sql_son_1_son_api = self.parsed_data['sons']["son_1"][1]
        sql_son_1_pos = self.parsed_data['sons']["son_1"][2]
        occur_son_1_var = self.parsed_data['sons']["son_1"][3]



        sql_request_son_1 = ""

        if sql_son_1_son_api:
            # Variable contenant l'opérateur logique la recherche du son_1
            sql_req_son_1_logic = conv_logic(colonne_sons, sql_son_1_logic)

            # Variable contenant la notation du son, propre à la DB Lexique
            sql_req_son_1_son_lex = conv_req_lex_api(sql_son_1_son_api)

            # Variable contenant la syntax SQLite3 pour positionner le son_1
            sql_req_son_1_son_pos = determ_position(sql_son_1_pos,
                                                                 sql_req_son_1_son_lex,
                                                                 "phon",
                                                                 len(conv_req_lex_api(sql_son_1_son_api)),
                                                                 occur_son_1_var
                                                               )

            # print(f"sql_req_son_1_son_pos : {sql_req_son_1_son_pos}")

            # Syntax complète de la recherche du son_1
            sql_request_son_1 = sql_req_son_1_logic + sql_req_son_1_son_pos

            # print(f"sql_request_son_1 : {sql_request_son_1}")

        ########################################
        # Recherche du son 2
        ########################################

        # Récupération des valeurs renvoyées par l'interface
        sql_son_2_logic = self.parsed_data['sons']["son_2"][0]
        sql_son_2_son_api = self.parsed_data['sons']["son_2"][1]
        sql_son_2_pos = self.parsed_data['sons']["son_2"][2]
        occur_son_2_var = self.parsed_data['sons']["son_2"][3]

        sql_request_son_2 = ""

        if sql_son_2_son_api:
            # Variable contenant l'opérateur logique la recherche du son_2
            sql_req_son_2_logic = conv_logic(colonne_sons, sql_son_2_logic)

            # Variable contenant la notation du son, propre à la DB Lexique
            sql_req_son_2_son_lex = conv_req_lex_api(sql_son_2_son_api)


            # Variable contenant la syntax SQLite3 pour positionner le son_2
            sql_req_son_2_son_pos = determ_position(sql_son_2_pos,
                                                                 sql_req_son_2_son_lex,
                                                                 "phon",
                                                                 len(conv_req_lex_api(sql_son_2_son_api)),
                                                                 occur_son_2_var
                                                               )

            # print(f"Son : {conv_req_lex_api(sql_son_2_son_api)} --> Il y a {len(conv_req_lex_api(sql_son_2_son_api))} graphème(s) pour ce son.")

            # Syntax complète de la recherche du son_2
            sql_request_son_2 = sql_req_son_2_logic + sql_req_son_2_son_pos

        ########################################
        # Recherche du son 3
        ########################################

        # Récupération des valeurs renvoyées par l'interface
        sql_son_3_logic = self.parsed_data['sons']["son_3"][0]
        sql_son_3_son_api = self.parsed_data['sons']["son_3"][1]
        sql_son_3_pos = self.parsed_data['sons']["son_3"][2]
        occur_son_3_var = self.parsed_data['sons']["son_3"][3]

        sql_request_son_3 = ""

        if sql_son_3_son_api:
            # Variable contenant l'opérateur logique la recherche du son_3
            sql_req_son_3_logic = conv_logic(colonne_sons, sql_son_3_logic)

            # Variable contenant la notation du son, propre à la DB Lexique
            sql_req_son_3_son_lex = conv_req_lex_api(sql_son_3_son_api)

            # Variable contenant la syntax SQLite3 pour positionner le son_3
            sql_req_son_3_son_pos = determ_position(sql_son_3_pos,
                                                               sql_req_son_3_son_lex,
                                                               "phon",
                                                               len(conv_req_lex_api(sql_son_3_son_api)),
                                                               occur_son_3_var
                                                               )

            # print(f"Son : {conv_req_lex_api(sql_son_3_son_api)} "
            #       f"--> Il y a {len(conv_req_lex_api(sql_son_3_son_api))} graphème(s) pour ce son.")

            # Syntax complète de la recherche du son_3
            sql_request_son_3 = sql_req_son_3_logic + sql_req_son_3_son_pos

        ########################################
        # Recherche du son 4
        ########################################

        # Récupération des valeurs renvoyées par l'interface
        sql_son_4_logic = self.parsed_data['sons']["son_4"][0]
        sql_son_4_son_api = self.parsed_data['sons']["son_4"][1]
        sql_son_4_pos = self.parsed_data['sons']["son_4"][2]
        occur_son_4_var = self.parsed_data['sons']["son_4"][3]

        sql_request_son_4 = ""

        if sql_son_4_son_api:
            # Variable contenant l'opérateur logique la recherche du son_4
            sql_req_son_4_logic = conv_logic(colonne_sons, sql_son_4_logic)

            # Variable contenant la notation du son, propre à la DB Lexique
            sql_req_son_4_son_lex = conv_req_lex_api(sql_son_4_son_api)

            # Variable contenant la syntax SQLite3 pour positionner le son_4
            sql_req_son_4_son_pos = determ_position(sql_son_4_pos,
                                                               sql_req_son_4_son_lex,
                                                               "phon",
                                                               len(conv_req_lex_api(sql_son_4_son_api)),
                                                               occur_son_4_var
                                                               )

            # print(f"Son : {conv_req_lex_api(sql_son_4_son_api)} "
            #       f"--> Il y a {len(conv_req_lex_api(sql_son_4_son_api))} graphème(s) pour ce son.")

            # Syntax complète de la recherche du son_4
            sql_request_son_4 = sql_req_son_4_logic + sql_req_son_4_son_pos

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #                Recherche de lettres
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        # Pour toutes les lettres
        colonne_trs = ""  # Dans quelle colonne chercher
        if self.parsed_data['ltrs']["ign_acc"]:
            if self.parsed_data['source']["lem_uniq"]:
                colonne_trs = "lem_norm"             # Va chercher les lettres des lemmes sans accents
            else:
                colonne_trs = "ortho_norm"           # Va chercher dans les lettres des mots sans accents
        else:
            if self.parsed_data['source']["lem_uniq"]:
                colonne_trs = "lemme"           # Va chercher les lettres des lemmes
            else:
                colonne_trs = "ortho"           # Va chercher dans les lettres des mots

        ########################################
        # Recherche de la lettre 1
        ########################################

        # Récupération des valeurs renvoyées par l'interface
        sql_ltr_1_ign_acc = self.parsed_data['ltrs']["ign_acc"]    # True / False
        sql_ltr_1_logic = self.parsed_data['ltrs']["ltr_1"][0]

        # Enlever les accents si "ign_acc" coché
        if sql_ltr_1_ign_acc :
            sql_ltr_1 = remove_accents(accent_dict, self.parsed_data['ltrs']["ltr_1"][1])
        else:
            sql_ltr_1 = self.parsed_data['ltrs']["ltr_1"][1]

        sql_ltr_1_pos = self.parsed_data['ltrs']["ltr_1"][2]
        occur_ltr_1_var = self.parsed_data['ltrs']["ltr_1"][3]


        sql_request_ltr_1 = ""

        # Si une lettre est dans l'entry
        if sql_ltr_1:
            # Variable contenant l'opérateur logique la recherche de ltr_1
            sql_req_ltr_1_logic = conv_logic(colonne_trs, sql_ltr_1_logic)

            # Création d'une liste pour que sql_ltr_1 (même avec plusieurs lettres) soit le premier élément,
            # sinon determ_position prend seulement la première lettre (1er élément)
            list_sql_ltr_1 = [sql_ltr_1]
            # Variable contenant la syntax SQLite3 pour positionner ltr_1
            sql_req_ltr_1_pos = determ_position(sql_ltr_1_pos,
                                                    list_sql_ltr_1,
                                                    "ortho",
                                                    1,
                                                    occur_ltr_1_var
                                                    )

            # Syntax complète de la recherche de ltr_1
            sql_request_ltr_1 = sql_req_ltr_1_logic + sql_req_ltr_1_pos

        ########################################
        # Recherche de la lettre 2
        ########################################

        # Récupération des valeurs renvoyées par l'interface
        sql_ltr_2_logic = self.parsed_data['ltrs']["ltr_2"][0]
        sql_ltr_2 = self.parsed_data['ltrs']["ltr_2"][1]
        sql_ltr_2_pos = self.parsed_data['ltrs']["ltr_2"][2]
        occur_ltr_2_var = self.parsed_data['ltrs']["ltr_2"][3]

        sql_request_ltr_2 = ""

        # Si une lettre est dans l'entry
        if sql_ltr_2:
            # Variable contenant l'opérateur logique la recherche de ltr_1
            sql_req_ltr_2_logic = conv_logic(colonne_trs, sql_ltr_2_logic)

            # Création d'une liste pour que sql_ltr_2 (même avec plusieurs lettres) soit le premier élément,
            # sinon determ_position prend seulement la première lettre (1er élément)
            list_sql_ltr_2 = [sql_ltr_2]
            # Variable contenant la syntax SQLite3 pour positionner ltr_2
            sql_req_ltr_2_pos = determ_position(sql_ltr_2_pos,
                                                list_sql_ltr_2,
                                                "ortho",
                                                1,
                                                occur_ltr_2_var
                                                )

            # Syntax complète de la recherche de ltr_2
            sql_request_ltr_2 = sql_req_ltr_2_logic + sql_req_ltr_2_pos

        ########################################
        # Recherche de la lettre 3
        ########################################

        # Récupération des valeurs renvoyées par l'interface
        sql_ltr_3_logic = self.parsed_data['ltrs']["ltr_3"][0]
        sql_ltr_3 = self.parsed_data['ltrs']["ltr_3"][1]
        sql_ltr_3_pos = self.parsed_data['ltrs']["ltr_3"][2]
        occur_ltr_3_var = self.parsed_data['ltrs']["ltr_3"][3]

        print(f"sql_ltr_3 : {sql_ltr_3}")

        sql_request_ltr_3 = ""

        # Si une lettre est dans l'entry
        if sql_ltr_3:
            # Variable contenant l'opérateur logique la recherche de ltr_1
            sql_req_ltr_3_logic = conv_logic(colonne_trs, sql_ltr_3_logic)

            print(f"sql_req_ltr_3_logic : {sql_req_ltr_3_logic}")

            # Création d'une liste pour que sql_ltr_3 (même avec plusieurs lettres) soit le premier élément,
            # sinon determ_position prend seulement la première lettre (1er élément)
            list_sql_ltr_3 = [sql_ltr_3]
            # Variable contenant la syntax SQLite3 pour positionner ltr_3
            sql_req_ltr_3_pos = determ_position(sql_ltr_3_pos,
                                                list_sql_ltr_3,
                                                "ortho",
                                                1,
                                                occur_ltr_3_var
                                                )

            # Syntax complète de la recherche de ltr_3
            sql_request_ltr_3 = sql_req_ltr_3_logic + sql_req_ltr_3_pos

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #                 Nombre de syllabes
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        # Récupération des valeurs renvoyées par l'interface
        min_syll = self.parsed_data['nbsyll']["min_syll"]
        max_syll = self.parsed_data['nbsyll']["max_syll"]

        sql_nb_syll = f"AND (nbsyll BETWEEN {min_syll} AND {max_syll}) "

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #                  Natures des mots
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        ########################################
        # Base de données "Lexique"
        ########################################

        if self.parsed_data["source"]["choosen_db"] == "lexique":
            # Récupération des valeurs renvoyées par l'interface
            nom_lex = self.parsed_data['nat_lex']["nom_lex"]
            vb_lex = self.parsed_data['nat_lex']["vb_lex"]
            adj_lex = self.parsed_data['nat_lex']["adj_lex"]
            adv_lex = self.parsed_data['nat_lex']["adv_lex"]
            arti_lex = self.parsed_data['nat_lex']["arti_lex"]
            pron_lex = self.parsed_data['nat_lex']["pron_lex"]
            conj_lex = self.parsed_data['nat_lex']["conj_lex"]
            prep_lex = self.parsed_data['nat_lex']["prep_lex"]
            onom_lex = self.parsed_data['nat_lex']["onom_lex"]

            sql_nat = f"AND ("
            if nom_lex :
                sql_nat = sql_nat + "(cgramortho LIKE '%NOM%') OR "
            if vb_lex :
                sql_nat = sql_nat + "(cgramortho LIKE '%VER%') OR "
            if adj_lex :
                sql_nat = sql_nat + "(cgramortho LIKE '%ADJ%') OR "
            if adv_lex :
                sql_nat = sql_nat + "(cgramortho LIKE '%ADV%') OR "
            if arti_lex :
                sql_nat = sql_nat + "(cgramortho LIKE '%ART%') OR "
            if pron_lex :
                sql_nat = sql_nat + "(cgramortho LIKE '%PRO%') OR "
            if conj_lex :
                sql_nat = sql_nat + "(cgramortho LIKE '%CON%') OR "
            if prep_lex :
                sql_nat = sql_nat + "(cgramortho LIKE '%PRE%') OR "
            if onom_lex :
                sql_nat = sql_nat + "(cgramortho LIKE '%ONO%') OR "

            # Enlever le 'OR' de la dernière partie et fermer la parentèse
            sql_nat = sql_nat[:-4] + ")"

        ########################################
        # Base de données "Minima Lexical"
        ########################################

        if self.parsed_data["source"]["choosen_db"] == "minilex":
            # Récupération des valeurs renvoyées par l'interface
            nom_minilex = self.parsed_data['nat_minilex']["nom_minilex"]
            vb_minilex = self.parsed_data['nat_minilex']["vb_minilex"]
            adj_minilex = self.parsed_data['nat_minilex']["adj_minilex"]
            pttm_minilex = self.parsed_data['nat_minilex']["pttm_minilex"]

            sql_nat = f"AND ("
            if nom_minilex :
                sql_nat = sql_nat + "(nat = 'N') OR "
            if vb_minilex :
                sql_nat = sql_nat + "(nat = 'V') OR "
            if adj_minilex :
                sql_nat = sql_nat + "(nat = 'A') OR "
            if pttm_minilex :
                sql_nat = sql_nat + "(nat = 'PM') OR "

            # Enlever le 'OR' de la dernière partie et fermer la parentèse
            sql_nat = sql_nat[:-4] + ")"

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #                   Genre des mots
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        masc = self.parsed_data['gender']["masc"]
        fem = self.parsed_data['gender']["fem"]
        # Genre possible
        genre_poss = self.parsed_data['gender']["genre_poss"]

        sql_genre = f"AND ("

        # Même notation du genre que ce soit Lexique ou Minima Lexical
        if genre_poss:
            try:
                if masc:
                    sql_genre = sql_genre + "(genre = 'm') OR "
                if fem:
                    sql_genre = sql_genre + "(genre = 'f') OR "
            except:
                print("Information de genre indisponible")

        # Enlever le 'OR' de la dernière partie et fermer la parentèse
        sql_genre = sql_genre[:-4] + ")"

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #               Thèmes de Minima Lexical
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


        espace = self.parsed_data['them']["espace"]
        temps = self.parsed_data['them']["temps"]
        maison = self.parsed_data['them']["maison"]
        ecole = self.parsed_data['them']["ecole"]

        nature = self.parsed_data['them']["nature"]
        jardin = self.parsed_data['them']["jardin"]
        activ_phy = self.parsed_data['them']["activ_phy"]
        moi_autres = self.parsed_data['them']["moi_autres"]

        transports = self.parsed_data['them']["transports"]
        cuisine = self.parsed_data['them']["cuisine"]
        metiers = self.parsed_data['them']["metiers"]
        musique = self.parsed_data['them']["musique"]

        pron_autres = self.parsed_data['them']["pron_autres"]
        maths_raison = self.parsed_data['them']["maths_raison"]
        question = self.parsed_data['them']["question"]

        sql_them = f"AND ("

        if self.parsed_data["source"]["choosen_db"] == "minilex":
            if espace:
                sql_them = sql_them + "(theme = 'espace') OR "
            if temps:
                sql_them = sql_them + "(theme = 'temps') OR "
            if maison:
                sql_them = sql_them + "(theme = 'maison') OR "
            if ecole:
                sql_them = sql_them + "(theme = 'ecole') OR "

            if nature:
                sql_them = sql_them + "(theme = 'nature') OR "
            if jardin:
                sql_them = sql_them + "(theme = 'jardin') OR "
            if activ_phy:
                sql_them = sql_them + "(theme = 'activ_phy') OR "
            if moi_autres:
                sql_them = sql_them + "(theme = 'moi_autres') OR "

            if transports:
                sql_them = sql_them + "(theme = 'transports') OR "
            if cuisine:
                sql_them = sql_them + "(theme = 'cuisine') OR "
            if metiers:
                sql_them = sql_them + "(theme = 'metiers') OR "
            if musique:
                sql_them = sql_them + "(theme = 'musique') OR "

            if pron_autres:
                sql_them = sql_them + "(theme = 'pron_autres') OR "
            if maths_raison:
                sql_them = sql_them + "(theme = 'maths_raison') OR "
            if question:
                sql_them = sql_them + "(theme = 'question') OR "



        # Enlever le 'OR' de la dernière partie et fermer la parentèse
        sql_them = sql_them[:-4] + ")"


        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #           Renvoie de la requête complète
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        def creat_request():
            """
            Fonction pour associer toutes les sections de requête
            """

            local_sql_request = sql_source

            if table == "lexique383" :
                local_sql_request = local_sql_request + sql_diffic_lex
            if table == "minilex1":
                local_sql_request = local_sql_request + sql_diffic_minilex

            if sql_request_son_1:
                local_sql_request = local_sql_request + sql_request_son_1
                if sql_request_son_2:
                    local_sql_request = local_sql_request + sql_request_son_2
                    if sql_request_son_3:
                        local_sql_request = local_sql_request + sql_request_son_3
                        if sql_request_son_4:
                            local_sql_request = local_sql_request + sql_request_son_4

            if sql_request_ltr_1:
                local_sql_request = local_sql_request + sql_request_ltr_1
                if sql_request_ltr_2:
                    local_sql_request = local_sql_request + sql_request_ltr_2
                    if sql_request_ltr_3:
                        local_sql_request = local_sql_request + sql_request_ltr_3

            local_sql_request = (local_sql_request
                                 + sql_nb_syll
                                 + sql_nat)

            # N'utiliser la requête de genre que si le genre est possible
            # Et s'il a été renseigné
            if genre_poss and (masc or fem):
                local_sql_request = local_sql_request + sql_genre

            # N'utiliser la requête de thème qu'avec Minilex
            if self.parsed_data["source"]["choosen_db"] == "minilex":
                local_sql_request = local_sql_request + sql_them

            local_sql_request = local_sql_request + ";"
            return local_sql_request

        sql_request = creat_request()
        return sql_request     # self.parsed_data


if __name__ == "__name__":
    pass