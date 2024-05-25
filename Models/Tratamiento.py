class Tratamiento:
    def __init__(self, fecha, descripcion):
        self.__fecha = fecha
        self.__descripcion = descripcion

    def __str__(self):
        return f"""Fecha: {self.__fecha}
Descripción: {self.__descripcion}"""

    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion
    
