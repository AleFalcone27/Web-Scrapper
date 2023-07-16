import requests
from bs4 import BeautifulSoup


def gezatek_get_data(product:str)-> tuple:
    
    """
    Esta funcion se encarga de obtener el nombre y el precio de cada uno de los productos accediendo a las etiquetas HTML en las que se encuentran 
    - product: Str con el contenido HTML de la pagina
    """
    
    name = product.find("h2").text # Obtenemos el nombre
    h3_Tag = product.find("h3") 
    price = h3_Tag.get("data-id") # Obtenemos el precio

    return name,price


def gezatek_scrapper(url:str)->dict:
    
    """
    Esta funcion se encarga de hacer la request para obtener el HTML de la pagina y de recorrerlo
    - url: str con la direccion a scrappear
    """
    
    try:
        response  = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
    except:
        print("--La URL ingresada NO EXISTE--")

    price_dic = dict()

    try:
        product_list = soup.find_all("div",class_ = "w-box product")
        for product in product_list:
                elem = gezatek_get_data(product)
                price_dic.update({elem})    
        return price_dic
    except:
        print("--No se encontró el producto--")



