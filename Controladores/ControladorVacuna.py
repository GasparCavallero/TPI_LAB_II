
from Models.Vacuna import Vacuna
from Vistas.Vista_Vacuna import Vista_Vacuna

class Controlador_Vacuna:
    def __init__(self):
        self.vista = Vista_Vacuna()
        self.modelo = Vacuna()
        self.listaVacunas = []

    def cargarVacuna(self):
        with open("Archivos\\vacuna.txt", "r") as file:
            linea = file.readlines()
        for l in linea:
            nombre = l.strip().split(",")
            self.listaVacunas.append(Vacuna(nombre))
        return self.listaVacunas

    def buscarVacuna(self, vacuna):
        for i in self.listaVacunas:
            if i.nombre == vacuna:
                return i