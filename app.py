import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'particular-ecommerce-website-url'

page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

product_names = []
products = soup.find_all('a', class_='class_name')

for product in products:
	product_names.append(product.find('div', class_='_3wU53n').text)

data = pd.DataFrame({'Product Name': product_names})
data.to_csv('products.csv', index=False, encoding='utf-8')

	# print(product, end='\n'*2)