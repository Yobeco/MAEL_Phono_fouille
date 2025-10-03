import sqlite3
import os

class Model:
    def __init__(self, db_file):
        self.db_file = db_file

    def create_connection(self):
        """ crée une connexion à la base de données SQLite
            dont le nom est l'argument "db_file"
        :param db_file: nom du fichier de base de données
        :return: objet de connexion ou 'None'
        """
        conn = None

        try:
            if not os.path.exists(self.db_file):       # Si le fichier "self.db_file" n'existe pas
                print(f"Creating database file: {self.db_file}")
                # Ouvrir la base de données en écriture (= créer si elle n'existe pas déjà) puis fermer.
                open(self.db_file, 'w').close()

            # se connecter à la db parce que, soit la DB existait déjà, soit elle vient d'être créée
            conn = sqlite3.connect(self.db_file)

            # Renvoyer l'objet de connexion
            return conn

        except Exception as e:
            print(e)

        return conn

    def execute_request(self, table):
        """ Exécute une requête de sélection sur la table spécifiée
               :param table: nom de la table à interroger
        """
        # Créer une connexion
        conn = self.create_connection()

        # Si la connexion est bien ouverte
        if conn is not None:
            # Créer un curseur de connexion
            cursor = conn.cursor()
            # Lancer une requête sur la table entrée en paramètre
            cursor.execute(f"SELECT lemme FROM {table} WHERE freqfilms2 BETWEEN 300 AND 10863")
            # Récupérer la réponse
            result = cursor.fetchall()
            # Convertir le résultat en variable de type liste
            result_list = []
            for element in result:
                result_list.append(element[0])

            # Création d'une variable de type collection (Pas de doublon possible)
            # pour enlever être (vb) + être (nom)...
            self.result_set = set(result_list)
            for element in self.result_set:
                print(element)

            # Afficher le résultat en colonne
            print(25 * "-")
            print(f"Nombre de réponses : {len(self.result_set)}")

            conn.close()

        else :
            print(f"Problème de connexion à {self.db_file}")

        return self.result_set

if __name__ == "__main__":
    db_file = "LEXIQUE.db"
    model_instance = Model(db_file)

    # Exécuter une requête sur une table précise
    model_instance.execute_request("lexique383")
