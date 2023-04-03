# OpenC
ProjetsPython
# Projet 2: Books To Scrape
--------------

__Le script « main.py »cpermet de récupérer les informations de tout les produits sur le site http://books.toscrape.com/. Ces informations sont les suivantes:__
--------------------------

product_page_url 
* universal_ product_code (upc)  
* title 
* price_including_tax 
* price_excluding_tax 
* number_available 
* product_description 
* category 
* review_rating 
* image_url
============================================
Les images des livres sont téléchargées. Ces données sont ensuite classées par catégories et inscrites dans un fichier CSV correspondant. Les données sont générées à la racine du projet suivant cette arborescence:  
-- data/  
    ----- categorie1/  
        ----------- categorie1.csv  
        ----- imgs/  
            ------ img1.jpg  
            ------ img2.jpg   
    ---- categorie2/  
 

Installation:
Installation de [Python] : (https://www.python.org/downloads/release/python-3112/)
Lancer le terminal et placer vous dans le répertoire de votre choix.  
Clonez le [repository] : (https://github.com/FrancisMPyth/OpenC.git)
Installer les packages : pip install -r requirements.txt

Lancez le script : python main.py
