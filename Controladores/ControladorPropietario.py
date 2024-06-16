from Models.Propietario import Propietario

class Controlador_Propietario:
    def __init__(self):
        self.__modelo = Propietario
        self.__listaPropietarios = self.cargar_lista_propietarios()

    def cargar_lista_propietarios(self):
        lista = []
        with open("Archivos/propietario.txt", "r") as txt:
            for linea in txt:
                codigo, estado, nombre, apellido, fechaNac, correo, listaMascotas = linea.strip().split(";")
                lista.append(self.__modelo(codigo, estado, nombre, apellido, fechaNac, correo, listaMascotas))
        return lista

    def buscarPropietario(self, propietario):
        for i in self.listaPropietarios:
            if i.nombre == propietario:
                return i

    def get_lista_propietarios(self):
        return self.__listaPropietarios
