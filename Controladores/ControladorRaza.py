from Models.Raza import Raza
from Vistas.Vista_Raza import Vista_Raza


class Controlador_Raza:
    def __init__(self):
        self._vista = Vista_Raza()
        self._modelo = Raza()
        self.listaRazas = []

    def cargarRaza(self):
        with open("Archivos\\raza.txt", "r") as file:
            linea = file.readlines()
        for l in linea:
            nombre, tipoAnimal, codigo = l.strip().split(",")
            self.listaRazas.append(Raza(nombre, tipoAnimal, codigo))
        return self.listaRazas

    def buscarRaza(self, raza):
        for i in self.listaRazas:
            if i.codigo == raza:
                return i

    def agregarRaza(self):
        nombre = self._vista.getNombre()
        tipoAnimal = self._vista.getTipoAnimal()
        codigo = self._vista.getCodigo()
        self.listaRazas.append(Raza(nombre, tipoAnimal, codigo))

    def verRaza(self, raza):
        for i in self.listaRazas:
            if i.nombre == raza:
                return i

    def verTodasLasRazas(self):
        for i in self.listaRazas:
            self._vista.mostrarRaza(i)
