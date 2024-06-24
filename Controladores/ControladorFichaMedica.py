from Models.FichaMedica import FichaMedica
from Vistas.VistaFichaMedica import VistaFichaMedica
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
                    codigo, estado, mascota, listaVacunas = linea.strip().split(";")
                    self.__listaFichasMedicas.append(self.__modelo(int(codigo), bool(estado), mascota, listaVacunas))

    def crear_nueva_fichaMedica(self, codigoMascota):
        ficha = self.__modelo(codigoMascota, True, codigoMascota, [])
        self.__listaFichasMedicas.append(ficha)

    def get_fichas_medicas(self):
        return self.__listaFichasMedicas

    def buscar_ficha_medica(self, codigo: int):
        for fm in self.__listaFichasMedicas:
            if fm.codigo == codigo:
                return fm
    
    def menu(self):
        opcion = VistaFichaMedica().menu()
        match opcion:
            case 1:
                ...
            case 2:
                ...
            case _:
                ...

    def guardar_fichasmedicas(self):
        for linea in self.__listaFichasMedicas:
            with open(f"Archivos/fichasmedicas/{str(linea.codigo)}.txt", "w") as txt:
                txt.write(f"{linea.codigo};{linea.estado};{linea.mascota};{linea.listaVacunas}")

    # RESOLVER ESCRITURA DE ARCHIVOS