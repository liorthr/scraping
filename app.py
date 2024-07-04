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