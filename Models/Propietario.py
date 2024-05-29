from Persona import Persona

class Propietario(Persona):
    def __init__(self, nombre, apellido, fecha_nac, correo, codigo):
        self.__mascotas = []
        self.__codigo= int(codigo)
        super().__init__(nombre, apellido, fecha_nac, correo)

    def __str__(self):
        return f"""Nombre: {super().nombre}
Apellido: {super().apellido}
Fecha de nacimiento: {super().fechaNac}
Correo: {super().correo}
Mascotas: {self.__mascotas}
Codigo: {self.__codigo}"""
    
    def agregar_mascota(self, Mascota):
        self.__mascotas.append(Mascota)

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo

    