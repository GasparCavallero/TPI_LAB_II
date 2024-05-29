from Models.Diagnostico import Diagnostico
from Vistas.Vista_Diagnostico import Vista_Diagnostico


class Controlador_Diagnostico:
    def __init__(self):
        self.vista = Vista_Diagnostico()
        self.modelo = Diagnostico()
        self.listaDiagnostico = []

    def cargarDiagnostico(self):
        with open("Archivos\\diagnostico.txt", "r") as file:
            linea = file.readlines()
        for l in linea:
            fecha, descripcion, tratamiento = l.strip().split(",")
            self.listaRazas.append(Diagnostico(fecha, descripcion, tratamiento))
        return self.listaRazas

    # def buscarDiagnostico(self, ):
    #     for i in self.listaDiagnostico:
    #         if i. == :
    #             return i
