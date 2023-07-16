import requests
from bs4 import BeautifulSoup


def full_hard_getdata(product)-> tuple:
    
    """
    Esta funcion se encarga de obtener el nombre y el precio de cada uno de los productos accediendo a las etiquetas HTML en las que se encuentran 
    - product: Str con el contenido HTML de la pagina
    """
    name = product.find("h3").text
    price = product.find(class_="price").text #Nos devuelve 2 precio uno normal y el otro el precio de "descuento"
    
    # Nos quedamos con el precio de descuento
    price = price.split(" ")
    price = price[0]

    return name,price


def full_hard_scrapper(url:str)-> dict:
    """
    Esta funcion se encarga de hacer la request para obtener el HTML de la pagina y de recorrerlo
    - url: String con la direccion a scrappear 
    """
    try:
        response  = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        product_list = soup.find_all(class_= "item product-list")
    except:
        print("--La URL ingresada NO EXISTE o La pagina Fue Editada--")
    
    price_dic = dict()

    for product in product_list:
        try:
            price_dic.update({full_hard_getdata(product)})
        except AttributeError:
            print("No se encontró el producto.")
    return price_dic
        

