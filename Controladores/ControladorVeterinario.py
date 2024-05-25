
from Models.Veterinario import Veterinario
from Vistas.Vista_Veterinario import Vista_Veterinario

class Controlador_Veterinario:
    def __init__(self):
        self.vista = Vista_Veterinario()
        self.modelo = Veterinario()
