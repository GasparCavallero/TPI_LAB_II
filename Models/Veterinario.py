from Persona import Persona

class Veterinario(Persona):
    def __init__(self, matricula, nombre, apellido, fechaNac, correo, codigo):
        super().__init__(nombre, apellido, fechaNac, correo)
        self.__matricula = matricula
        self.__codigo =int(codigo)

    def __str__(self):
        return f"""Nombre: {super().nombre}
Apellido: {super().apellido}
Fecha de nacimiento: {super().fechaNac}
Correo: {super().correo}
Especialidad: {self.__matricula}
Codigo: {self.__codigo}"""

    @property
    def matricula(self):
        return self.matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo
    