from PyQt6 import uic, QtWidgets
from model.usuario import Usuario
from data.usuariodata import UsuarioData

class Registrowindons():
    def __init__(self):
        self.v = uic.loadUi("gui/registrotransferencia.ui")
        self.v.show()

    