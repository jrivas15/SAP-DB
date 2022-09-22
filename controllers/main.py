from PySide6.QtWidgets import QWidget, QMessageBox,QFileDialog
from PySide6.QtCore import Qt
from PySide6 import QtCore
from ui_files.main_db import Ui_Form
from msg_boxes.msg_box import confirmationBox,errorBoxes,okBoxes, questionBox
from db import querys
import os
import platform
sistema_operativo = platform.system()

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Crear DB")
        #BTN
        self.btn_cerrar.clicked.connect(lambda:self.close())
        self.btn_crear.clicked.connect(self.crear)
        self.ip_line.setText("192.168.10.133")
        self.progreso = 0

    def crear(self):
        ip = self.ip_line.text()
        print("IP: ", ip)
        if len(ip) > 7 :
            resp = questionBox("Crear DB", "Desea crear una base de datos?")
            if resp == QMessageBox.Yes:
                querys.crear_database(ip)
                self.aumentar_progreso()
                #Crear tablas
                #querys.crear_tablas_parqueadero(ip, db = 'parqueadero')
            
            resp = confirmationBox("Importar DB", "Desea importar una base de datos?")
            if resp ==QMessageBox.Yes:
                path_import = QFileDialog.getOpenFileName(self, filter="SQL (*.sql)")[0]
                print(path_import)
                if len(path_import) > 0:
                    if sistema_operativo == 'Darwin':
                        path_mysql = '/usr/local/mysql/bin/mysql'
                        os.system(f"{path_mysql} -u root -p123456789 parqueadero < {path_import} ")
                        okBoxes("Import", "Base de datos importada exitosamente")
                    elif sistema_operativo == "Windows":
                        path_msqldump = 'C:\Program Files\MySQL\MySQL Server 5.5\bin\mysqldump'
                        print(path_msqldump)
                        os.system(f'"{path_msqldump} -u root -p553051922428536000 parqueadero < {path_import}"')

            resp = confirmationBox("Fix consecutivos facturas", "Aplicar cambios consecutivos importar una base de datos?")
            if resp == QMessageBox.Yes:
                cosecutivo_inical = 208577
                data = querys.leer_consecutivos_facturas(cosecutivo_inical, ip= ip)
                #print(data)
                consecutivos=[]
                for registros in data:
                    consecutivos.append(registros[1])
                    
                #alterar facturas
                print(len(consecutivos))
                factura_inicial = 41899
                id_resolucion = 3
                prefijo = "PPA"
                i = 1
                for consecutivo in consecutivos:
                    #leer valor base
                    #print(querys.leer_valor_pagado(consecutivo=consecutivo, ip=ip))
                    valor_pagado = querys.leer_valor_pagado(consecutivo=consecutivo, ip=ip)[0][0]
                    valor_iva =valor_pagado*0.19
                    valor_base = valor_pagado*(0.81)
                    data_fix = (factura_inicial, valor_iva,valor_base, prefijo, id_resolucion)
                    #ACTUALIZAR INFO
                    querys.fix_facturas(consecutivo= consecutivo, data= data_fix, ip=ip)
                    progreso = (i/len(consecutivos))*100 
                    print(f"VP={valor_pagado} IVA={valor_iva} Base={valor_base} factura = {factura_inicial} Cons = {consecutivo} \
                         {i} de {len(consecutivos)}  %{progreso}")
                    i +=1
                    self.aumentar_progreso(round(progreso))    
                    factura_inicial += 1
        else:
            pass

    def aumentar_progreso(self, add_progreso= 5):
        #self.progreso += add_progreso
        #self.progressBar.setValue( self.progreso )
        self.progressBar.setValue(add_progreso)