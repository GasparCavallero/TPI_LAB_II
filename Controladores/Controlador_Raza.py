
from Models.Raza import Raza
from Vistas.Vista_Raza import Vista_Raza

class Controlador_Raza:
    def __init__(self):
        self.vista = Vista_Raza()
        self.modelo = Raza()
