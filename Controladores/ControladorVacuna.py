from Models.Vacuna import Vacuna

class Controlador_Vacuna:
    def __init__(self):
        self.__modelo = Vacuna
        self.__listaVacunas = self.cargar_lista_vacunas()

    def cargar_lista_vacunas(self):
        lista = []
        with open("Archivos/vacuna.txt", "r") as txt:
            for linea in txt:
                codigo, estado, nombre, = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), bool(estado), nombre))
        return lista

    def get_lista_vacunas(self): # Returnea lista de vacunas
        return self.__listaVacunas

    def buscar_vacuna(self, vacuna): # Busca vacuna vía código en lista de vacunas
        for vacuna in self.__listaVacunas:
            if vacuna.nombre == vacuna:
                return vacuna
