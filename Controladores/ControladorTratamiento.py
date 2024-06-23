from Models.Tratamiento import Tratamiento
from utilidades import *


class ControladorTratamiento:
    def __init__(self):
        self.__modelo = Tratamiento
        self.__listaTratamientos = self.cargar_lista_tratamientos()

    def cargar_lista_tratamientos(self):
        lista = []
        with open("Archivos/tratamiento.txt", "r") as txt:
            for linea in txt:
                codigo, mascota, fecha, descripcion = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), mascota, fecha, descripcion))
        return lista
    
    def crear_nuevo_tratamiento(self, descripcion, mascota):
        tratamiento = self.__modelo(crearCodigo(self.__listaTratamientos), mascota, fechaActual(), descripcion)
        self.__listaTratamientos.append(tratamiento)
        # quizá haya que appendear a la lista de ficha medica, o quiza directamente quitar la lista de ficha medica y usar este controlador

    def get_tratamientos_via_codigo(self, codigo):
        # get todos los tratamientos que matcheen el código, para construir ficha médica
        ...

    def eliminar_tratamiento(self, codigo: int):
        for tratamiento in self.__listaTratamientos:
            if tratamiento.codigo == codigo:
                self.__listaTratamientos.remove(tratamiento)

    def modificar_tratamiento(self, codigo: int, descripcion, mascota):
        for tratamiento in self.__listaTratamientos:
            if tratamiento.codigo == codigo:
                tratamiento.descripcion = descripcion
                tratamiento.mascota = mascota

    def get_lista_tratamientos(self):
        return self.__listaTratamientos