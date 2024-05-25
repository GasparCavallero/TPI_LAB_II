
from Models.Vacuna import Vacuna
from Vistas.Vista_Vacuna import Vista_Vacuna

class Controlador_Vacuna:
    def __init__(self):
        self.vista = Vista_Vacuna()
        self.modelo = Vacuna()
