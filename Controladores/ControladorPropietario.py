from Models.Propietario import Propietario
from utilidades import *
from Vistas.VistaPropietario import VistaPropietario

class ControladorPropietario:
    def __init__(self):
        self.__modelo = Propietario
        self.__vista = VistaPropietario()
        self.__listaPropietarios = []
        self.cargar_lista_propietarios()

    def cargar_lista_propietarios(self) -> None:
        with open("Archivos/propietario.txt", "r") as txt:
            for linea in txt:
                codigo, estado, nombre, apellido, fechaNac, correo, listaMascotas = linea.strip().split(";")
                self.__listaPropietarios.append(self.__modelo(int(codigo), bool(estado), nombre, apellido, fechaNac, correo, listaMascotas))

    def agregar_mascota(self, codigo: int, mascota: str):
        for propietario in self.__listaPropietarios:
            if propietario.codigo == codigo:
                propietario.agregar_mascota(mascota)

    def buscar_propietario(self, codigo):
        match = False
        for i in self.__listaPropietarios:
            if i.codigo == codigo:
                match = True
                return i
        if match == False:
            return False

    def crear_nuevo_propietario(self):
        nombre, apellido, fechaNac, correo = self.__vista.crearPropietario()
        propietario = self.__modelo(crearCodigo(self.__listaPropietarios), True, nombre, apellido, fechaNac, correo, "0") # Creación de nuevo propetario, usar crearCodigo, estado = True, pasarle la lista de Mascotas vacía y luego appendearla cuando se haya creado mascota
        self.__listaPropietarios.append(propietario)
        self.__vista.mostrarCreacionExitosa()

    def modificar_propietario(self):
        match = False
        codigo:int = self.__vista.pedirCodigo("Ingrese el código del propietario a modificar: ")
        for propietario in self.__listaPropietarios:
            if propietario.codigo == codigo:
                match = True
                nombre, apellido, fechaNac, correo = self.__vista.modificarPropietario(propietario.nombre, propietario.apellido)
                propietario.nombre = nombre
                propietario.apellido = apellido
                propietario.fechaNac = fechaNac
                propietario.correo = correo
                self.__vista.mostrarCambioExitoso()
        if match == False:
            self.__vista.codigoInvalido()

    def anular_propietario(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código del propietario a anular: ")
        for propietario in self.__listaPropietarios:
            if propietario.codigo == codigo:
                match = True
                propietario.anular()
                self.__vista.mostrarObjetoAnuladoExitosamente("Propietario/a")
        if match == False:
            self.__vista.codigoInvalido()

    def guardar_propietarios(self):
        with open("Archivos/propietario.txt", "w") as txt:
            for linea in self.__listaPropietarios:
                txt.write(f"{linea.codigo};{linea.estado};{linea.nombre};{linea.apellido};{linea.fechaNac};{linea.correo};{linea.listaMascotas}\n")

    def get_lista_propietarios(self):
        return self.__listaPropietarios

    def menu(self):
        opcion = self.__vista.menu()
        while opcion != 5:
            match opcion:
                case 1:
                    self.__vista.mostrarLista(self.get_lista_propietarios())
                    self.__vista.mostrarEnterParaVolver()
                case 2:
                    self.crear_nuevo_propietario()
                    self.__vista.mostrarEnterParaVolver()
                case 3:
                    self.modificar_propietario()
                    self.__vista.mostrarEnterParaVolver()
                case 4:
                    self.anular_propietario()
                    self.__vista.mostrarEnterParaVolver()
                case 5:
                    break
            break