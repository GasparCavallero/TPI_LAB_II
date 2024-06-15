from Models.Consulta import Consulta
from Vistas.VistaConsulta import VistaConsulta


class Controlador_Consulta:
    def __init__(self):
        self._vista = VistaConsulta()
        self._modelo = Consulta()
