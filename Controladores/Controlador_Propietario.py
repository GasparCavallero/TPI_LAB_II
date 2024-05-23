
from Models.Propietario import Propietario
from Vistas.Vista_Propietario import Vista_Propietario

class Controlador_Propietario:
    def __init__(self):
        self.vista = Vista_Propietario()
        self.modelo = Propietario()
