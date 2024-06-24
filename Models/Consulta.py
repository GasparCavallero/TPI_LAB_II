class Consulta:
    def __init__(self, codigo: int, estado: bool, Veterinario: int, descripcion, fecha):
        self.__codigo = codigo
        self.__estado = estado
        self.__veterinario = Veterinario
        self.__veterinaria = "Veterinaria San Pedrito"
        self.__descripcion = descripcion
        self.__fecha = fecha

    def __str__(self):
        return f"""Codigo: {self.__codigo} | Estado: {self.ishabilitado()} | Fecha de la consulta: {self.__fecha} | Veterinario: {self.__veterinario} | Veterinaria: {self.__veterinaria} | Descripción: {self.__descripcion}"""

    ### Get/Set

    @property
    def veterinario(self):
        return self.__veterinario
    
    @veterinario.setter
    def veterinario(self, Veterinario):
        self.__veterinario = Veterinario

    @property
    def diagnostico(self):
        if self.__diagnostico: return self.__diagnostico
        return "No hay un diagnóstico cargado"

    @diagnostico.setter
    def diagnostico(self, Diagnostico):
        self.__diagnostico = Diagnostico

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
    def veterinaria(self):
        return self.__veterinaria
    
    @veterinaria.setter
    def veterinaria(self, veterinaria):
        self.__veterinaria = veterinaria

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    def dar_alta(self):
        self.__estado = True

    def dar_baja(self):
        self.__estado = False

    def ishabilitado(self):
        if self.__estado == True:
            return "Vigente"
        else:
            return "Anulada"