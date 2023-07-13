import requests
from bs4 import BeautifulSoup


def gezatek_get_data(product:str):
    
    """
    Esta funcion se encarga de obtener el nombre y el precio de cada uno de los productos
    accediendo a las etiquetas HTML en las que se encuentran
    """
    name = product.find("h2").text # Obtenemos el nombre
    h3_Tag = product.find("h3") # Obtenemos el precio
    price = h3_Tag.get("data-id")

    return name,price


def gezatek_scrapper(url:str):
    
    """
    Esta funcion se encarga de hacer la request para obtener el HTML de la pagina y de recorrerlo
    - Recibe como parametro la url a scrappear en formato de string  
    """
    response  = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    product_list = soup.find_all("div",class_ = "w-box product")

    try:
        for product in product_list:
            print(gezatek_get_data(product))
    except AttributeError:
        print("No se encontró el producto.")
        


# gezatek_scrapper("https://www.gezatek.com.ar/tienda/procesadores-amd/") # Microprocesadores AMD
# gezatek_scrapper("https://www.gezatek.com.ar/tienda/procesadores-intel/") # Microprocesadores Intel

# gezatek_scrapper("https://www.gezatek.com.ar/tienda/mothers-amd-am4/") # Mothers AMD
# gezatek_scrapper("https://www.gezatek.com.ar/tienda/mothers-intel-6ta-7ma/") #Mothers Intel




