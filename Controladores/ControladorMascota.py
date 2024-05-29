from Models.Mascota import Mascota
from Vistas.Vista_Mascota import Vista_Mascota


class Controlador_Mascota:
    def __init__(self):
        self._vista = Vista_Mascota()
        self._modelo = Mascota()
        self.listaMascotas = []

    def cargarMascota(self):
        with open("Archivos\\mascota.txt", "r") as file:
            linea = file.readlines()
        for l in linea:
            Propietario, Raza, FichaMedica, nombre, fechaNac, tipoAnima = (
                l.strip().split(",")
            )
            self.listaMascotas.append(
                Mascota(Propietario, Raza, FichaMedica, nombre, fechaNac, tipoAnima)
            )
        return self.listaMascotas

    def buscarMascota(self, mascota):
        for i in self.listaMascotas:
            if i.nombre == mascota:
                return i
