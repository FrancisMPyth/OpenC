# Book To Scrap

Il s'agit d'un programme de grattage Web pour le site books.toscrape.com, toutes les informations de chaque catégories sont dans un fichier csv nommé du nom de la catégorie.

## Installation

Vous pouvez créer un environnement virtuel en utilisant la commande :
```
$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip freeze > requirements.txt
```
L'environnement virtuel venv est créé avec tous le spackages nécessaires pour exécuter le programme. Toutes les dépendances se trouvent dans le fichier requirements.txt.

## Utilisation

Dans le dossier ou se trouve le fichier main.py lancez:
```
$ python3 main.py
```
Dans le repertoire "data" créé, Tous les fichiers csv sont dans le dossier "csv" et toute les images sont dans le dossier "image".