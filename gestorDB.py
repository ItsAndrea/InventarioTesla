import sqlite3

def ejecutar(query) -> int:
    """ Ejecuta una consulta de acción y retorna el número de registros afectadas """
    try:
        with sqlite3.connect('static\db\Tesla.db') as conn:
            warea = conn.cursor()
            rst = warea.execute(query).rowcount
            if rst!=0:
                conn.commit()
            conn.close()
    except Exception as e:
        rst = 0
    return rst

def seleccionar(query) -> list:
    """ Ejecuta una consulta de seleccion y retorna los registros seleccionados """
    try:
        with sqlite3.connect('static\db\Tesla.db') as conn:
            warea = conn.cursor()                       # Área intermedia para trabajo con la BD
            rst = warea.execute(query).fetchall()    # Se ejecuta el comando y recupera la cantidad de filas (registros) afectados
    except Exception as ex:
        rst = None
    return rst