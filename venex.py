import requests
from bs4 import BeautifulSoup
import json


def clean_data(data:str)-> str:
    """
    Esta funcion se encarga de limpiar el request asi poder transformalo en un diccionario
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
    """
    return diccionario["name"],float(diccionario["price"]) 


def venex_scrapper(url:str):
    """
    Esta funcion se encarga de hacer la request para obtener el HTML de la pagina y de recorrerlo
    - Recibe como parametro la url a scrappear en formato de string  
    """
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    product_list = soup.find_all(class_="col-container col-xs-12 col-md-8 col-lg-8") # Acedemos a las etiquetas con una clase especifica 
    
    for product in product_list:
        try:
            a_tag = product.find('a', class_='product-box-overlay') # Accede a las etiquetas a con clase "product-box-overlay" 
            
            data = a_tag.get('onclick') # Acede al atributo onclick de las etiquetas a donde se encuentra la informacion
            
            cleaned_data = clean_data(data) # Limpiamos la info

            product_dict = json.loads(cleaned_data) # Casteamos de string a diccionario (en realidad a json pero en este caso los formatos son iguales)

            print(venex_get_data(product_dict))
            
        except AttributeError:
            print("No se encontró el producto.")


# venex_scrapper("https://www.venex.com.ar/componentes-de-pc/microprocesadores?man=3") # Microprocesadores AMD
# venex_scrapper("https://www.venex.com.ar/componentes-de-pc/microprocesadores?man=35&opt=24751") # Microprocesadores Intel

# venex_scrapper("https://www.venex.com.ar/componentes-de-pc/motherboards/amd?opt=14214") # Mothers AMD
# venex_scrapper("https://www.venex.com.ar/componentes-de-pc/motherboards/intel?opt=14399") # Mothers Intel

# venex_scrapper("https://www.venex.com.ar/componentes-de-pc/memorias-ram/pc-de-escritorio?opt=14658") # Memorias RAM

# venex_scrapper("https://www.venex.com.ar/componentes-de-pccomponentes-de-pc/discos-solidos-ssd") # SSD 1 SORTEAR POR M.2
# venex_scrapper("https://www.venex.com.ar/discos-solidos-ssd?cPath=_231&page=2") # SSD 2 SORTEAR POR M.2
# venex_scrapper("https://www.venex.com.ar/discos-solidos-ssd?cPath=231&page=3") # SSD 3 SORTEAR POR M.2

# venex_scrapper("https://www.venex.com.ar/componentes-de-pccomponentes-de-pc/discos-duros-mecanicos") # HDD