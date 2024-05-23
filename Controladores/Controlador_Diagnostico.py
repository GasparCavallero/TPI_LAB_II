
from Models.Diagnostico import Diagnostico
from Vistas.Vista_Diagnostico import Vista_Diagnostico

class Controlador_Diagnostico:
    def __init__(self):
        self.vista = Vista_Diagnostico()
        self.modelo = Diagnostico()
