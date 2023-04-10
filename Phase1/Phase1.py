import os
import requests
from bs4 import BeautifulSoup
import csv

# URL de la page produit à extraire
url = 'http://books.toscrape.com/catalogue/the-grand-design_405/index.html'

# Obtenir le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extraire les informations de la page
product_page_url = url
upc_element = soup.find('th', string='UPC')
upc = upc_element.find_next_sibling('td').text if upc_element else ''
title = soup.find('h1').text
price_including_tax_element = soup.find('th', string='Price (incl. tax)')
price_including_tax = price_including_tax_element.find_next_sibling('td').text if price_including_tax_element else ''
price_excluding_tax_element = soup.find('th', string='Price (excl. tax)')
price_excluding_tax = price_excluding_tax_element.find_next_sibling('td').text if price_excluding_tax_element else ''
availability_element = soup.find('th', string='Availability')
number_available = availability_element.find_next_sibling('td').text if availability_element else ''
product_description_element = soup.find('div', {'id': 'product_description'})
product_description = product_description_element.find_next_sibling('p').text if product_description_element else ''
category_element = soup.find('ul', {'class': 'breadcrumb'}).find_all('li')[-2]
category = category_element.text.strip() if category_element else ''
review_rating_element = soup.find('p', {'class': 'star-rating'})
review_rating = review_rating_element.get('class')[1] if review_rating_element else ''
image_url_element = soup.find('div', {'class': 'item active'}).find('img')
image_url = image_url_element['src'].replace('../', 'http://books.toscrape.com/') if image_url_element else ''

# Créer le chemin complet vers le fichier CSV
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'produit.csv')

# Écrire les données dans un fichier CSV
with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax',
                     'price_excluding_tax', 'number_available', 'product_description', 'category',
                     'review_rating', 'image_url'])
    writer.writerow([product_page_url, upc, title, price_including_tax, price_excluding_tax,
                     number_available, product_description, category, review_rating, image_url])
