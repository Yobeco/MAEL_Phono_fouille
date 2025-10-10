![MAEL](https://github.com/Yobeco/MAEL_Gen/blob/main/readme_assets/Logo-MAEL-120.png "Logo du projet MAEL")

# MAEL Phonofouille

*Une application appartenant au [__projet MAEL__](https://github.com/Yobeco/MAEL_Project)*   
Copyright (c) 2022 Yonnel Bécognée

[![License: Libre Non Commerciale](https://img.shields.io/badge/license-GNU%20GENERAL%20PUBLIC%20LICENSE%20V3-white.svg)](./LICENSE)

[![Python](https://img.shields.io/badge/Python-V3.10%2B-blue?logo=python&logoColor=yellow)](https://www.python.org/)

[![SQLite](https://img.shields.io/badge/SQLite-V3.50.4%2B-003366?logo=sqlite&logoColor=99CCFF)](https://sqlite.org/)

[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-009900.svg)](#contributing) [![Beginner friendly](https://img.shields.io/badge/Beginner%20friendly-FF8000)]()

[![Status: Active](https://img.shields.io/badge/status-active-009900.svg)]()

## :fr: [Français](https://github.com/Yobeco/MAEL_Phonofouille) | :gb: English

---

![](https://github.com/Yobeco/MAEL_Project/blob/main/readme_assets/Phonofouille-600px.png)


## A- Description :eye:

:computer: **Application de bureau** multiplateforme (Linux, MacOS et Windows) qui permet aux enseignants de trouver de mots selon des critères pédagogiques très utiles comme :

- La présence et la position d'un son dans le mot,
- la présence et la position de lettres,
- le niveau de difficulté des mots,
- le thème,
- la nature grammaticale du mot...

Les bases de données de mots actuellement implémentées sont :
- [MiniLex](https://github.com/Yobeco/MAEL_Phrases/blob/main/readme_assets/Minima%20_Lexical_C1fev25.pdf) élaborée par AMLA Nord
- [Lexique 3.83](http://www.lexique.org/) <img src="https://cdn.simpleicons.org/creativecommons/FFFF" width="24" height="24" style="vertical-align: middle;" /> BY NC *(Très complète ! Et surtout : contient les __descriptions phoniques__)*

Phonofouille est déjà utilisée comme tel par des enseignants, mais son objectif réel est d'être implémenté en JavaScript dans **MAEL Phrase** afin d'aider les enseigannts à créer des activités sur mesure pour leurs élèves.

---

## B- Fonctionnalités :clipboard:

- Choix de la base de données.
- Choix du niveau de difficulté.
- Choix des sons qui doivent être présents, et leur position.
- Choix des lettres qui doivent être présentes, et leur position.
- Choix du nombre de syllabes.
- choix du genre (si pertinent).
- Choix du thème.
- Bouton pour lancer la recherche.
- Bouton pour copier toute la liste de mots.
- Double clic sur un mot pour le copier.
- Clic droit sur la liste pour la réorganiser ou supprimer une ligne
- Menu de déplacement dans les pages de la liste.

---

## C- Comment utiliser MAEL Gen ? :blush:

Utilisation très standard :

1. Choisir la base de données
1. Choisir les critères de sélection des mots (Pas d'ordre en particulier)
1. Lancer la recherche
1. Copier toute la liste ou seulement un mot

---

## D- Principe de fonctionnement :gear:

*(Pour aider à la compréhension du code)*

---

Les différents widgets de l'interface génèrent une [variable de type dictionnaire](/readme_assets/parsed_data_V6.pdf) qui contient les critères qui seront utilisés par **SQlite** pour lancer la recherche.

---

## E- Fonctionnalités à développer :rocket:

- Ajout des images associées aux mots dans la base de données.
- Ajout des vignettes dans l'interface du moteur de recherche.

Il faudrait surtout porter **MAEL Phonofouille** en JavaScript dans l'interface de la plateforme **MAEL Phrases**.

### :+1: Proposez votre aide pour efffectuer ce portage.

---

## F- Participez au projet MAEL :open_hands:

:sos: Pour **obtenir de l'aide** concernant l'utilisation de MAEL ou pour **paticiper au développement** :computer:, écrivez-moi ici :

### :mailbox_with_mail: ***[mael@lvh.edu.ni](mailto:mael@lvh.edu.ni)***

### :star2: Contributeurs

Un grand merci à toutes les personnes qui vont contribuer à ce projet !

 | Avatar | Nom                | GitHub                          | Rôle                     |
 |--------|--------------------|---------------------------------|--------------------------|
 | ![Bécognée Yonnel](https://github.com/Yobeco.png?size=50) | Bécognée Yonnel | [@Yobeco](https://github.com/Yobeco) | Mainteneur |
 | ... | ... | ... | Développeur (euse) |
 | ... | ... | ... | Illustrateur (trice) |
 | ... | ... | ... | Traducteur (trice) |

---

## G- Installation :arrow_heading_down:

Pour essayer **MAEL Gen**, exécutez le script :

    git clone https://github.com/Yobeco/MAEL_Gen.git
    cd MAEL_Gen
    python3 -m venv mael_venv
    source mael_venv/bin/activate
    pip install -r requirements.txt
    python3 MAEL_V5.0.py


