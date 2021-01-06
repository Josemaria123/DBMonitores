import psycopg2


def connectDB():

    try:
        conn = psycopg2.connect(host="127.0.0.1", database = "MonitoresMercadoLibre", user = "postgres", password = "grinblue9", port="5432")
        
        print("Conexion Exitosa")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    return conn

#1. Creo el cursor
cur = conn.cursor()

#Connection to the database
def tableCreation():


    # 2. Ejecuto algun query
    #Crear tabla de monitores
    crearTabla = "CREATE TABLE monitores (id INTEGER PRIMARY KEY, nombre VARCHAR(50), precio INTEGER);" 
    cur.execute(crearTabla)
    #Guardar los cambios
    conn.commit()
    # 3. Cierro el cursor
    cur.close()

def dropTable():
    cur = conn.cursor()
    dropTable = "DROP TABLE monitores;"
    cur.execute(dropTable)
    conn.commit()
    cur.close()


limpiarDB = int(input("Para borrar la tabla monitores aprete 1: "))
if limpiarDB == 1:
    dropTable()

conn.close()