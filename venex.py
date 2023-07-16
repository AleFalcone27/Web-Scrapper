import requests
from bs4 import BeautifulSoup
import json


def clean_data(data:str)-> str:
    """
    Esta funcion se encarga de limpiar el request asi poder transformalo en un diccionario
    - data: Str con la informacion extraida del HTML
    """
    data = data.strip("['").rstrip("']")
    data = data.replace("enhancedClick(","")
    data = data.replace(')',"")
    data = data.replace("(","")
    data = data.strip()
    return data

def venex_get_data(diccionario:dict)-> tuple:
    """
    Esta funcion se encarga de obtener y devolver el nombre y el precio de cada uno de los productos 
    - diccionario: dict que contiene la informacion extraida del HTML
    """
    return diccionario["name"],(diccionario["price"]) 


def venex_scrapper(url:str)->dict:
    """
    Esta funcion se encarga de hacer la request para obtener el HTML de la pagina y de recorrerlo
    - url: string con la direccion a scrappear 
    """
    
    try:
        response  = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        product_list = soup.find_all(class_="col-container col-xs-12 col-md-8 col-lg-8") # Acedemos a las etiquetas con una clase especifica 
    except:
        print("--La URL ingresada NO EXISTE o La pagina Fue Editada--")
    
    
    
    price_dic = dict()
    
    try:
        for product in product_list:
            a_tag = product.find('a', class_='product-box-overlay') # Accede a las etiquetas a con clase "product-box-overlay" 
            
            data = a_tag.get('onclick') # Acede al atributo onclick de las etiquetas a donde se encuentra la informacion
            
            cleaned_data = clean_data(data) # Limpiamos la info

            product_dict = json.loads(cleaned_data) # Casteamos de string a diccionario (en realidad a json pero en este caso los formatos son iguales)

            price_dic.update({venex_get_data(product_dict)})
            
        return price_dic
            
    except AttributeError:
        print("No se encontró el producto.")


