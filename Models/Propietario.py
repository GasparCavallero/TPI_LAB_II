from Persona import Persona

class Propietario(Persona):
    def __init__(self, nombre, apellido, fecha_nac, correo):
        self.__mascotas = []
        super().__init__(nombre, apellido, fecha_nac, correo)

    def __str__(self):
        return f"""Nombre: {super().nombre}
Apellido: {super().apellido}
Fecha de nacimiento: {super().fechaNac}
Correo: {super().correo}
Mascotas: {self.__mascotas}"""
    
    def agregar_mascota(self, Mascota):
        self.__mascotas.append(Mascota)

    