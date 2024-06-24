from Models.Vacuna import Vacuna
from Vistas.VistaVacuna import VistaVacuna
from utilidades import *

class ControladorVacuna:
    def __init__(self):
        self.__modelo = Vacuna
        self.__vista = VistaVacuna()
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

    def guardar_vacunas(self):
        with open("Archivos/vacuna.txt", "w") as txt:
            for linea in self.__listaVacunas:
                txt.write(f"{linea.codigo};{linea.estado};{linea.nombre}\n")

    def crear_nueva_vacuna(self):
        vacuna = self.__modelo(crearCodigo(self.__listaVacunas), True, self.__vista.inputStringNoVacia("Ingrese el nombre de la vacuna: "))
        self.__vista.mostrarCreacionExitosa()
        self.__listaVacunas.append(vacuna)

    def modificar_vacuna(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código de la vacuna a modificar: ")
        for vacuna in self.__listaVacunas:
            if vacuna.codigo == codigo:
                match = True
                nombre = self.__vista.modificarVacuna(vacuna)
                vacuna.nombre = nombre
                self.__vista.mostrarCambioExitoso()
        if match == False:
            self.__vista.codigoInvalido()

    def buscar_vacuna(self, codigo): # Busca vacuna vía código en lista de vacunas
        match = False
        for vacuna in self.__listaVacunas:
            if vacuna.codigo == codigo:
                return vacuna
        if match == False:
            return False

    def alta_vacuna(self, codigo: int):
        for vacuna in self.__listaVacunas:
            if vacuna.codigo == codigo:
                vacuna.dar_alta()
    
    def anular_vacuna(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código de la vacuna a anular: ")
        for vacuna in self.__listaVacunas:
            if vacuna.codigo == codigo:
                match = True
                vacuna.anular()
                self.__vista.mostrarObjetoAnuladoExitosamente(f"Vacuna {vacuna.nombre}")
        if match == False:
            self.__vista.codigoInvalido()


    def menu(self):
        opcion = self.__vista.menu()
        while opcion != 5:
            match opcion:
                case 1:
                    self.__vista.mostrarLista(self.get_lista_vacunas())
                    self.__vista.mostrarEnterParaVolver()
                case 2:
                    self.modificar_vacuna()
                    self.__vista.mostrarEnterParaVolver()
                case 3:
                    self.crear_nueva_vacuna()
                    self.__vista.mostrarEnterParaVolver()
                case 4:
                    self.anular_vacuna()
                    self.__vista.mostrarEnterParaVolver()
                case 5:
                    break
            break
