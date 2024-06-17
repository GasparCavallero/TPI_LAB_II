from Models.FichaMedica import FichaMedica
from Vistas.VistaFichaMedica import VistaFichaMedica


class Controlador_FichaMedica:
    def __init__(self):
        self._vista = VistaFichaMedica()
        self._modelo = FichaMedica()
