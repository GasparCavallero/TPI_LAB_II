from Models.Veterinario import Veterinario
from Vistas.Vista_Veterinario import Vista_Veterinario


class Controlador_Veterinario:
    def __init__(self):
        self._vista = Vista_Veterinario()
        self._modelo = Veterinario()
        self.listaVeterinario = []

    def cargar_veterinario(self):
        with open("\\Archivos\\veterinario.txt", "r") as file:
            lineas = file.readlines()
        for i in lineas:
            especialidad, nombre, apellido, fechaNac, correo = i.strip().split(",")
            self.listaVeterinario.append(
                Veterinario(especialidad, nombre, apellido, fechaNac, correo)
            )
