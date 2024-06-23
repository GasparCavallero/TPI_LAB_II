from Models.Propietario import Propietario
from utilidades import *
from Vistas.VistaPropietario import VistaPropietario

class ControladorPropietario:
    def __init__(self):
        self.__modelo = Propietario
        self.__listaPropietarios = []
        self.cargar_lista_propietarios()

    def cargar_lista_propietarios(self) -> None:
        with open("Archivos/propietario.txt", "r") as txt:
            for linea in txt:
                codigo, estado, nombre, apellido, fechaNac, correo, listaMascotas = linea.strip().split(";")
                self.__listaPropietarios.append(self.__modelo(int(codigo), bool(estado), nombre, apellido, fechaNac, correo, list(listaMascotas)))

    def agregar_mascota(self, codigo, mascota):
        for propietario in self.__listaPropietarios:
            if propietario.codigo == codigo:
                propietario.agregar_mascota(mascota)

    def buscar_propietario_via_codigo(self, codigo):
        for i in self.__listaPropietarios:
            if i.codigo == codigo:
                return i

    def crear_nuevo_propietario(self):
        nombre = input("Nombre: ") # Reemplazar por vistas
        apellido = input("Apellido: ") # Reemplazar por vistas
        fechaNac = input("Fecha de nacimiento (formato DD/MM/AAAA): ") # Reemplazar por vistas
        correo = input("Ingrese su correo: ") # Reemplazar por vistas
        propietario = self.__modelo(crearCodigo(self.__listaPropietarios), True, nombre, apellido, fechaNac, correo, []) # Creación de nuevo propetario, usar crearCodigo, estado = True, pasarle la lista de Mascotas vacía y luego appendearla cuando se haya creado mascota
        self.__listaPropietarios.append(propietario)

    def modificar_propietario(self):
        codigo:int = int(input("Ingrese del propietario a modificar: "))
        for propietario in self.__listaPropietarios:
            if propietario.codigo == codigo:
                propietario.nombre = input("Nuevo nombre: ")
                propietario.apellido = input("Nuevo apellido: ")
                propietario.fechaNac = input("Nueva fecha de nacimiento: ")
                propietario.correo = input("Nuevo correo: ")
            else:
                return # Vista de error

    def baja_propietario(self):
        codigo:int = int(input("Codigo del propietario a anular: ")) # Reempalzar por vista
        for propietario in self.__listaPropietarios:
            if propietario.codigo == codigo:
                propietario.baja()
            else:
                return # Vista error

    def get_lista_propietarios(self):
        return self.__listaPropietarios

    def menu(self):
        opcion = VistaPropietario().menu()