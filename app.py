##https://www.youtube.com/watch?v=sOAZpHDEdkg
# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint

# url = 'https://books.toscrape.com/'
# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')
# aside = soup.find('aside')
# side_category = aside.find('div', class_='side_categories')
# links = side_category.find_all('a')
# pprint(links)

# ol = soup.find('ol')
# products = ol.find_all('article', class_='product_pod')
# images = []
# for product in products:
#     img = product.find('img')
#     if img:
#         images.append(img['src'])

# pprint(images)


import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://books.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
side_categories = soup.find('div', class_='side_categories')
categories = side_categories.find('ul').find('li').find('ul')
categorie_list = [child.text.strip() for child in categories.children if child.name]
# pprint(categorie_list)


images = soup.find('section').find_all('img')
for img in images:
    pprint(img.get('src'))