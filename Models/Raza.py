class Raza:
    def __init__(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return f"Nombre: {self.__nombre}"

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre