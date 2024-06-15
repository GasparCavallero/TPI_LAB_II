from Models.Raza import Raza
# from Vistas.Vista_Raza import Vista_Raza
from utilidades import *

class Controlador_Raza:
    def __init__(self):
        # self._vista = Vista_Raza() COMENTADO HASTA QUE EXISTA VISTA_RAZA
        self.__modelo = Raza()
        self.__listaRazas = []
        cargarArchivoEnLista("Archivos/raza.txt", self.__listaRazas, self.__modelo)

    """def cargarRaza(self):
        with open("Archivos\\raza.txt", "r") as file:
            linea = file.readlines()
        for l in linea:
            nombre = l.strip().split(",")
            self.listaRazas.append(Raza(nombre))
        return self.listaRazas"""

    def buscarRaza(self, raza):
        for i in self.listaRazas:
            if i.nombre == raza:
                return i

    def mostrar_Datos(self):
        self._vista.Visualizar_Datos(self._modelo.getDatos_Raza())
