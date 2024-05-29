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
            nombre = l.strip().split(",")
            self.listaRazas.append(Raza(nombre))
        return self.listaRazas

    def buscarRaza(self, raza):
        for i in self.listaRazas:
            if i.nombre == raza:
                return i

    def mostrar_Datos(self):
        self._vista.Visualizar_Datos(self._modelo.getDatos_Raza())
