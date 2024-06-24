from Models.Diagnostico import Diagnostico
from Vistas.VistaDiagnostico import VistaDiagnostico
from utilidades import *

class ControladorDiagnostico:
    def __init__(self):
        self.__modelo = Diagnostico
        self.__vista = VistaDiagnostico()
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

    def crear_nuevo_diagnostico(self):
        mascota = self.__vista.pedirCodigo("Ingrese el código de la mascota a la que se le creará un nuevo diagnóstico: ")
        # if controlador.mascota.buscar_mascota
        # entonces mascota = mascota
        # else self._vista.error y break?
        descripcion = self.__vista.inputStringNoVacia("Ingrese la descripción del diagnóstico: ")
        diagnostico = self.__modelo(crearCodigo(self.__listaDiagnosticos), mascota, fechaActual(), descripcion)
        self.__listaDiagnosticos.append(diagnostico)

    def get_diagnosticos_via_codigo(self, codigo):
        # get todos los tratamientos que matcheen el código, para construir ficha médica
        ...

    def guardar_diagnosticos(self):
        with open("Archivos/diagnostico.txt", "w") as txt:
            for linea in self.__listaDiagnosticos:
                txt.write(f"{linea.codigo};{linea.mascota};{linea.fecha};{linea.descripcion}\n")

    def eliminar_diagnostico(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código del diagnóstico a eliminar: ")
        for diagnostico in self.__listaDiagnosticos:
            if diagnostico.codigo == codigo:
                match = True
                self.__listaDiagnosticos.remove(diagnostico)
                self.__vista.mostrarEliminadoExitosamente("Diagnóstico")
        if match == False:
            self.__vista.codigoInvalido()

    def modificar_diagnostico(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código del diagnóstico a modificar: ")
        for diagnostico in self.__listaDiagnosticos:
            if diagnostico.codigo == codigo:
                match = True
                descripcion = self.__vista.modificarDiagnostico(diagnostico)
                diagnostico.descripcion = descripcion
                self.__vista.mostrarCambioExitoso()
        if match == False:
            self.__vista.codigoInvalido()

    def menu(self):
        opcion = self.__vista.menu()
        while opcion != 5:
            match opcion:
                case 1:
                    self.__vista.mostrarLista(self.get_lista_diagnosticos())
                    self.__vista.mostrarEnterParaVolver()
                case 2:
                    self.modificar_diagnostico()
                    self.__vista.mostrarEnterParaVolver()
                case 3:
                    self.crear_nuevo_diagnostico()
                    self.__vista.mostrarEnterParaVolver()
                case 4:
                    self.eliminar_diagnostico()
                    self.__vista.mostrarEnterParaVolver()
                case 5:
                    break
            break