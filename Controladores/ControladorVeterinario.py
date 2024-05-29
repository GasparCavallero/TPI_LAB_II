
from Models.Veterinario import Veterinario
from Vistas.Vista_Veterinario import Vista_Veterinario

class Controlador_Veterinario:
    def __init__(self):
        self.vista = Vista_Veterinario()
        self.modelo = Veterinario()

    def cargar_veterinario(self):
        with open("\\Archivos\\socios.txt", "r") as file:
            lineas = file.readlines()
        for i in lineas:
            especialidad, nombre, apellido, fechaNac, correo = i.strip().split(",")
            self._listaSocios.append(Veterinario(especialidad, nombre, apellido, fechaNac, correo))