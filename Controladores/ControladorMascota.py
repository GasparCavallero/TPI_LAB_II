from Models.Mascota import Mascota
from Models.Raza import Raza
from Models.Propietario import Propietario
from Models.FichaMedica import FichaMedica
from utilidades import *
from Vistas.VistaMascota import VistaMascota

class ControladorMascota:
    def __init__(self, ControladorPropietario, ControladorFichaMedica):
        self.__ControladorPropietario = ControladorPropietario
        self.__ControladorFichaMedica = ControladorFichaMedica
        self.__modelo = Mascota
        self.__vista = VistaMascota()
        self.__listaMascotas = self.cargar_lista_mascotas()

    def cargar_lista_mascotas(self):
        lista = []
        with open("Archivos/mascota.txt", "r") as txt:
            for linea in txt:
                codigo, estado, Propietario, Raza, FichaMedica, nombre, fechaNac = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), bool(estado), Propietario, Raza, FichaMedica, nombre, fechaNac))
        return lista
    
    def buscar_mascota(self):
        ...

    def crear_nueva_mascota(self):
        # Pedir propietario y si propietario no existe crear uno
        codigo_propietario = self.__vista.pedirCodigo("Ingrese el código del propietario de la mascota: ")
        if self.__ControladorPropietario.buscar_propietario_via_codigo(codigo_propietario):
            propietario = propietario
        else:
            propietario = self.__ControladorPropietario.crear_nuevo_propietario() # Falta crear
        raza = input("Código de raza: ") # Reemplazar por vistas
        nombre = input("Nombre: ") # Reemplazar por vistas
        fechaNac = input("Fecha de nacimiento formato DD/MM/AAAA: ") # Reemplazar por vistas con validación
        codigo = crearCodigo(self.__listaMascotas)
        mascota = Mascota(codigo, True, propietario, raza, codigo, nombre, fechaNac)
        self.__listaMascotas.append(self.__modelo(int(codigo), True, propietario, raza, int(codigo), nombre, fechaNac))
        self.__ControladorFichaMedica.crear_nueva_fichaMedica(mascota.codigo)
        self.__ControladorPropietario.agregar_mascota(mascota.propietario, str(mascota.codigo))

    def modificar_mascota(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código de la mascota a modificar: ")
        for mascota in self.__listaMascotas:
            if mascota.codigo == codigo:
                match = True
                nombre, fechaNac = self.__vista.modificarMascota(mascota)
                mascota.nombre = nombre
                mascota.fechaNac = fechaNac
                self.__vista.mostrarCambioExitoso()
        if match == False:
            self.__vista.codigoInvalido()

    def guardar_mascotas(self):
        with open("Archivos/mascota.txt", "w") as txt:
            for linea in self.__listaMascotas:
                txt.write(f"{linea.codigo};{linea.estado};{linea.propietario};{linea.raza};{linea.codigo};{linea.nombre};{linea.fechaNac}\n")

    def anular_mascota(self):
        match = False
        codigo = self.__vista.pedirCodigo("Ingrese el código de la mascota a anular: ")
        for mascota in self.__listaMascotas:
            if mascota.codigo == codigo:
                match = True
                mascota.anular()
                self.__vista.mostrarObjetoAnuladoExitosamente("Mascota")
        if match == False:
            self.__vista.codigoInvalido()

    def get_lista_mascotas(self):
        return self.__listaMascotas
    
    def menu(self):
        opcion = self.__vista.menu()
        while opcion != 5:
            match opcion:
                case 1:
                    self.__vista.mostrarLista(self.get_lista_mascotas())
                case 2:
                    self.crear_nueva_mascota()
                case 3:
                    self.modificar_mascota()
                case 4:
                    self.anular_mascota()
                case 5:
                    break
            break