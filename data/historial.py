import conexion as con

class HistorialData():
    def buscarporfecha(self, fechadesde, fechahasta, documento, tipo):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        
        # Agregar impresión para depuración
        print(f"Consulta SQL con fechas: desde {fechadesde} hasta {fechahasta}, documento: {documento}, tipo: {tipo}")
        
        sql = """SELECT T.id as transaccion, D.*
                 FROM transferencias T 
                 INNER JOIN depositos D ON D.tipo = T.tipo AND D.documento = T.documento 
                 WHERE T.fecha_registro >= ? AND T.fecha_registro <= ? 
                 AND D.documento = ? AND D.tipo = ?"""
        res = self.cursor.execute(sql, (fechadesde, fechahasta, documento, tipo))
        data = res.fetchall()
        return data
