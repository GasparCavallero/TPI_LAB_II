class Raza:
    def __init__(self, codigo: int, estado: bool, tipoAnimal: str, nombre: str):
        self.__codigo = codigo
        self.__estado = estado
        self.__tipoAnimal = tipoAnimal
        self.__nombre = nombre

    def __str__(self):
        return f"""Codigo: {self.__codigo}
Estado: {self.__estado}
Tipo animal: {self.__tipoAnimal}
Nombre: {self.__nombre}"""

    def anular(self):
        self.__estado = False

    def habilitar(self):
        self.__estado = True

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def tipoAnimal(self):
        return self.__tipoAnimal

    @tipoAnimal.setter
    def tipoAnimal(self, tipoAnimal):
        self.__tipoAnimal = tipoAnimal
