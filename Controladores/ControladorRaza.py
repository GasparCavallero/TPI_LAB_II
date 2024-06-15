from Models.Raza import Raza
# from Vistas.Vista_Raza import Vista_Raza
from utilidades import *

class Controlador_Raza:
    def __init__(self):
        # self._vista = Vista_Raza() COMENTADO HASTA QUE EXISTA VISTA_RAZA
        self.__modelo = Raza
        self.__listaRazas = self.cargarListaRazas()

    def cargarListaRazas(self):
        with open("Archivos/raza.txt", "r") as txt:
            lista = []
            for linea in txt:
                codigo, nombre, tipoAnimal = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), nombre, tipoAnimal))
            return lista

    def getListaRazas(self):
        return self.__listaRazas

    def buscarRaza(self, raza):
        for i in self.listaRazas:
            if i.nombre == raza:
                return i

    def mostrar_Datos(self):
        self._vista.Visualizar_Datos(self._modelo.getDatos_Raza())