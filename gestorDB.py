import sqlite3

URL ='static\db\Tesla.db'

def ejecutar(query,params) -> int:
    """ Ejecuta una consulta de acción y retorna el número de registros afectadas """
    try:
        with sqlite3.connect(URL) as conn:
            warea = conn.cursor()
            rst = warea.execute(query,params).rowcount
            if rst!=0:
                conn.commit()
    except Exception as e:
        rst = 0
    finally:
            warea.close()
            conn.close()
    return rst

def seleccionar(query,params) -> list:
    """ Ejecuta una consulta de seleccion y retorna los registros seleccionados """
    try:
        with sqlite3.connect(URL) as conn:
            warea = conn.cursor()
            rst = warea.execute(query,params).fetchall()
    except Exception as ex:
        rst = None
    finally:
            warea.close()
            conn.close()
    return rst