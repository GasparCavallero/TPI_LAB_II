class FichaMedica:
    def __init__(self, codigo: int, estado: bool, Mascota, listaConsultas, listaVacunas):
        self.__codigo = codigo
        self.__estado = estado
        self.__mascota = Mascota
        self.__listaConsultas = listaConsultas
        self.__listaVacunas = listaVacunas

    def __str__(self):
        return f"""Codigo: {self.__codigo}
Estado: {self.__estado}
Mascota: {self.__mascota}
Consulta: {self.__listaConsultas}
Vacunas: {self.__listaVacunas}
"""

    @property
    def codigo(self):
        return self.__codigo

    @property
    def mascota(self):
        return self.__mascota
    
    @mascota.setter
    def mascota(self, mascota):
        self.__mascota = mascota
 
    @property
    def consultas(self):
        return self.__listaConsultas
    
    @consultas.setter
    def consultas(self, consultas):
        self.__listaConsultas = consultas

    @property
    def vacunas(self):
        return self.__listaVacunas
    
    @vacunas.setter
    def vacunas(self, vacunas):
        self.__listaVacunas = vacunas

    def agregar_vacuna(self, Vacuna):
        self.__listaVacunas.append(Vacuna)

    def anular_vacuna(self, indice):
        return

    def agregar_consulta(self, Consulta):
        self.__listaConsultas.append(Consulta)

    def anular_consulta(self, indice):
        return

    def dar_alta(self):
        self.__estado = True

    def dar_baja(self):
        self.__estado = False

