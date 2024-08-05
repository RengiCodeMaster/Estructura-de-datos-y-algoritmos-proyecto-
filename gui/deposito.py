from PyQt6 import uic, QtWidgets
from model.usuario import Usuario
from data.usuariodata import UsuarioData

class Registrowindons():
    def __init__(self):
        self.v = uic.loadUi("gui/deposito.ui")
        self.v.show()
