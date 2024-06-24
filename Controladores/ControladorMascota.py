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
        self.__listaMascotas = self.cargar_lista_mascotas()

    def cargar_lista_mascotas(self):
        lista = []
        with open("Archivos/mascota.txt", "r") as txt:
            for linea in txt:
                codigo, estado, Propietario, Raza, FichaMedica, nombre, fechaNac = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), bool(estado), Propietario, Raza, FichaMedica, nombre, fechaNac))
        return lista
    
    def crear_nueva_mascota(self, propietario):
        if self.__ControladorPropietario.buscar_propietario_via_codigo(int(propietario)):
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

    def modificar_mascota(self, codigo: int):
        for mascota in self.__listaMascotas:
            if mascota.codigo == codigo:
                mascota.nombre = input(f"Nuevo nombre para {mascota.nombre}: ") # Modificar por vista
                mascota.fechaNac = input(f"Nueva fecha de nacimiento: ") # Modificar por vista
            else:
                return # Crear excepción/mensaje de error/no encontrado en sección vista

    def guardar_mascotas(self):
        with open("Archivos/mascota.txt", "w") as txt:
            for linea in self.__listaMascotas:
                txt.write(f"{linea.codigo};{linea.estado};{linea.propietario};{linea.raza};{linea.codigo};{linea.nombre};{linea.fechaNac}\n")


    def anular_mascota(self, codigo: int):
        for mascota in self.__listaMascotas:
            if mascota.codigo == codigo:
                mascota.anular()
                # Vista de mensaje success
            else:
                return # Crear exepción/mensaje de error/no encontrado en sección vista

    """def codigoaobj_propietario(self, codigoBusqueda: int):
        ...

    def codigoaobj_fichamedica(self, codigoBusqueda: int):
        lista = []
        with open("Archivos/fichamedica.txt", "r") as txt:
            for linea in txt:
                codigo, nombre, tipoAnimal = linea.strip().split(";")
                lista.append(Raza(int(codigo), nombre, tipoAnimal))
        return buscarObjetoViaCodigo(codigoBusqueda, lista)

    def codigoaobj_raza(self, codigoBusqueda: int):
        lista = []
        with open("Archivos/raza.txt", "r") as txt:
            for linea in txt:
                codigo, nombre, tipoAnimal = linea.strip().split(";")
                lista.append(Raza(int(codigo), nombre, tipoAnimal))
        return buscarObjetoViaCodigo(codigoBusqueda, lista)"""
    
    def get_lista_mascotas(self):
        return self.__listaMascotas
    
    def menu(self):
        opcion = VistaMascota.menu()