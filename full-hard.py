import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.fullh4rd.com.ar/cat/search/ryzen')
soup = BeautifulSoup(response.text, "html.parser")

product_list = soup.find_all(class_= "item product-list")

for product in product_list:
    try:
        name = product.find("h3").text
        price = product.find(class_="price").text
        print(name, price)
    except AttributeError:
        print("No se encontró el precio.")