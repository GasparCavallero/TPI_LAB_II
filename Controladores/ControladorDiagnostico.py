from Models.Diagnostico import Diagnostico
from Vistas.VistaDiagnostico import VistaDiagnostico
from utilidades import *

class ControladorDiagnostico:
    def __init__(self):
        self.__modelo = Diagnostico
        self.__listaDiagnosticos = self.cargar_lista_diagnosticos()

    def cargar_lista_diagnosticos(self):
        lista = []
        with open("Archivos/diagnostico.txt", "r") as txt:
            for linea in txt:
                codigo, mascota, fecha, descripcion = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), mascota, fecha, descripcion))
        return lista

    def get_lista_diagnosticos(self):
        return self.__listaDiagnosticos

    def crear_nuevo_diagnostico(self, mascota, descripcion):
        diagnostico = self.__modelo(crearCodigo(self.__listaDiagnosticos), mascota, fechaActual(), descripcion)
        self.__listaDiagnosticos.append(diagnostico)

    def get_diagnosticos_via_codigo(self, codigo):
        # get todos los tratamientos que matcheen el código, para construir ficha médica
        ...

    def guardar_diagnosticos(self):
        with open("Archivos/diagnostico.txt", "w") as txt:
            for linea in self.__listaDiagnosticos:
                txt.write(f"{linea.codigo};{linea.mascota};{linea.fecha};{linea.descripcion}\n")

    def eliminar_diagnostico(self, codigo: int):
        for diagnostico in self.__listaDiagnosticos:
            if diagnostico.codigo == codigo:
                self.__listaDiagnosticos.remove(diagnostico)

    def menu(self):
        opcion = VistaDiagnostico().menu()
        match opcion:
            case 1:
                ...
            case 2:
                ...

    def modificar_diagnostico(self, codigo: int, mascota, descripcion):
        for diagnostico in self.__listaDiagnosticos:
            if diagnostico.codigo == codigo:
                diagnostico.mascota = mascota
                diagnostico.descripcion = descripcion