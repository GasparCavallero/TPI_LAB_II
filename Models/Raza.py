class Raza:
    def __init__(self, nombre, codigo):
        self.__nombre = nombre
        self.__codigo = int(codigo)

    def __str__(self):
        return f"""Nombre: {self.__nombre}
        Codigo: {self.__codigo}"""

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo