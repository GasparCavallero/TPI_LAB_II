class Tratamiento:
    def __init__(self, codigo: int, fecha, descripcion):
        self.__codigo = codigo
        self.__fecha = fecha
        self.__descripcion = descripcion

    def __str__(self):
        return f"""Codigo: {self.__codigo}
Fecha: {self.__fecha}
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

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo