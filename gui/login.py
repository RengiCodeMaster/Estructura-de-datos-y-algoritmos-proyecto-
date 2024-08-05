from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from data.usuariodata import Usuariodata
from gui.main import MainWindons
from model.usuario import Usuario
from model import usuario

class Login():
    def __init__(self):
        self.login = uic.loadUi("gui/login.ui")  # Cargar la interfaz de usuario desde el archivo "gui/login.ui"
        self.initGUI()  # Inicializar la interfaz de usuario
        self.login.lblmensaje.setText("")  # Establecer el texto vacío en el QLabel lblmensaje
        self.login.show()  # Mostrar la ventana de inicio de sesión

    def ingresar(self):
        if len(self.login.txtusuario.text()) < 2:  # Verificar si el campo de usuario tiene menos de 2 caracteres
            self.login.lblmensaje.setText("Ingrese un usuario")  # Establecer el mensaje de error en el QLabel lblmensaje
            self.login.txtusuario.setFocus()  # Establecer el foco en el campo de usuario
        elif len(self.login.txtclave.text()) < 3:  # Verificar si el campo de clave tiene menos de 3 caracteres
            self.login.lblmensaje.setText("Ingrese una clave")  # Establecer el mensaje de error en el QLabel lblmensaje
            self.login.txtclave.setFocus()  # Establecer el foco en el campo de clave
        else:
            self.login.lblmensaje.setText("")  # Establecer el texto vacío en el QLabel lblmensaje
            usu = Usuario(usuario=self.login.txtusuario.text(), clave=self.login.txtclave.text())  # Crear un objeto Usuario con los valores de los campos de usuario y clave
            usudata = Usuariodata()  # Crear un objeto Usuariodata
            res = usudata.login(usu)  # Llamar al método login de Usuariodata y pasarle el objeto Usuario
            if res:  # Si el resultado es verdadero
                self.main = MainWindons()  # Crear un objeto MainWindons
                self.login.hide()  # Ocultar la ventana de inicio de sesión
            else:
                self.login.lblmensaje.setText("Usuario o clave incorrecta")  # Establecer el mensaje de error en el QLabel lblmensaje

    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)  # Conectar el botón btnAcceder con el método ingresar
