from Models.Diagnostico import Diagnostico

class ControladorDiagnostico:
    def __init__(self):
        self.__modelo = Diagnostico
        self.__listaDiagnosticos = self.cargar_lista_diagnosticos()

    def cargar_lista_diagnosticos(self):
        lista = []
        with open("Archivos/diagnostico.txt", "r") as txt:
            for linea in txt:
                codigo, fecha, descripcion, Tratamiento = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), fecha, descripcion, Tratamiento))
        return lista

    def get_lista_diagnosticos(self):
        return self.__listaDiagnosticos