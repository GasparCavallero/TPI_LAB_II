from Models.Veterinario import Veterinario
from utilidades import *

class ControladorVeterinario:
    def __init__(self):
        self.__modelo = Veterinario
        self.__listaVeterinarios = []
        self.cargar_lista_veterinarios()

    def cargar_lista_veterinarios(self):
        with open("Archivos/veterinario.txt", "r") as txt:
            for linea in txt:
                codigo, estado, nombre, apellido, fechaNac, correo, especialidad = linea.strip().split(";")
                self.__listaVeterinarios.append(self.__modelo(int(codigo), bool(estado), nombre, apellido, fechaNac, correo, especialidad))

    def buscarPropietario(self, propietario):
        for i in self.listaPropietarios:
            if i.nombre == propietario:
                return i

    def crear_nuevo_veterinario(self):
        nombre = input("Nombre: ") # Reemplazar por vistas
        apellido = input("Apellido: ") # Reemplazar por vistas
        fechaNac = input("Fecha de nacimiento (formato DD/MM/AAAA): ") # Reemplazar por vistas
        correo = input("Ingrese su correo: ") # Reemplazar por vistas
        especialidad = input("Ingrese la especialidad: ")
        propietario = self.__modelo(crearCodigo(self.__listaVeterinarios), True, nombre, apellido, fechaNac, correo, especialidad) # Creación de nuevo propetario, usar crearCodigo, estado = True, pasarle la lista de Mascotas vacía y luego appendearla cuando se haya creado mascota
        self.__listaVeterinarios.append(propietario)

    def modificar_veterinario(self):
        codigo:int = int(input("Ingrese el código del veterinario a modificar: "))
        for veterinario in self.__listaVeterinarios:
            if veterinario.codigo == codigo:
                veterinario.nombre = input("Ingrese el nuevo nombre: ") # Reemplazar por vistas
                veterinario.apellido = input("Ingrese el nuevo apellido: ")
                veterinario.fechaNac = input("Ingrese la nueva fecha de nacimiento: ")
                veterinario.correo = input("Ingrese el nuevo correo: ")
                veterinario.especialidad = input("Ingrese la nueva especialidad: ") # Reemplazar por vistas
            else:
                return # Vista de error/no encontrado algo así

    def get_lista_veterinarios(self):
        return self.__listaVeterinarios

    def baja_veterinario(self):
        codigo:int = int(input("Codigo del veterinario a anular: ")) # Reempalzar por vista
        for veterinario in self.__listaVeterinarios:
            if veterinario.codigo == codigo:
                veterinario.baja()
            else:
                return # Vista error