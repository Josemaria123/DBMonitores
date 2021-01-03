from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import psycopg2

#Connection to the database
def dbconection():

    try:
        conn = psycopg2.connect(host="127.0.0.1", database = "MonitoresMercadoLibre", user = "postgres", password = "grinblue9", port="5432")
        
        print("Conexion Exitosa")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    #1. Creo el cursor
    cur = conn.cursor()

    # 2. Ejecuto algun query
    #Crear tabla de monitores
    crearTabla = "CREATE TABLE monitores (id INTEGER PRIMARY KEY, nombre VARCHAR(50), precio INTEGER)" 
    cur.execute(crearTabla)
    #Guardar los cambios
    conn.commit()
    # 3. Cierro el cursor
    cur.close()

    conn.close()

PATH = "/Users/josemaria/Desktop/proyectoMonitores/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get('https://listado.mercadolibre.cl/monitores#D[A:monitores]')

dbconection()
try:

    nombre_producto = driver.find_element_by_class_name('ui-search-item__title')
    precio = driver.find_element_by_class_name('price-tag-fraction')
    print("El precio es de {}".format(nombre_producto.text))
    print("El precio es de $ {}".format(precio.text))


finally:
    driver.close()



