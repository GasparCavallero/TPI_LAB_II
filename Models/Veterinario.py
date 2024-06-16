from .Persona import Persona

class Veterinario(Persona):
    def __init__(self, codigo: int, estado: bool, nombre, apellido, fechaNac, correo, especialidad):
        super().__init__(estado, nombre, apellido, fechaNac, correo)
        self.__especialidad = especialidad
        self.__codigo = codigo

    def __str__(self):
        return f"""Codigo: {self.__codigo}
Estado: {super().estado}
Nombre: {super().nombre}
Apellido: {super().apellido}
Fecha de nacimiento: {super().fechaNac}
Correo: {super().correo}
Especialidad: {self.__especialidad}
"""

    @property
    def especialidad(self):
        return self.especialidad

    @especialidad.setter
    def especialidad(self, especialidad):
        self.__especialidad = especialidad

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo
    