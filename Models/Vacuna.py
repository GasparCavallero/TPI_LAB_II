class Vacuna:
    def __init__(self, nombre):
        self.__estado = True
        self.__nombre = nombre

    def __str__(self):
        return f"""Nombre: {self.__nombre}
Estado: {self.__estado}"""

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def dar_baja(self):
        self.__estado = False
    
    def dar_alta(self):
        self.__estado = True
    
