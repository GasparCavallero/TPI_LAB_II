from Models.Raza import Raza
from utilidades import *
from Vistas.VistaRaza import VistaRaza

class ControladorRaza:
    def __init__(self):
        self.__modelo = Raza
        self.__vista = VistaRaza()
        self.__listaRazas = []
        self.cargar_lista_razas()

    def cargar_lista_razas(self):
        with open("Archivos/raza.txt", "r") as txt:
            for linea in txt:
                codigo, estado, tipoAnimal, nombre = linea.strip().split(";")
                self.__listaRazas.append(self.__modelo(int(codigo), bool(estado), tipoAnimal, nombre))

    def get_lista_razas(self): # Returnea lista de razas 
        return self.__listaRazas

    def crear_nueva_raza(self):
        tipoAnimal, nombre = self.__vista.crearNuevaRaza()
        objeto = Raza(crearCodigo(self.__listaRazas), True, tipoAnimal, nombre)
        self.__listaRazas.append(objeto)
        self.__vista.mostrarCreacionExitosa()
        
    def modificar_raza(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código de raza a modificar: ")
        for raza in self.__listaRazas:
            if raza.codigo == codigo:
                match = True
                tipoAnimal, nombre = self.__vista.modificarRaza(raza)
                raza.nombre = nombre
                raza.tipoAnimal = tipoAnimal
                self.__vista.mostrarCambioExitoso()
        if match == False:
            self.__vista.codigoInvalido()

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

    def eliminar_raza(self):
        codigo = self.__vista.pedirCodigo("Ingrese el código de raza a eliminar: ")
        match = False
        for raza in self.__listaRazas:
            if raza.codigo == codigo:
                match = True
                self.__listaRazas.remove(raza)
                self.__vista.mostrarObjetoEliminadoExitosamente("Raza")
        if match == False:
            self.__vista.codigoInvalido()


    def menu(self):
        opcion = self.__vista.menu()
        while opcion != 5:
            match opcion:
                case 1:
                    self.__vista.mostrarLista(self.get_lista_razas()) # Mostrar todas las razas
                    self.__vista.mostrarEnterParaVolver()
                case 2:
                    self.modificar_raza()
                    self.__vista.mostrarEnterParaVolver()
                case 3:
                    self.crear_nueva_raza()
                    self.__vista.mostrarEnterParaVolver()
                case 4:
                    self.eliminar_raza()
                    self.__vista.mostrarEnterParaVolver()
                case 5:
                    break
            break