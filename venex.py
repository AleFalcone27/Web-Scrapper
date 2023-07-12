import requests
from bs4 import BeautifulSoup
import json

import requests
from bs4 import BeautifulSoup
import json

response = requests.get('https://www.venex.com.ar/resultado-busqueda.htm?keywords=ryzen')
soup = BeautifulSoup(response.text, "html.parser")

product_list = soup.find_all(class_="col-container col-xs-12 col-md-8 col-lg-8")


def clean_data(data:str):
    """
    Esta funcion se encarga de limpiar el request asi poder transformalo en un diccionario
    """
    data = data.strip("['").rstrip("']")
    data = data.replace("enhancedClick(","")
    data = data.replace(')',"")
    data = data.replace("(","")
    data = data.strip()
    return data


def get_price_and_name(diccionario:dict):
    return diccionario["name"],float(diccionario["price"]) # Obtenemos el nombre y el precio de cada uno de los productos

def get_data():
    """
    Esta funcion se ecarga de ingresar a las etiquetas del HTML y scrapear 
    la informacion que nos interesa
    """
    try:
        a_tag = product.find('a', class_='product-box-overlay') # Accede a las etiquetas a con clase "product-box-overlay" 
        data = a_tag.get('onclick') # Acede al atributo onclick de las etiquetas a donde se encuentra la informacion
        cleaned_data = clean_data(data) # Limpiamos la info

        product_dict = json.loads(cleaned_data) # Casteamos de string a diccionario (en realidad a json pero en este caso los formatos son iguales)

        print(get_price_and_name(product_dict))
        
    except AttributeError:
        print("No se encontró el atributo onclick.")
    

for product in product_list:
    get_data()


