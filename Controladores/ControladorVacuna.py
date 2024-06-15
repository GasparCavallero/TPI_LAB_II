from Models.Vacuna import Vacuna
from Vistas.Vista_Vacuna import Vista_Vacuna


class Controlador_Vacuna:
    def __init__(self):
        self._vista = Vista_Vacuna()
        self._modelo = Vacuna()
        self.listaVacunas = []

    def cargarVacuna(self):
        with open("Archivos\\vacuna.txt", "r") as file:
            linea = file.readlines()
        for l in linea:
            nombre, codigo = l.strip().split(",")
            self.listaVacunas.append(Vacuna(nombre, codigo))
        return self.listaVacunas

    def buscarVacuna(self, vacuna):
        for i in self.listaVacunas:
            if i.codigo == vacuna:
                return i

    def agregarVacuna(self):
        nombre = self._vista.getNombre()
        codigo = self._vista.getCodigo()
        self.listaVacunas.append(Vacuna(nombre, codigo))

    def anularVacuna(self, vacuna):
        for i in self.listaVacunas:
            if i.codigo == vacuna:
                i.estado = False

    def verVacuna(self, vacuna):
        for i in self.listaVacunas:
            if i.codigo == vacuna:
                self._vista.mostrarVacuna(i)

    def mostrarTodasLasVacunas(self):
        for i in self.listaVacunas:
            self._vista.mostrarVacuna(i)

    def mostrarVacunasHabilitadas(self):
        for i in self.listaVacunas:
            if i.estado == True:
                self._vista.mostrarVacuna(i)
