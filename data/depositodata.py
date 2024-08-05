import conexion as con
from model.movimientos import DepositoInternacinal
from datetime import datetime
class Deposito_data():
    def __init__(self)->None:
        try:
             self.db=con.Conexion().conectar()
             self.cursor=self.db.cursor()
             sql_crear_depositos = """CREATE TABLE IF NOT EXISTS depositos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                monto NUMERIC,
                tipo TEXT ,
                documento TEXT,
                internacional BOOLEAN,
                dolares BOOLEAN,
                fecha_registro DATETIME,
                fecha_nacimiento DATETIME,
                motivo TEXT, 
                primer_nombre TEXT, 
                segunto_nombre TEXT,
                primer_apellido TEXT,
                segundo_apellido TEXT,
                sexo TEXT,
                ciudad_nacimiento TEXT,
                terminos BOOLEAN     
            )"""
             self.cursor.execute(sql_crear_depositos)
             self.db.commit()
             self.cursor.close()
             self.db.close()
             print("tabla de deposito creada")
        except Exception as ex:
            print("tabla de deposito ok",ex)
            
        
    def registar(self,info:DepositoInternacinal):
        fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        self.db=con.Conexion().conectar()
        self.cursor=self.db.cursor()
        self.cursor.execute("""INSERT INTO depositos VALUES(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._monto,info._tipo,info._documento,info._internacional,info._dolares,
                fecha,info._fechaNacimiento,info._motivo,info._nombre1,info._nombre2,info._apellido1,info._apellido2,info._sexo,info._lugarNacimiento,info._terminos))
        self.db.commit()
        if self.cursor.rowcount==1:
            return True
        else:
            return False
       
        
        
        