from Persona import Persona

class Veterinario(Persona):
    def __init__(self, especialidad, nombre, apellido, fechaNac, correo):
        super().__init__(nombre, apellido, fechaNac, correo)
        self.__especialidad = especialidad

    def __str__(self):
        return f"""Nombre: {super().nombre}
Apellido: {super().apellido}
Fecha de nacimiento: {super().fechaNac}
Correo: {super().correo}
Especialidad: {self.__especialidad}"""

    @property
    def especialidad(self):
        return self.especialidad

    @especialidad.setter
    def especialidad(self, especialidad):
        self.__especialidad = especialidad
    