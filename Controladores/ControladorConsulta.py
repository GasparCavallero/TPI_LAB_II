from Models.Consulta import Consulta
from utilidades import *

class ControladorConsulta:
    def __init__(self):
        self.__modelo = Consulta
        self.__listaConsultas = self.cargar_lista_consultas()

    def cargar_lista_consultas(self):
        lista = []
        with open("Archivos/consulta.txt", "r") as txt:
            for linea in txt:
                codigo, estado, Veterinario, descripcion, fecha = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), bool(estado), Veterinario, descripcion, fecha))
        return lista

    def crear_nueva_consulta(self, veterinario, descripcion):
        consulta = self.__modelo(crearCodigo(self.__listaConsultas), True,  veterinario, descripcion, fechaActual())
        self.__listaConsultas.append(consulta)

    def eliminar_consulta(self, codigo: int):
        for consulta in self.__listaConsultas:
            if consulta.codigo == codigo:
                self.__listaConsultas.remove(consulta)

    def modificar_consulta(self, codigo: int, veterinario, descripcion):
        for consulta in self.__listaConsultas:
            if consulta.codigo == codigo:
                consulta.veterinario = veterinario
                consulta.descripcion = descripcion

    def guardar_consultas(self):
        with open("Archivos/consulta.txt", "w") as txt:
            for linea in self.__listaConsultas:
                txt.write(f"{linea.codigo};{linea.estado};{linea.veterinario};{linea.descripcion};{linea.fecha}\n")

    def get_lista_consultas(self):
        return self.__listaConsultas
