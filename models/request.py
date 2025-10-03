import sqlite3

class Request:
    def __init__(self, database_path, sql_request):
        self.database_path = database_path
        self.sql_request = sql_request


    def make_request(self):
        """
        Pas encore de placeholders pour gérer séparément la requête et les paramètres...
        À implémenter !
        :return: None
        """
        result_list = []

        try:
            # Pour déconnecter automatiquement, même en cas d'erreur...
            with sqlite3.connect(self.database_path) as connexion:
                curseur = connexion.cursor()

                # Activer PRAGMA pour cette connexion pour activer la sensibilité à la casse
                curseur.execute("PRAGMA case_sensitive_like = ON;")

                # Exécuter la requête SQL
                curseur.execute(self.sql_request)
                resultats = curseur.fetchall()
                i = 1
                if resultats:
                    for ligne in resultats:
                        print(ligne[0])
                        result_list.append((i, ligne[0]))
                        i += 1
                    print(f"Il y a {len(resultats)} résultats.")
                else:
                    print("Aucun résultat trouvé.")


        except sqlite3.Error as erreur:
            print(f"Erreur SQLite3 : {erreur}")


        except Exception as erreur:
            print(f"Une erreur inattendue s'est produite : {erreur}")

        # Renvoyer la liste des mots trouvés
        return result_list