from Models.Consulta import Consulta

class ControladorConsulta:
    def __init__(self):
        self.__modelo = Consulta
        self.__listaConsultas = self.cargar_lista_consultas()

    def cargar_lista_consultas(self):
        lista = []
        with open("Archivos/consulta.txt", "r") as txt:
            for linea in txt:
                codigo, estado, Veterinario, Diagnostico, descripcion, fecha = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), bool(estado), Veterinario, Diagnostico, descripcion, fecha))
        return lista

    def get_lista_consultas(self):
        return self.__listaConsultas
