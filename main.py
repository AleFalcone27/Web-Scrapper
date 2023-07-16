from fullhard import full_hard_scrapper
from venex import venex_scrapper
from gezatek import gezatek_scrapper
from excel import load_on_excel
flag = True

try : 
    # LA PRIMER LLAMADA HAY QUE HACERLA ANTES DE CAMBIAR EL ESTADO DE LA BANDERA
    load_on_excel(full_hard_scrapper("https://www.fullh4rd.com.ar/cat/192/amd-am4/1"),1,"Procesadores AMD",flag) # Procesadores AMD

    flag = not flag
    # LAS DEMAS LLAMADAS DEBEN HACERSE ABAJO DE ESTE LINEA
    
    # --- FULL HARD ----
    load_on_excel(full_hard_scrapper("https://www.fullh4rd.com.ar/cat/384/intel-1700/1"),1,"Procesadores Intel",flag) # Microprocesadores Intel
    load_on_excel(full_hard_scrapper("https://www.fullh4rd.com.ar/cat/198/mb-amd-am4/1/menor"),1,"Motherboards AMD",flag) # Mothers AMD
    load_on_excel(full_hard_scrapper("https://www.fullh4rd.com.ar/cat/385/mb-intel-1700/1"),1,"Motherboards Intel",flag) # Mothers Intel
    load_on_excel(full_hard_scrapper("https://www.fullh4rd.com.ar/cat/search/ddr4"),1,"Memorias RAM",flag) # Memorias Ram 
    load_on_excel(full_hard_scrapper("https://www.fullh4rd.com.ar/cat/185/ssd/1"),1,"SSD",flag) # SSD 
    
    
    # --- VENEX ----
    load_on_excel(venex_scrapper("https://www.venex.com.ar/componentes-de-pc/microprocesadores?man=3"),2,"Procesadores AMD",flag) # Procesadores AMD
    load_on_excel(venex_scrapper("https://www.venex.com.ar/componentes-de-pc/microprocesadores?man=35&opt=24751"),2,"Procesadores Intel",flag) # Microprocesadores Intel
    load_on_excel(venex_scrapper("https://www.venex.com.ar/componentes-de-pc/motherboards/amd?opt=14214"),2,"Motherboards AMD",flag) # Mothers AMD
    load_on_excel(venex_scrapper("https://www.venex.com.ar/componentes-de-pc/motherboards/intel?opt=14399"),2,"Motherboards Intel",flag) # Mothers Intel
    load_on_excel(venex_scrapper("https://www.venex.com.ar/componentes-de-pc/memorias-ram/pc-de-escritorio?opt=14658"),2,"Memorias RAM",flag) # Memorias RAM
    load_on_excel(venex_scrapper("https://www.venex.com.ar/componentes-de-pccomponentes-de-pc/discos-solidos-ssd"),2,"SSD",flag) 
    load_on_excel(venex_scrapper("https://www.venex.com.ar/discos-solidos-ssd?cPath=_231&page=2"),2,"SSD",flag) # SSD
    load_on_excel(venex_scrapper("https://www.venex.com.ar/discos-solidos-ssd?cPath=231&page=3"),2,"SSD",flag) # SSD
    load_on_excel(venex_scrapper("https://www.venex.com.ar/componentes-de-pccomponentes-de-pc/discos-duros-mecanicos"),2,"HDD",flag) # HDD


    # --- GEZATEK ----
    load_on_excel(gezatek_scrapper("https://www.gezatek.com.ar/tienda/procesadores-amd/"),3,"Procesadores AMD",flag) 
    load_on_excel(gezatek_scrapper("https://www.gezatek.com.ar/tienda/procesadores-amd/"),3,"Procesadores AMD",flag) # Procesadores AMD
    load_on_excel(gezatek_scrapper("https://www.gezatek.com.ar/tienda/procesadores-intel/"),3,"Procesadores Intel",flag) # Microprocesadores Intel
    load_on_excel(gezatek_scrapper("https://www.gezatek.com.ar/tienda/mothers-amd-am4/"),3,"Motherboards AMD",flag) # Mothers AMD
    load_on_excel(gezatek_scrapper("https://www.gezatek.com.ar/tienda/mothers-intel-6ta-7ma/"),3,"Motherboards Intel",flag) # Mothers Intel
    load_on_excel(gezatek_scrapper("https://www.gezatek.com.ar/tienda/ram-ddr4/"),3,"Memorias RAM",flag) # Memorias Ram
    load_on_excel(gezatek_scrapper("https://www.gezatek.com.ar/tienda/discos-solidos-ssd/"),3,"SSD",flag) # SSD
    load_on_excel(gezatek_scrapper("https://www.gezatek.com.ar/tienda/discos-rigidos/"),3,"HDD",flag) # HDD
    
except PermissionError:
    print("--ERROR: Para poder ejecutar el programa tenes que cerrar el excel--")











