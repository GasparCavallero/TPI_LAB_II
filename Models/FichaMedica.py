class FichaMedica:
    def __init__(self, mascota,codigo):
        self.__mascota = mascota
        self.__consultas = []
        self.__vacunas = []
        self.__estado = True
        self.__codigo= int(codigo)

    def __str__(self):
        return f"""Mascota: {self.__mascota}
Consulta: {self.__consultas}
Vacunas: {self.__vacunas}
Estado: {self.__estado}
Codigo: {self.__codigo}"""

    @property
    def mascota(self):
        return self.__mascota
    
    @mascota.setter
    def mascota(self, mascota):
        self.__mascota = mascota
 
    @property
    def consultas(self):
        return self.__consultas
    
    @consultas.setter
    def consultas(self, consultas):
        self.__consultas = consultas

    @property
    def vacunas(self):
        return self.__vacunas
    
    @vacunas.setter
    def vacunas(self, vacunas):
        self.__vacunas = vacunas

    def agregar_vacuna(self, Vacuna):
        self.__vacunas.append(Vacuna)

    def anular_vacuna(self, indice):
        return

    def agregar_consulta(self, Consulta):
        self.__consultas.append(Consulta)

    def anular_consulta(self, indice):
        return

    def dar_alta(self):
        self.__estado = True

    def dar_baja(self):
        self.__estado = False

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo

    def ishabilitado(self):
        if self.__estado==True:
            return True
