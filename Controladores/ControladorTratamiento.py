from Models.Tratamiento import Tratamiento
from Vistas.VistaTratamiento import VistaTratamiento
from utilidades import *


class ControladorTratamiento:
    def __init__(self, controladorMascota):
        self.__modelo = Tratamiento
        self.__vista = VistaTratamiento()
        self.__listaTratamientos = self.cargar_lista_tratamientos()
        self.__cm = controladorMascota

    def cargar_lista_tratamientos(self):
        lista = []
        with open("Archivos/tratamiento.txt", "r") as txt:
            for linea in txt:
                codigo, mascota, fecha, descripcion = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), mascota, fecha, descripcion))
        return lista
    
    def crear_nuevo_tratamiento(self):
        mascota = self.__vista.pedirCodigo("Ingrese el código de la mascota a la que se le asignará el tratamiento: ")
        if self.__cm.buscar_mascota(mascota):
            descripcion = self.__vista.inputStringNoVacia("Ingrese la descripción del tratamiento: ")
            tratamiento = self.__modelo(crearCodigo(self.__listaTratamientos), mascota, fechaActual(), descripcion)
            self.__listaTratamientos.append(tratamiento)
            self.__vista.mostrarCreacionExitosa()
        else:
            self.__vista.codigoInvalido()

    def get_tratamientos_via_codigo(self, codigo):
        # get todos los tratamientos que matcheen el código, para construir ficha médica
        ...

    def eliminar_tratamiento(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código del tratamiento a eliminar: ")
        for tratamiento in self.__listaTratamientos:
            if tratamiento.codigo == codigo:
                match = True
                self.__listaTratamientos.remove(tratamiento)
                self.__vista.mostrarEliminadoExitosamente("Tratamiento")
        if match == False:
            self.__vista.codigoInvalido()

    def guardar_tratamientos(self):
        with open("Archivos/tratamiento.txt", "w") as txt:
            for linea in self.__listaTratamientos:
                txt.write(f"{linea.codigo};{linea.mascota};{linea.fecha};{linea.descripcion}\n")

    def modificar_tratamiento(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código del tratamiento a modificar: ")
        for tratamiento in self.__listaTratamientos:
            if tratamiento.codigo == codigo:
                match = True
                mascota, descripcion = self.__vista.modificar_tratamiento(tratamiento)
                tratamiento.descripcion = descripcion
                tratamiento.mascota = mascota
                self.__vista.mostrarCambioExitoso()
        if match == False:
            self.__vista.codigoInvalido()

    def menu(self):
        opcion = self.__vista.menu()
        while opcion != 5:
            match opcion:
                case 1:
                    self.__vista.mostrarLista(self.get_lista_tratamientos())
                    self.__vista.mostrarEnterParaVolver()
                case 2:
                    self.modificar_tratamiento()
                    self.__vista.mostrarEnterParaVolver()
                case 3:
                    self.crear_nuevo_tratamiento()
                    self.__vista.mostrarEnterParaVolver()
                case 4:
                    self.eliminar_tratamiento()
                    self.__vista.mostrarEnterParaVolver()
                case 5:
                    break
            break

    def get_lista_tratamientos(self):
        return self.__listaTratamientos