from Models.Veterinario import Veterinario
from utilidades import *
from Vistas.VistaVeterinario import VistaVeterinario

class ControladorVeterinario:
    def __init__(self):
        self.__modelo = Veterinario
        self.__listaVeterinarios = []
        self.__vista = VistaVeterinario()
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
        nombre, apellido, fechaNac, correo, especialidad = self.__vista.crearVeterinario()
        propietario = self.__modelo(crearCodigo(self.__listaVeterinarios), True, nombre, apellido, fechaNac, correo, especialidad) # Creación de nuevo propetario, usar crearCodigo, estado = True, pasarle la lista de Mascotas vacía y luego appendearla cuando se haya creado mascota
        self.__listaVeterinarios.append(propietario)
        self.__vista.mostrarCreacionExitosa()

    def guardar_veterinarios(self):
        with open("Archivos/veterinario.txt", "w") as txt:
            for linea in self.__listaVeterinarios:
                txt.write(f"{linea.codigo};{linea.estado};{linea.nombre};{linea.apellido};{linea.fechaNac};{linea.correo};{linea.especialidad}\n")

    def modificar_veterinario(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código del veterinario a modificar: ")
        for veterinario in self.__listaVeterinarios:
            if veterinario.codigo == codigo:
                match = True
                nombre, apellido, fechaNac, correo, especialidad = self.__vista.modificarVeterinario(veterinario)
                veterinario.nombre = nombre
                veterinario.apellido = apellido
                veterinario.fechaNac = fechaNac
                veterinario.correo = correo
                veterinario.especialidad = especialidad
                self.__vista.mostrarCambioExitoso()
        if match == False:
            self.__vista.codigoInvalido()

    def get_lista_veterinarios(self):
        return self.__listaVeterinarios

    def anular_veterinario(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código del veterinario a anular: ")
        for veterinario in self.__listaVeterinarios:
            if veterinario.codigo == codigo:
                match = True
                veterinario.anular()
                self.__vista.mostrarObjetoAnuladoExitosamente("Veterinario/a")
        if match == False:
            self.__vista.codigoInvalido()
            
    def menu(self):
        opcion = self.__vista.menu()
        while opcion != 5:
            match opcion:
                case 1:
                    self.__vista.mostrarLista(self.get_lista_veterinarios())
                case 2:
                    self.crear_nuevo_veterinario()
                case 3:
                    self.modificar_veterinario()
                case 4:
                    self.anular_veterinario()
                case 5:
                    break
            break