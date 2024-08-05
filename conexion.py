import sqlite3

class Conexion:
    def __init__(self):
        try:
            self.con = sqlite3.connect('sistema.db')
            self.crear_tabla()
        except Exception as ex:
            print(ex)
    
    def crear_tabla(self):  
            sql_crear_tabla = """CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                usuario TEXT UNIQUE,
                clave TEXT NOT NULL
            )"""
            cur = self.con.cursor()
            cur.execute(sql_crear_tabla)
            cur.close()
            self.crear_admin()
        
        

    
    def conectar(self):
        return self.con
                        


    
    


