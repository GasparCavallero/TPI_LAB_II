class Diagnostico:
    def __init__(self, fecha, descripcion,codigo):
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tratamiento = ""
        self.__codigo= int(codigo)

    def __str__(self):
        return f"""Fecha: {self.__fecha}
Descripción: {self.__descripcion}
Tratamiento: {self.__tratamiento}
Codigo: {self.__codigo}"""

    @property
    def tratamiento(self):
        return self.__tratamiento

    @tratamiento.setter
    def tratamiento(self, Tratamiento):
        self.__tratamiento = Tratamiento

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
  
    def agregar_tratamiento(self, Tratamiento):
        self.__tratamiento = Tratamiento
