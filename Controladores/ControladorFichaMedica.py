from Models.FichaMedica import FichaMedica
from Vistas.Vista_FichaMedica import Vista_FichaMedica
from Models.Mascota import Mascota


class Controlador_FichaMedica:
    def __init__(self):
        self._vista = Vista_FichaMedica()
        self._modelo = FichaMedica()
        self.listaFichaMedica = []

    def cargarFichaMedica(self):
        with open("Archivos\\diagnostico.txt", "r") as file:
            linea = file.readlines()
        for l in linea:
            mascota = self.buscarMascota()
            mascota = l.strip().split(",")
            self.listaDiagnostico.append(FichaMedica(mascota,))
        return self.listaFichaMedica
    