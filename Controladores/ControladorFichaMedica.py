from Models.FichaMedica import FichaMedica
from utilidades import *
import os

archivos = os.listdir("Archivos/fichasmedicas")

class ControladorFichaMedica:
    def __init__(self):
        self.__modelo = FichaMedica
        self.__listaFichasMedicas = []
        self.cargar_fichas_medicas()

    def cargar_fichas_medicas(self):
        for archivo in archivos:
            with open(f"Archivos/fichasmedicas/{archivo}", "r") as txt:
                for linea in txt:
                    codigo, estado, mascota, listaConsultas, listaVacunas = linea.strip().split(";")
                    self.__listaFichasMedicas.append(self.__modelo(int(codigo), bool(estado), mascota, listaConsultas, listaVacunas))

    def crear_nueva_fichaMedica(self, codigoMascota):
        ficha = self.__modelo(codigoMascota, True, codigoMascota, [], [])
        self.__listaFichasMedicas.append(ficha)

    def get_fichas_medicas(self):
        return self.__listaFichasMedicas
