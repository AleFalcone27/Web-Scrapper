import requests
from bs4 import BeautifulSoup


def full_hard_getdata(product):
    
    """
    Esta funcion se encarga de obtener el nombre y el precio de cada uno de los productos
    accediendo a las etiquetas HTML en las que se encuentran
    """

    name = product.find("h3").text
    price = product.find(class_="price").text
    
    return name,price


def full_hard_scrapper(url:str):
    """
    Esta funcion se encarga de hacer la request para obtener el HTML de la pagina y de recorrerlo
    - Recibe como parametro la url a scrappear en formato de string  
    """
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    product_list = soup.find_all(class_= "item product-list")

    for product in product_list:
        try:
            print(full_hard_getdata(product))
        except AttributeError:
            print("No se encontró el producto.")
        

# full_hard_scrapper("https://www.fullh4rd.com.ar/cat/192/amd-am4/1") # Microprocesares AMD
# full_hard_scrapper("https://www.fullh4rd.com.ar/cat/384/intel-1700/1") # Microprocesadores Intel

# full_hard_scrapper("https://www.fullh4rd.com.ar/cat/198/mb-amd-am4/1/menor") # Mothers AMD
# full_hard_scrapper("https://www.fullh4rd.com.ar/cat/385/mb-intel-1700/1") # Mothers Intel

# full_hard_scrapper("https://www.fullh4rd.com.ar/cat/search/ddr4") # Memoria Ram FALTA SORTEAR POR SODDIM Y NORMAL

# full_hard_scrapper("https://www.fullh4rd.com.ar/cat/185/ssd/1") # SSD 1 SORTEAR POR M.2
# full_hard_scrapper("https://www.fullh4rd.com.ar/cat/185/discos-ssd/2")# SSD 2 SORTEAR POR M.2

# full_hard_scrapper("https://www.fullh4rd.com.ar/cat/19/discos-sata/1") # HDD
