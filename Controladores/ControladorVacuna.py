from Models.Vacuna import Vacuna
from Vistas.VistaVacuna import VistaVacuna
from utilidades import *

class ControladorVacuna:
    def __init__(self):
        self.__modelo = Vacuna
        self.__listaVacunas = self.cargar_lista_vacunas()

    def cargar_lista_vacunas(self):
        lista = []
        with open("Archivos/vacuna.txt", "r") as txt:
            for linea in txt:
                codigo, estado, nombre, = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), bool(estado), nombre))
        return lista

    def get_lista_vacunas(self): # Returnea lista de vacunas
        return self.__listaVacunas

    def buscar_vacuna(self, vacuna): # Busca vacuna vía código en lista de vacunas
        for vacuna in self.__listaVacunas:
            if vacuna.nombre == vacuna:
                return vacuna

    def menu(self):
        opcion = VistaVacuna().menu()
        match opcion:
            case 1:
                ...
            case 2:
                ...
            case _:
                ...

    def guardar_vacunas(self):
        with open("Archivos/vacuna.txt", "w") as txt:
            for linea in self.__listaVacunas:
                txt.write(f"{linea.codigo};{linea.estado};{linea.nombre}\n")

    def crear_nueva_vacuna(self, nombre):
        vacuna = self.__modelo(crearCodigo(self.__listaVacunas), True, nombre)
        self.__listaVacunas.append(vacuna)

    def modificar_vacuna(self, codigo: int):
        for vacuna in self.__listaVacunas:
            if vacuna.codigo == codigo:
                vacuna.nombre = input("Nombre vacuna: ") # Reemplazar con vista
    
    def alta_vacuna(self, codigo: int):
        for vacuna in self.__listaVacunas:
            if vacuna.codigo == codigo:
                vacuna.dar_alta()
    
    def baja_vacuna(self, codigo: int):
        for vacuna in self.__listaVacunas:
            if vacuna.codigo == codigo:
                vacuna.dar_baja()