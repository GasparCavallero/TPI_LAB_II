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
            if i.codigo == propietario:
                return i

    def agregarPropietario(self):
        nombre = self._vista.getNombre()
        apellido = self._vista.getApellido()
        fecha_nac = self._vista.getFecha_nac()
        correo = self._vista.getCorreo()
        self.listaPropietarios.append(Propietario(nombre, apellido, fecha_nac, correo))

    def anularPropietario(self, propietario):
        for i in self.listaPropietarios:
            if i.codigo == propietario:
                i.estado = False

    def verPropietario(self, propietario):
        for i in self.listaPropietarios:
            if i.codigo == propietario:
                self._vista.mostrarPropietario()

    def mostrarTodosLosPropietarios(self):
        for i in self.listaPropietarios:
            self._vista.mostrarPropietario(i)

    def mostrarPropietariosHabilitados(self):
        for i in self.listaPropietarios:
            if i.estado == True:
                self._vista.mostrarPropietario(i)
