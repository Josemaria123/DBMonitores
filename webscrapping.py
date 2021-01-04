from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import psycopg2
import time


try:
    conn = psycopg2.connect(host="127.0.0.1", database = "MonitoresMercadoLibre", user = "postgres", password = "grinblue9", port="5432")
    
    print("Conexion Exitosa")
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

cur = conn.cursor()
#Connection to the database
def tableCreation():

    #1. Creo el cursor

    # 2. Ejecuto algun query
    #Crear tabla de monitores
    crearTabla = "CREATE TABLE monitores (id INTEGER PRIMARY KEY, nombre VARCHAR(50), precio INTEGER);" 
    cur.execute(crearTabla)
    #Guardar los cambios
    conn.commit()
    # 3. Cierro el cursor
    cur.close()


tableCreation()

def dropTable():
    cur = conn.cursor()
    dropTable = "DROP TABLE monitores;"
    cur.execute(dropTable)
    conn.commit()
    cur.close()
    

PATH = "/Users/josemaria/Desktop/proyectoMonitores/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get('https://listado.mercadolibre.cl/monitores#D[A:monitores]')
time.sleep(5)

try:

    nombre_producto = driver.find_elements_by_class_name('ui-search-result__content-wrapper')
    info_dic = {}
    for value in range(len(nombre_producto)):
        
        info_dic["producto_%s" %value] = nombre_producto[value].text
        
    print(info_dic)
    # precio = driver.find_element_by_class_name('price-tag-fraction')
    # print("El nombre del producto es {}".format(nombre_producto.text))
    # print("El precio es de $ {}".format(precio.text))


finally:
    driver.close()

limpiarDB = int(input("Para borrar la tabla monitores aprete 1: "))
if limpiarDB == 1:
    dropTable()

conn.close()


