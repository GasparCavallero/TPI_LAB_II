class Consulta:
    def __init__(self, Veterinario, descripcion, veterinaria, fecha,codigo):
        self.__veterinario = Veterinario
        self.__descripcion = descripcion
        self.__veterinaria = veterinaria
        self.__fecha = fecha
        self.__diagnostico = ""
        self.__estado = True
        self.__codigo = int(codigo)

    def __str__(self):
        return f"""Fecha de la consulta: {self.__fecha}
Veterinario: {self.__veterinario}
Veterinaria: {self.__veterinaria}
Diagnostico: {self.__diagnostico}
Descripción: {self.__descripcion}
Anulada: {self.__estado}
Codigo: {self.__codigo}"""

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
    def veterinaria(self, codigo):
        self.__codigo = codigo
    
    def dar_alta(self):
        self.__estado = True

    def dar_baja(self):
        self.__estado = False

    def ishabilitado(self):
        if self.__estado==True:
            return True