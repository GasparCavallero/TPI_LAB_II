from Models.Veterinario import Veterinario
from Vistas.Vista_Veterinario import Vista_Veterinario


class Controlador_Veterinario:
    def __init__(self):
        self._vista = Vista_Veterinario()
        self._modelo = Veterinario()
        self.listaVeterinario = []

    def cargar_veterinario(self):
        with open("\\Archivos\\veterinario.txt", "r") as file:
            lineas = file.readlines()
        for i in lineas:
            matricula, nombre, apellido, fechaNac, correo, codigo = i.strip().split(",")
            self.listaVeterinario.append(
                Veterinario(matricula, nombre, apellido, fechaNac, correo, codigo)
            )

    def buscarVeterinario(self, veterinario):
        for i in self.listaVeterinario:
            if i.codigo == veterinario:
                return i

    def agregarVeterinario(self):
        matricula = self._vista.getMatricula()
        nombre = self._vista.getNombre()
        apellido = self._vista.getApellido()
        fechaNac = self._vista.getFechaNac()
        correo = self._vista.getCorreo()
        codigo = self._vista.getCodigo()
        self.listaVeterinario.append(
            Veterinario(matricula, nombre, apellido, fechaNac, correo, codigo)
        )

    def anularVeterinario(self, veterinario):
        for i in self.listaVeterinario:
            if i.codigo == veterinario:
                i.codigo = False

    def verVeterinario(self, veterinario):
        for i in self.listaVeterinario:
            if i.codigo == veterinario:
                self._vista.mostrarVeterinario()

    def mostrarTodosLosVeterinarios(self):
        for i in self.listaVeterinario:
            self._vista.mostrarVeterinario(i)

    def mostrarVeterinariosHabilitados(self):
        for i in self.listaVeterinario:
            if i.estado == True:
                self._vista.mostrarVeterinario(i)
