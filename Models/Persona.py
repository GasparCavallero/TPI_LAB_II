class Persona():
    def __init__(self, estado: bool, nombre, apellido, fechaNac, correo):
        self.__estado = estado
        self.__nombre = nombre
        self.__apellido = apellido
        self.__documento=documento
        self.__fechaNac = fechaNac
        self.__correo = correo

    def __str__(self):
        return f"""Estado: {self.__estado}
Nombre: {self.__nombre}
Apellido: {self.__apellido}
Documento: {self.__documento}
Fecha de nacimiento: {self.__fechaNac}
Correo: {self.__correo}"""

    @property
    def estado(self):
        return self.__estado

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
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, documento):
        self.__documento= documento

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

    def alta(self):
        self.__estado = True

    def baja(self):
        self.__estado = False 

    def habilitado(self):
        if self.__estado == True:
            return True
