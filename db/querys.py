from .conexion import create_connection
from mysql.connector import Error
from msg_boxes import msg_box

class Query() : # Clase para lectura

    def __init__(self, sql, error, puntero, funcion, data, okText, ip ="localhost"):
        self.conn = create_connection(ip)
        self.data = []
        if funcion == "leer":
            try:
                cursor = self.conn.cursor()
                cursor.execute(sql)
                if puntero == "1":
                    self.data = cursor.fetchone()
                elif puntero == "*":
                    self.data = cursor.fetchall()
            except Error as e:
                print(error + str(e))
                msg_box.errorBoxes("Error", f"{error} : {e}")
            finally:
                if self.conn:
                    cursor.close()
                    self.conn.close()
        elif funcion == "editar" or funcion == "crear" or funcion == "eliminar":
            try:
                cursor = self.conn.cursor()
                if funcion =="eliminar":
                    cursor.execute(sql)
                else:
                    cursor.execute(sql, data)
                # Guarda cambios con un commit
                self.conn.commit()
                #print(okText)
                self.error = False
                if funcion == "editar" or funcion == "crear":
                    #msg_box.okBoxes("Información", okText)
                    pass

            except Error as e:
                print(error + str(e))
                msg_box.errorBoxes("Error", f"{error} : {e}")
                self.error = True
            finally:
                if self.conn:
                    # Finaliza el cursor y la conexion
                    cursor.close()
                    self.conn.close()


def crear_database(ip = 'localhost'):
        sqls =[]
        sqls.append("CREATE DATABASE parqueadero")
        sqls.append("CREATE DATABASE sap")
        sqls.append("CREATE DATABASE test")
        conn = create_connection(ip)
        cursor = conn.cursor()
        for sql in sqls:
            cursor.execute(sql)
        cursor.close()
        conn.close()

#Tablas para parqueadero
def crear_tablas_parqueadero(ip ='localhost', db =''):
    sqls = []
    sqls.append("CREATE TABLE `auditoria` (\
                `id` int(11) NOT NULL AUTO_INCREMENT,\
                `Cedula` varchar(16) DEFAULT '', \
                `Empleado` varchar(50) DEFAULT '',\
                `Fecha` date DEFAULT NULL,\
                `Hora` varchar(8) DEFAULT '', \
                `Novedad` varchar(80) DEFAULT '',\
                `Tipo` varchar(1) DEFAULT 'S', \
                PRIMARY KEY (`id`) \
                ) ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=utf8\
            ")
    sqls.append("CREATE TABLE `clientes` (\
                `Id` varchar(20) NOT NULL DEFAULT '',\
                `TipoId` varchar(4) DEFAULT '',\
                `DV` varchar(1) DEFAULT '',\
                `Placa` varchar(50) DEFAULT '',\
                `RazonSocial` varchar(50) DEFAULT '',\
                `Nombres` varchar(30) DEFAULT '',\
                `Apellidos` varchar(30) DEFAULT '',\
                `Direccion` varchar(60) DEFAULT '',\
                `Telefonos` varchar(20) DEFAULT '',\
                `Email` varchar(50) DEFAULT '',\
                `Municipio` varchar(5) DEFAULT '',\
                PRIMARY KEY (`Id`)\
                ) ENGINE=MyISAM DEFAULT CHARSET=utf8 \
                ")

    conn = create_connection(ip, db)
    cursor = conn.cursor()
    for sql in sqls:
        cursor.execute(sql)
    cursor.close()
    conn.close()

def leer_consecutivos_facturas(consecutivo_ini,ip):
    sql =f"SELECT * from liquidetallado WHERE ConsMov >= {consecutivo_ini} AND ValorPagado < {100000} AND ValorPagado > {0}"
    errorText = "Error leyendo usuarios by user "
    data = Query(sql, errorText, "*", "leer", [], "",ip= ip).data
    return data
def leer_valor_pagado(consecutivo,ip):
    sql =f"SELECT ValorPagado from liquidetallado WHERE ConsMov = {consecutivo}"
    errorText = "Error leyendo valor pagado "
    data = Query(sql, errorText, "*", "leer", [], "",ip= ip).data
    return data
def fix_facturas(consecutivo,data, ip):
    #SQL
    sql = f"""UPDATE liquidetallado SET FacturaNo = %s, 
                                    ValorIVA = %s, 
                                    ValorBase = %s,
                                    Prefijo = %s,
                                    IdResol =%s 
                                WHERE ConsMov = {consecutivo}
                                    """
    errorText = "Error actualizando usuario!"
    okText = "Producto actualizado exitosamente!"
    Query(sql, errorText, "1", "editar",data, okText, ip=ip)




        