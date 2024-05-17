class Persona:
    def __init__(self, nombre, apellido, fecha_nac, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Fecha de nacimiento: {self.fecha_nac}, Correo: {self.correo}."

    def __repr__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Fecha de nacimiento: {self.fecha_nac}, Correo: {self.correo}."

    def Dar_baja(self):
        pass
