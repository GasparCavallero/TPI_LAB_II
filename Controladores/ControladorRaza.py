from Models.Raza import Raza
from utilidades import *
from Vistas.VistaRaza import VistaRaza

class ControladorRaza:
    def __init__(self):
        self.__modelo = Raza
        self.__listaRazas = []
        self.cargar_lista_razas()

    def cargar_lista_razas(self):
        with open("Archivos/raza.txt", "r") as txt:
            for linea in txt:
                codigo, estado, tipoAnimal, nombre = linea.strip().split(";")
                self.__listaRazas.append(self.__modelo(int(codigo), bool(estado), tipoAnimal, nombre))

    def get_lista_razas(self): # Returnea lista de razas 
        return self.__listaRazas

    def crear_nueva_raza(self, nombre, tipoAnimal):
        objeto = Raza(crearCodigo(self.__listaRazas), True, tipoAnimal, nombre)
        self.__listaRazas.append(objeto)
        
    def modificar_raza(self, codigo):
        for raza in self.__listaRazas:
            if raza.codigo == codigo:
                tipoAnimal = input("Tipo de animal: ") # Reemplazar por llamada a vista
                nombre = input("Nombre: ") # Reemplazar por llamada a vista
                raza.nombre = nombre
                raza.tipoAnimal = tipoAnimal

    def anular_raza(self, codigo):
        for raza in self.__listaRazas:
            if raza.codigo == codigo:
                raza.anular()

    def guardar_razas(self):
        with open("Archivos/raza.txt", "w") as txt:
            for linea in self.__listaRazas:
                txt.write(f"{linea.codigo};{linea.estado};{linea.nombre};{linea.tipoAnimal}\n")

    def buscar_raza(self, codigo): # Busca raza vía código en lista de razas
        for raza in self.__listaRazas:
            if raza.codigo == codigo:
                return raza

    def menu(self):
        opcion = VistaRaza.menu()
        while opcion != 9:
            match opcion:
                case 1:
                    print("...")
                    opcion = VistaRaza.menu()
                case 9:
                    print("0")
            break