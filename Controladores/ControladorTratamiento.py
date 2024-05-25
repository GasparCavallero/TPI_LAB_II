
from Models.Tratamiento import Tratamiento
from Vistas.Vista_Tratamiento import Vista_Tratamiento

class Controlador_Tratamiento:
    def __init__(self):
        self.vista = Vista_Tratamiento()
        self.modelo = Tratamiento()
