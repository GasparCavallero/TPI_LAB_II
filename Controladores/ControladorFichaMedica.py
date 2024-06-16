from Models.FichaMedica import FichaMedica

class ControladorFichaMedica:
    def __init__(self):
        self.__modelo = FichaMedica
        self.__listaFichasMedicas = self.cargar_fichas_medicas()

    def cargar_fichas_medicas(self):
        lista = []
        with open("Archivos/fichamedica.txt", "r") as txt:
            for linea in txt:
                codigo, estado, mascota, listaConsultas, listaVacunas = linea.strip().split(";")
                lista.append(FichaMedica(int(codigo), bool(estado), mascota, listaConsultas, listaVacunas))
        return lista

    def get_fichas_medicas(self):
        return self.__listaFichasMedicas
