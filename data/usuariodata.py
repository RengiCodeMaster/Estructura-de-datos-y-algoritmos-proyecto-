import conexion as con
from model.usuario import Usuario
class Usuariodata():
    def __init__(self) :
        try:
            self.db=con.Conexion().conectar()
            self.cursor=self.db.cursor()
            sql_crear_admin = """INSERT INTO usuarios values(null,'{}','{}','{}')""".format("administrador","admin","admin")
            self.cursor.execute(sql_crear_admin)
            self.db.commit()
        except Exception as ex:
            print("Ya se creo el usuiario",ex)   

    def login(self,usuario:Usuario):
        self.db=con.Conexion().conectar()
        self.cursor=self.db.cursor()
        res=self.cursor.execute("SELECT * FROM usuarios WHERE usuario='{}' AND clave='{}'".format(usuario._usuario,usuario._clave))
        fila=res.fetchone()
        if fila:
            usuario=Usuario(nombre=fila[1],usuario=fila[2])
            self.cursor.close()
            self.db.close()
            return usuario
        else:
            self.cursor.close()
            self.db.close()
            return None