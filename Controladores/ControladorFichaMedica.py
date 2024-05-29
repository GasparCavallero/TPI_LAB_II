from Models.FichaMedica import FichaMedica
from Vistas.Vista_FichaMedica import Vista_FichaMedica


class Controlador_FichaMedica:
    def __init__(self):
        self._vista = Vista_FichaMedica()
        self._modelo = FichaMedica()
