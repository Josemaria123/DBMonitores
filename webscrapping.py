from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import psycopg2
#Connection to the DB
conn = psycopg2.connect(host = "", database = "MonitoresMercadoLibre", user = "postgres", password = "grinblue9")

#1. Creo el cursor
cur = con.cursor()

# 2. Ejecuto algun query
cur.execute("CREATE TABLE monitores (Id INTEGER PRIMARY KEY, Nombre VARCHAR(50), Precio INTEGER)")

# 3. Guardo los cambios
cur.commit()

# Cierro el cursor
cur.close()

#Crear tabla de monitores

PATH = "/Users/josemaria/Desktop/proyectowebscrapping/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get('https://listado.mercadolibre.cl/monitores#D[A:monitores]')

try:

    nombre_producto = driver.find_element_by_class_name('ui-search-item__title')
    precio = driver.find_element_by_class_name('price-tag-fraction')
    print("El precio es de {}".format(nombre_producto.text))
    print("El precio es de $ {}".format(precio.text))


finally:
    driver.close()



conn.close()
