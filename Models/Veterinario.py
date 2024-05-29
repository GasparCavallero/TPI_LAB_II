from Persona import Persona

class Veterinario(Persona):
    def __init__(self, especialidad, nombre, apellido, fechaNac, correo, codigo):
        super().__init__(nombre, apellido, fechaNac, correo)
        self.__especialidad = especialidad
        self.__codigo =int(codigo)

    def __str__(self):
        return f"""Nombre: {super().nombre}
Apellido: {super().apellido}
Fecha de nacimiento: {super().fechaNac}
Correo: {super().correo}
Especialidad: {self.__especialidad}
Codigo: {self.__codigo}"""

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
    