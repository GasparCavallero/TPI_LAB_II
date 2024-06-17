from Models.Tratamiento import Tratamiento
from Vistas.VistaTratamiento import Vista_Tratamiento


class Controlador_Tratamiento:
    def __init__(self):
        self._vista = Vista_Tratamiento()
        self._modelo = Tratamiento()
