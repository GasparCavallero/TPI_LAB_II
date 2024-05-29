from Models.Propietario import Propietario
from Vistas.Vista_Propietario import Vista_Propietario


class Controlador_Propietario:
    def __init__(self):
        self._vista = Vista_Propietario()
        self._modelo = Propietario()
        self.listaPropietarios = []

    def cargarPropietario(self):
        with open("Archivos\\propietario.txt", "r") as file:
            linea = file.readlines()
        for l in linea:
            nombre, apellido, fecha_nac, correo = l.strip().split(",")
            self.listaPropietarios.append(
                Propietario(nombre, apellido, fecha_nac, correo)
            )
        return self.listaPropietarios

    def buscarPropietario(self, propietario):
        for i in self.listaPropietarios:
            if i.nombre == propietario:
                return i

    def Mostrar_Datos(self):
        self._vista.Visualizar_Datos(self._modelo.getDatos_Propietario())
