from Models.Consulta import Consulta
from Vistas.VistaConsulta import VistaConsulta
from utilidades import *

class ControladorConsulta:
    def __init__(self, controladorVeterinario):
        self.__cvt = controladorVeterinario
        self.__modelo = Consulta
        self.__vista = VistaConsulta()
        self.__listaConsultas = self.cargar_lista_consultas()

    def cargar_lista_consultas(self):
        lista = []
        with open("Archivos/consulta.txt", "r") as txt:
            for linea in txt:
                codigo, estado, Veterinario, descripcion, fecha = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), bool(estado), Veterinario, descripcion, fecha))
        return lista

    def crear_nueva_consulta(self):
        veterinario = self.__vista.pedirCodigo("Ingrese el código del veterinario que realizó la consulta: ")
        if self.__cvt.buscar_veterinario(veterinario):
            descripcion = self.__vista.inputStringNoVacia("Ingrese la descripción de la consulta: ")
            consulta = self.__modelo(crearCodigo(self.__listaConsultas), True,  veterinario, descripcion, fechaActual())
            self.__listaConsultas.append(consulta)
            self.__vista.mostrarCreacionExitosa()
        else:
            self.__vista.codigoInvalido()

    def eliminar_consulta(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código de la consulta a anular: ")
        for consulta in self.__listaConsultas:
            if consulta.codigo == codigo:
                match = True
                self.__listaConsultas.remove(consulta)
                self.__vista.mostrarEliminadoExitosamente("Consulta")
        if match == False:
            self.__vista.codigoInvalido()

    def modificar_consulta(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código de la consulta a modificar: ")
        for consulta in self.__listaConsultas:
            if consulta.codigo == codigo:
                match = True
                veterinario, descripcion = self.__vista.modificarConsulta(consulta)
                consulta.veterinario = veterinario
                consulta.descripcion = descripcion
                self.__vista.mostrarCambioExitoso()
        if match == False:
            self.__vista.codigoInvalido()

    def guardar_consultas(self):
        with open("Archivos/consulta.txt", "w") as txt:
            for linea in self.__listaConsultas:
                txt.write(f"{linea.codigo};{linea.estado};{linea.veterinario};{linea.descripcion};{linea.fecha}\n")

    def get_lista_consultas(self):
        return self.__listaConsultas

    def menu(self):
        opcion = self.__vista.menu()
        while opcion != 5:
            match opcion:
                case 1:
                    self.__vista.mostrarLista(self.get_lista_consultas())
                    self.__vista.mostrarEnterParaVolver()
                case 2:
                    self.modificar_consulta()
                    self.__vista.mostrarEnterParaVolver()
                case 3:
                    self.crear_nueva_consulta()
                    self.__vista.mostrarEnterParaVolver()
                case 4:
                    self.eliminar_consulta()
                    self.__vista.mostrarEnterParaVolver()
                case 5:
                    break
            break