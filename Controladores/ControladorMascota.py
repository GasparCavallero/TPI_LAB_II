from Models.Mascota import Mascota
from Models.Raza import Raza
from Models.Propietario import Propietario
from Models.FichaMedica import FichaMedica
from utilidades import *

class Controlador_Mascota:
    def __init__(self):
        self.__modelo = Mascota
        self.__listaMascotas = self.cargar_lista_mascotas()

    def cargar_lista_mascotas(self):
        lista = []
        with open("Archivos/mascota.txt", "r") as txt:
            for linea in txt:
                codigo, estado, Propietario, Raza, FichaMedica, nombre, fechaNac = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), bool(estado), Propietario, Raza, FichaMedica, nombre, fechaNac))
        return lista
    
    def codigoaobj_propietario(self, codigoBusqueda: int):
        ...

    def codigoaobj_fichamedica(self, codigoBusqueda: int):
        lista = []
        with open("Archivos/fichamedica.txt", "r") as txt:
            for linea in txt:
                codigo, nombre, tipoAnimal = linea.strip().split(";")
                lista.append(Raza(int(codigo), nombre, tipoAnimal))
        return buscarObjetoViaCodigo(codigoBusqueda, lista)

    def codigoaobj_raza(self, codigoBusqueda: int):
        lista = []
        with open("Archivos/raza.txt", "r") as txt:
            for linea in txt:
                codigo, nombre, tipoAnimal = linea.strip().split(";")
                lista.append(Raza(int(codigo), nombre, tipoAnimal))
        return buscarObjetoViaCodigo(codigoBusqueda, lista)
    
    def get_lista_mascotas(self):
        return self.__listaMascotas
