from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time


PATH = "/Users/josemaria/Desktop/proyectoMonitores/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get('https://listado.mercadolibre.cl/monitores#D[A:monitores]')
time.sleep(5)

paginas_monitores = [y.get_attribute('href') for y in driver.find_elements_by_class_name("andes-pagination__link.ui-search-link")]


def recopilarInfo(url):

    driver.get(url)
    enlaces = [x.get_attribute('href') for x in driver.find_elements_by_class_name("ui-search-item__group__element.ui-search-link")]
    for item in enlaces:
        
        try:
            driver.get(item)
            estado_producto = driver.find_element_by_class_name("ui-pdp-header__subtitle")
            nombre_producto = driver.find_element_by_class_name("ui-pdp-title")
            precio_producto = driver.find_element_by_class_name("price-tag-fraction")
            color_producto = driver.find_element_by_class_name("ui-pdp-variations")
            stock_producto = driver.find_element_by_class_name("ui-pdp-stock-information")
        
        except (NoSuchElementException, StaleElementReferenceException):
            color_producto = "-"
            stock_producto = "-"
        
        
        if color_producto == "-" or stock_producto == "-":
            print(estado_producto.text + "  |  " + nombre_producto.text + "  |  " + precio_producto.text + "  |  " + color_producto + "  |  " + stock_producto)
        else:
            print(estado_producto.text + "  |  " + nombre_producto.text + "  |  " + precio_producto.text + "  |  " + color_producto.text + "  |  " + stock_producto.text)    

    
for page in paginas_monitores:
    print("The URL is " + page)
    print("\n")
    recopilarInfo(page)
    
driver.quit()








