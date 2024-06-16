from Models.Veterinario import Veterinario

class ControladorVeterinario:
    def __init__(self):
        self.__modelo = Veterinario
        self.__listaVeterinarios = self.cargar_lista_veterinarios()

    def cargar_lista_veterinarios(self):
        lista = []
        with open("Archivos/veterinario.txt", "r") as txt:
            for linea in txt:
                codigo, estado, nombre, apellido, fechaNac, correo, especialidad = linea.strip().split(";")
                lista.append(self.__modelo(codigo, estado, nombre, apellido, fechaNac, correo, especialidad))
        return lista

    def buscarPropietario(self, propietario):
        for i in self.listaPropietarios:
            if i.nombre == propietario:
                return i

    def get_lista_veterinarios(self):
        return self.__listaVeterinarios
