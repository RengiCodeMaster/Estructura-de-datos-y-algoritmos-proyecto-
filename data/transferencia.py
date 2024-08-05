import conexion as con
from model.movimientos import Transferencia
from datetime import datetime
class Transferencia_data():
    def __init__(self)->None:
        try:
             self.db=con.Conexion().conectar()
             self.cursor=self.db.cursor()
             sql_crear_transferencias = """CREATE TABLE IF NOT EXISTS transfrencias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                monto NUMERIC,
                tipo TEXT ,
                documento TEXT,
                internacional BOOLEAN,
                dolares BOOLEAN,
                fecha_registro DATETIME,
                verificado BOOLEAN ,
                motivo TEXT 
            )"""
             self.cursor.execute(sql_crear_transferencias)
             self.db.commit()
             self.cursor.close()
             self.db.close()
             print("tabla de transferencias creada")
        except Exception as ex:
            print("tabla de transferencias ok",ex)
            
        
    def registar(self,info:Transferencia):
        fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        self.db=con.Conexion().conectar()
        self.cursor=self.db.cursor()
        self.cursor.execute("""INSERT INTO transferencias VALUES(null,'{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._monto,info._tipo,info._documento,info._internacional,info._dolares,
                fecha,False,info._motivo))
        self.db.commit()
        if self.cursor.rowcount==1:
            return True
        else:
            return False
       
        
        
        