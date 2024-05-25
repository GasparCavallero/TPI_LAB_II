
from Models.Mascota import Mascota
from Vistas.Vista_Mascota import Vista_Mascota

class Controlador_Mascota:
    def __init__(self):
        self.vista = Vista_Mascota()
        self.modelo = Mascota()
