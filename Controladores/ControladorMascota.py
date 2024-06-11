from Models.Mascota import Mascota
from Vistas.VistaMascota import VistaMascota


class Controlador_Mascota:
    def __init__(self):
        self._vista = VistaMascota()
        self._modelo = Mascota()
        self.listaMascotas = []

    def cargarMascota(self):
        with open("Archivos\\mascota.txt", "r") as file:
            linea = file.readlines()
        for l in linea:
            Propietario, Raza, FichaMedica, nombre, fechaNac, tipoAnimal = (
                l.strip().split(",")
            )
            self.listaMascotas.append(
                Mascota(Propietario, Raza, FichaMedica, nombre, fechaNac, tipoAnimal)
            )
        return self.listaMascotas

    def buscarMascota(self, mascota):
        for i in self.listaMascotas:
            if i.nombre == mascota:
                return i

    def agregarMascota(self):
        Propietario = self.vista.ingresarPropietario()
        Raza = self.vista.ingresarRaza()
        FichaMedica = self.vista.ingresarFichaMedica()
        nombre = self.vista.ingresarnombre()
        fechaNac = self.vista.ingresarfechaNac()
        tipoAnimal = self.vista.ingresartipoAnimal()
        self.listaMascotas.append(
            Mascota(Propietario, Raza, FichaMedica, nombre, fechaNac, tipoAnimal)
        )
        with open("Archivos\\mascotas.txt", "a") as f:
            f.write(
                f"\n{Propietario},{Raza},{FichaMedica},{nombre},{fechaNac},{tipoAnimal}"
            )

    def anularMascota(self, mascota):
        for i in self.listaMascotas:
            if i.nombre == mascota:
                i.estado = False

    def verMascota(self, mascota):
        for i in self.listaMascotas:
            if i.nombre == mascota:
                self.vista.mostrarMascota(i)
