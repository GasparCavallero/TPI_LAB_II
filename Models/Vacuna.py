class Vacuna:
    def __init__(self, codigo: int, estado: bool, nombre: str):
        self.__codigo = codigo
        self.__estado = estado
        self.__nombre = nombre
        
    def __str__(self):
        return f"""Codigo: {self.__codigo}
Estado: {self.__estado}
Nombre: {self.__nombre}"""

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo

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

    def anular(self):
        self.__estado = False
    
    def dar_alta(self):
        self.__estado = True

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo

    def habilitado(self):
        if self.__estado == True:
            return True
