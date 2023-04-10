import os
import requests
from bs4 import BeautifulSoup
import csv

# URL de la page de la catégorie à extraire
url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'

# Obtenir le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extraire les informations de chaque livre
books_urls = []
while True:
    # Extraire les informations des livres sur la page actuelle
    book_elements = soup.find_all('article', {'class': 'product_pod'})
    for book_element in book_elements:
        book_url = book_element.find('a')['href'].replace('../../../', 'http://books.toscrape.com/catalogue/')
        books_urls.append(book_url)

    # Passer à la page suivante si elle existe
    next_page_element = soup.find('li', {'class': 'next'})
    if not next_page_element:
        break

    next_page_url = next_page_element.find('a')['href']
    url = url.rsplit('/', 2)[0] + '/' + next_page_url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

# Écrire les données dans un fichier CSV
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'travel_books_urls.csv')

with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['product_page_url'])
    for book_url in books_urls:
        writer.writerow([book_url])
