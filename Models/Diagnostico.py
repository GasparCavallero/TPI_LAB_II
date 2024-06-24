class Diagnostico:
    def __init__(self, codigo: int, mascota, fecha, descripcion):
        self.__codigo = codigo
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__mascota = mascota

    def __str__(self):
        return f"""Codigo: {self.__codigo} | Fecha: {self.__fecha} | Descripción: {self.__descripcion} | Mascota: {self.__mascota}"""

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

    @property
    def mascota(self):
        return self.__mascota
    
    @mascota.setter
    def mascota(self, mascota):
        self.__mascota = mascota

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo
  
    def agregar_tratamiento(self, Tratamiento):
        self.__tratamiento = Tratamiento

    def ishabilitado(self):
        if self.__estado == True:
            return "Activo"
        else:
            return "Anulado"