"""
Petite application pour vérifier que les mots de la liste renvoyée
correspondent bien à la recherche faite.
Par exemple si un mot de la liste n'a pas :  1 < nbsyll < 3
alors que c'est ce qui est demandé : il sera signalé.

Si tous les mots de la liste respectent le critère testé
--> Afficher "Tous les mots respectent e critère"

--> Un seul critère à la fois

"""

from models.request import Request

text_to_verify = '''bagarreur
baiseur
balayeur
batteur
batteurs
belle-soeur
best-seller
beurre
beurré
beuverie
bienfaiteur
blancheur
blanchisseur
bluff
bluffe
bluffer
bluffes
bluffez
bluffé
boeuf'''

list_to_verify = text_to_verify.split("\n")
print(f"Liste à vérifier : \n{list_to_verify}")

# Chemin d'accès de la DB
database_path = "models/PHONOFOUILLE_V5.db"
# Requête à lancer pour chaque mot

# Requête de base pour mémoire
"""
SELECT DISTINCT ortho FROM lexique383 
                    WHERE (freqfilms2 BETWEEN 0.08 AND 25984) 
                    AND ((phon LIKE '%d%d%d%')) 
                    AND (nbsyll BETWEEN 1 AND 9) 
                    AND ((cgramortho LIKE '%NOM%') 
                    OR (cgramortho LIKE '%ART%'))
                    ;
                    
SELECT DISTINCT ortho FROM lexique383 
                    WHERE (freqfilms2 BETWEEN 0.42 AND 25984) 
                    AND ((phon LIKE 'b%')) 
                    AND ((phon LIKE '%9%')) 
                    AND (nbsyll BETWEEN 1 AND 3) 
                    AND (
                               (cgramortho LIKE '%NOM%') 
                            OR (cgramortho LIKE '%VER%') 
                            OR (cgramortho LIKE '%ADJ%') 
                            OR (cgramortho LIKE '%ADV%') 
                            OR (cgramortho LIKE '%ART%') 
                            OR (cgramortho LIKE '%PRO%') 
                            OR (cgramortho LIKE '%CON%') 
                            OR (cgramortho LIKE '%PRE%')
                        );

"""

sql_request = """SELECT DISTINCT ortho FROM lexique383 
                    WHERE (cgramortho LIKE '%NOM%') 
                            OR (cgramortho LIKE '%VER%') 
                            OR (cgramortho LIKE '%ADJ%') 
                            OR (cgramortho LIKE '%ADV%') 
                            OR (cgramortho LIKE '%ART%') 
                            OR (cgramortho LIKE '%PRO%') 
                            OR (cgramortho LIKE '%CON%') 
                            OR (cgramortho LIKE '%PRE%')
                    ;
              """

# Instanciation de Request
test_object = Request(database_path, sql_request)

# Rechercher avec seulement ce critère
one_criter_result = test_object.make_request()

# Ne garder que le mot (enlever l'ID)
one_criter_list = []
for element in one_criter_result:
    one_criter_list.append(element[1])

print(50*"%")
print(f"%        Test Phono-fouille a été lancé         %")
print(50*"%")

# Vérifier si chaque mot proposé avec plusieurs critères appartient bien
# à la liste de mots trouvée avec seulement ce critère
def verify_list():
    i = 0
    for element in list_to_verify:
        if element not in one_criter_list:
            print(f"Le mot '{element}', ne respecte pas le critère")
            i += 1
        else:
            pass
            # print(f"Mot '{element}' --> OK")
    print(50*"%")
    if i != 0:
        print(f"{i} mots sur {len(list_to_verify)} ne respectent pas le critère.")
    else:
        print(f"Tous les mots respectent le critère.")

verify_list()

