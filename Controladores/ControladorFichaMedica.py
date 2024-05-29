from Models.FichaMedica import FichaMedica
from Vistas.Vista_FichaMedica import Vista_FichaMedica


class Controlador_FichaMedica:
    def __init__(self):
        self.vista = Vista_FichaMedica()
        self.modelo = FichaMedica()
