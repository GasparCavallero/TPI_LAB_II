from Models.Tratamiento import Tratamiento

class ControladorTratamiento:
    def __init__(self):
        self.__modelo = Tratamiento
        self.__listaTratamientos = self.cargar_lista_tratamientos()

    def cargar_lista_tratamientos(self):
        lista = []
        with open("Archivos/tratamiento.txt", "r") as txt:
            for linea in txt:
                codigo, fecha, descripcion = linea.strip().split(";")
                lista.append(self.__modelo(int(codigo), fecha, descripcion))
        return lista
    
    def get_lista_tratamientos(self):
        return self.__listaTratamientos