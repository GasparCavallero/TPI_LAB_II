from Models.FichaMedica import FichaMedica
from Vistas.VistaFichaMedica import VistaFichaMedica
from utilidades import *
import os

archivos = os.listdir("Archivos/fichasmedicas")

class ControladorFichaMedica:
    def __init__(self):
        self.__modelo = FichaMedica
        self.__vista = VistaFichaMedica()
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

    def modificar_ficha_medica(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código de la ficha médica a modificar: ")
        for fm in self.__listaFichasMedicas:
            if fm.codigo == codigo:
                match = True
        if match == False:
            self.__vista.codigoInvalido()


    def get_fichas_medicas(self):
        return self.__listaFichasMedicas

    def buscar_ficha_medica(self, codigo: int):
        for fm in self.__listaFichasMedicas:
            if fm.codigo == codigo:
                return fm
    
    def ver_ficha_medica(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código de la ficha médica: ")
        for fm in self.__listaFichasMedicas:
            match = True
            if fm.codigo == codigo:
                self.__vista.mostrarObjeto(fm)
                # Traer también el nombre como nombre, no como código
                # Falta que funcione la funcion buscar_vacunas
        if match == False:
            self.__vista.codigoInvalido()

    def buscar_vacunas(self):
        # Necesita el controlador de vacunas para traer nombre x codigo
        ...

    def agregar_vacuna(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código de la ficha médica: ")
        for fm in self.__listaFichasMedicas:
            match = True
            if fm.codigo == codigo:
                # If controlador_vacuna.buscar_vacuna: fm.agregar_vacuna
                # Else self.vista.error
                pass
        if match == False:
            self.__vista.codigoInvalido()

    def anular_ficha_medica(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código de la ficha médica: ")
        for fm in self.__listaFichasMedicas:
            match = True
            if fm.codigo == codigo:
                fm.anular()
                self.__vista.mostrarObjetoAnuladoExitosamente("Ficha médica")
        if match == False:
            self.__vista.codigoInvalido()

    def menu(self):
        opcion = self.__vista.menu()
        while opcion != 5:
            match opcion:
                case 1:
                    self.__vista.mostrarLista(self.get_fichas_medicas())
                    self.__vista.mostrarEnterParaVolver()
                case 2:
                    self.ver_ficha_medica()
                    self.__vista.mostrarEnterParaVolver()
                case 3:
                    self.agregar_vacuna()
                    self.__vista.mostrarEnterParaVolver()
                case 4:
                    self.anular_ficha_medica()
                    self.__vista.mostrarEnterParaVolver()
                case 5:
                    break
            break

    def guardar_fichasmedicas(self):
        for linea in self.__listaFichasMedicas:
            with open(f"Archivos/fichasmedicas/{str(linea.codigo)}.txt", "w") as txt:
                txt.write(f"{linea.codigo};{linea.estado};{linea.mascota};{linea.listaVacunas}")