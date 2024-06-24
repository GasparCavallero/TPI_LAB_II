from .Persona import Persona

class Propietario(Persona):
    def __init__(self, codigo: int, estado: bool, nombre, apellido, fechaNac, correo, listaMascotas):
        super().__init__(estado, nombre, apellido, fechaNac, correo)
        self.__listaMascotas = listaMascotas
        self.__codigo = codigo

    def __str__(self):
        return f"""Codigo: {self.__codigo}
Estado: {super().estado}
Nombre: {super().nombre}
Apellido: {super().apellido}
Fecha de nacimiento: {super().fechaNac}
Correo: {super().correo}
Mascotas: {self.__listaMascotas}
"""

    def agregar_mascota(self, Mascota):
        lista = self.__listaMascotas + f",{Mascota}"
        self.__listaMascotas = lista

    @property
    def codigo(self):
        return self.__codigo

    @property
    def listaMascotas(self):
        return self.__listaMascotas

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo

    