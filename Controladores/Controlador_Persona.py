
from Models.Persona import Persona
from Vistas.Vista_Persona import Vista_Persona

class Controlador_Persona:
    def __init__(self):
        self.vista = Vista_Persona()
        self.modelo = Persona
