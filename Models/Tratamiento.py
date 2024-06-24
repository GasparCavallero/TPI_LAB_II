class Tratamiento:
    def __init__(self, codigo: int, mascota, fecha, descripcion):
        self.__codigo = codigo
        self.__mascota = mascota
        self.__fecha = fecha
        self.__descripcion = descripcion

    def __str__(self):
        return f"""Codigo: {self.__codigo}
Mascota: {self.__mascota}
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
    def mascota(self):
        return self.__mascota
    
    @mascota.setter
    def mascota(self, mascota):
        self.__mascota = mascota

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo