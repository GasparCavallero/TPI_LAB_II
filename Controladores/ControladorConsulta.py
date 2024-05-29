from Models.Consulta import Consulta
from Vistas.Vista_Consulta import Vista_Consulta


class Controlador_Consulta:
    def __init__(self):
        self._vista = Vista_Consulta()
        self._modelo = Consulta()
