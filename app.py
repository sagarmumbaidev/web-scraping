from lxml import html
import requests
import pandas as pd

page = requests.get('ecommerce-website')
page_content = html.fromstring(page.content)
product_names = []

products = page_content.xpath('//*[@class="targeted-class"]/@title')

for product in products:
	product_names.append(product)


data = pd.DataFrame({'Product Name': product_names})
data.to_csv('products.csv', index=False, encoding='utf-8')

#print(product_names,  end='\n'*2)