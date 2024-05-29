class Raza:
    def __init__(self, nombre, tipoAnimal, codigo):
        self.__nombre = nombre
        self.__tipoAnimal = tipoAnimal
        self.__codigo = int(codigo)

    def __str__(self):
        return f"""Nombre: {self.__nombre}
        Codigo: {self.__codigo}
Tipo animal: {self.__tipoAnimal}"""

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

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo