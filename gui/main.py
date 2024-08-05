from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QApplication,QTableWidgetItem
from data.historial import HistorialData
from data.transferencia import Transferencia_data
from data.ciudadesData import CiudadesData
from PyQt6.QtCore import QDate

from model.movimientos import Transferencia
from data.depositodata import Deposito_data
from model.movimientos import DepositoInternacinal,Transferencia
class MainWindons():
    def __init__(self):
        self.main = uic.loadUi("gui/main.ui")
        self.initGUI()     
        self.main.showMaximized()

    def  initGUI(self):
        self.main.btnRegistrar_transferencia.triggered.connect(self.abrirRegistro)
        self.main.btnReportar_transferencia.triggered.connect(self.abrirDeposito)  
        self.main.btnHistorial_de_transferencia.triggered.connect(self.AbrirHistorial) 
        self.registro=uic.loadUi("gui/registrotransferencia.ui")
        self.deposito=uic.loadUi("gui/deposito.ui")
        self.historial=uic.loadUi("gui/historial.ui")
    def abrirRegistro(self):
        self.registro.btnregistrar.clicked.connect(self.registrarTranssaccion)
        self.registro.show()
    def abrirDeposito(self):
        self.deposito.btnregistrar.clicked.connect(self.RegistrarDeposito)
        self.deposito.show()
        self.LlenarCiudades()
    def AbrirHistorial(self):
        self.historial.btnbuscar.clicked.connect(self.buscar)
        self.historial.tblhistorial.setColumnWidth(1,400)
        self.historial.tblhistorial.setColumnWidth(3,250)
        self.historial.tblhistorial.setColumnWidth(4,400)
        self.historial.show()
##################TRANSFERENCIAS##################
    def registrarTranssaccion(self):
        if self.registro.cbtipo.currentText()=="---Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Seleccione un tipo de documento")
            mBox.exec()
            self.registro.cbtipo.setFocus()
        elif len(self.registro.txtdocumento.text())<4:
            mBox = QMessageBox()
            mBox.setText("Debe ingresar un documento válido")
            mBox.exec()
            self.registro.txtdocumento.setFocus() 
        elif self.registro.cbmotivo.currentText()=="---Seleccione una opción": 
            mBox = QMessageBox()
            mBox.setText("Seleccione un motivo")
            mBox.exec()
            self.registro.cbmotivo.setFocus()
        elif  not self.registro.txtmonto.text().isnumeric():
            mBox = QMessageBox()
            mBox.setText("Ingrese un monto válido")
            mBox.exec()
            self.registro.txtmonto.setText("0")
            self.registro.txtmonto.setFocus()
        else:
            transferencia=Transferencia(
                tipo=self.registro.cbtipo.currentText(),
                documento=self.registro.txtdocumento.text(),
                motivo=self.registro.cbmotivo.currentText(),
                monto=int(self.registro.txtmonto.text()),
                dolares=self.registro.checkdolares.isChecked(),
                internacional=self.registro.checkinternacional.isChecked()
            )
           
            objData=Transferencia_data()
            if objData.registar(info=transferencia):
                mBox = QMessageBox()
                mBox.setText("Registro exitoso")
                mBox.exec()
                self.LimpiarTrasferencia()
                
            else:
                mBox = QMessageBox()
                mBox.setText("Error al registrar")
            
            mBox.exec()
            
    def LimpiarTrasferencia(self):
        self.registro.cbtipo.setCurrentIndex(0)
        self.registro.txtdocumento.setText("")
        self.registro.cbmotivo.setCurrentIndex(0)
        self.registro.txtmonto.setText("0")
        self.registro.checkdolares.setChecked(False)
        self.registro.checkinternacional.setChecked(False)
        self.registro.txtdocumento.setFocus()
    
######DEPOSITOS########
    def LlenarCiudades(self):
       objData=CiudadesData()
       datos=objData.listaCiudades()
       for item in datos:
         self.deposito.cbnacimiento.addItem(item[1])
    
    def Validarcampos(self)->bool:
        if not self.deposito.txtdocumento.text() or not self.deposito.txtprimernombre.text() or not self.deposito.txtprimerapellido.text() or not self.deposito.txtmonto.text() or self.deposito.cbmotivo.currentText()=="---Seleccione una opción" or self.deposito.cbnacimiento.currentText()=="---Seleccione una opción" or self.deposito.cbsexo.currentText()=="---Seleccione una opción" or self.deposito.cbtipo.currentText()=="---Seleccione una opción":
            return False
        else:
            return True
    
    def RegistrarDeposito(self):
        mBox = QMessageBox()
        if not  self .Validarcampos():
            mBox = QMessageBox()
            mBox.setText("Debe llenar los campos obligatorios")
            mBox.exec()
        elif  self.deposito.checkterminos.isChecked()==False:
            mBox.setText("Debe aceptar los terminos y condiciones")
            self.deposito.checkterminos.setFocus()
            mBox.exec()
        elif not self.deposito.txtmonto.text().isnumeric() or float(self.deposito.txtmonto.text())<1:
            mBox.setText("El monto debe ser mayor a 0")
            self.deposito.txtmonto.setText("0")
            self.deposito.txtmonto.setFocus()
            mBox.exec()
        else:
            fechan=self.deposito.txtfecha.date().toPyDate()
            deposito=DepositoInternacinal(
                tipo=self.deposito.cbtipo.currentText(),
                documento=self.deposito.txtdocumento.text(),
                monto=float(self.deposito.txtmonto.text()),
                motivo=self.deposito.cbmotivo.currentText(),
                sexo=self.deposito.cbsexo.currentText(),
                lugarNacimiento=self.deposito.cbnacimiento.currentText(),
                nombre1=self.deposito.txtprimernombre.text(),
                nombre2=self.deposito.txtsegundonombre.text(),
                apellido1=self.deposito.txtprimerapellido.text(),
                apellido2=self.deposito.txtsegundoapellido.text(),
                terminos=self.deposito.checkterminos.isChecked(),
                fechaNacimiento=fechan
            )
            objData=Deposito_data()
            if objData.registar(info=deposito):
                mBox = QMessageBox()
                mBox.setText("Deposito exitoso")
                mBox.exec()
                self.LimpiarDeposito()
            else:
                mBox = QMessageBox()
                mBox.setText("Deposito no registrado")
                mBox.exec()
                
    def LimpiarDeposito(self):
        self.deposito.cbtipo.setCurrentIndex(0)
        self.deposito.cbmotivo.setCurrentIndex(0)
        self.deposito.cbsexo.setCurrentIndex(0)
        self.deposito.cbnacimiento.setCurrentIndex(0)
        self.deposito.txtdocumento.setText("")
        self.deposito.txtprimernombre.setText("")
        self.deposito.txtsegundonombre.setText("")
        self.deposito.txtprimerapellido.setText("")
        self.deposito.txtsegundoapellido.setText("")
        miFecha=QDate(2000,0,0)
        self.deposito.txtfecha.setDate(miFecha)
        self.deposito.txtmonto.setText("0")
        self.deposito.checkterminos.setChecked(False)
        self.deposito.txtdocumento.setFocus()
####HISTORIAL DE TRANSACCIONES#####
  
         
    def buscar(self):
        his=HistorialData()
        data=his.buscarporfecha(self.historial.txtfechadesde.date().toPyDate(),self.historial.txtfechahasta.date().toPyDate(),self.historial.txtdocumento.text(),self.historial.cbtipo.currentText())
        fila =0
        self.historial.tblhistorial.setRowCount(len(data))
        for item in data:
            self.historial.tblhistorial.setItem(fila,0,QTableWidgetItem(str(item[0])))
            self.historial.tblhistorial.setItem(fila,1,QTableWidgetItem("{} {} {} {}".format(str(item[10]),str(item[11]),str(item[12]),str(item[13]))))
            if item[6]=='True': 
                self.historial.tblhistorial.setItem(fila,2,QTableWidgetItem("$/"+str(item[2]))) 
            else:
                self.historial.tblhistorial.setItem(fila,2,QTableWidgetItem("S/"+str(item[2]))) 
                
            if item[5]=='True': 
                self.historial.tblhistorial.setItem(fila,3,QTableWidgetItem("Transferencia Internacional-" + str(item[9])) )
            else:
                self.historial.tblhistorial.setItem(fila,3,QTableWidgetItem("Transferencia Nacional") ) 
            self.historial.tblhistorial.setItem(fila,4,QTableWidgetItem(str(item[7])))
            if item[16]=='True':
                self.historial.tblhistorial.setItem(fila,5,QTableWidgetItem("Aprobado"))
            else:
                self.historial.tblhistorial.setItem(fila,5,QTableWidgetItem("Pendiente"))
            
            fila=fila+1
            
    def llenarHistorial(self):
        pass