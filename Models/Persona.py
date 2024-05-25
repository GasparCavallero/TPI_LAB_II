class Persona():
    def __init__(self, nombre, apellido, fechaNac, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaNac = fechaNac
        self.__correo = correo
        self.__estado = True

    def __str__(self):
        return f"""Nombre: {self.__nombre}
Apellido: {self.__apellido}
Fecha de nacimiento: {self.__fechaNac}
Correo: {self.__correo}
Estado: {self.__estado}"""

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def fechaNac(self):
        return self.__fechaNac
    
    @fechaNac.setter
    def fechaNac(self, fechaNac):
        self.__fechaNac = fechaNac

    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self, correo):
        self.__correo = correo

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, correo):
        self.__estado = correo

    def dar_alta(self):
        self.__estado = True

    def dar_baja(self):
        self.__estado = False 
