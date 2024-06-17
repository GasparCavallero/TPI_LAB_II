class Mascota:
    def __init__(self, codigo: int, estado: bool, Propietario, Raza, FichaMedica, nombre, fechaNac):
        self.__codigo = codigo
        self.__estado = estado
        self.__propietario = Propietario
        self.__raza = Raza
        self.__fichaMedica = FichaMedica
        self.__nombre = nombre
        self.__fechaNac = fechaNac
        
    def __str__(self):
        return f"""Codigo: {self.__codigo}
Estado: {self.__estado}
Propietario: {self.__propietario}
Raza: {self.__raza}
Ficha médica: {self.__fichaMedica}
Nombre: {self.__nombre}
Fecha de nacimiento: {self.__fechaNac}"""

    @property
    def propietario(self):
        return self.__propietario

    @propietario.setter
    def propietario(self, Propietario):
        self.__propietario = Propietario

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, Raza):
        self.__raza = Raza

    @property
    def fichamedica(self):
        return self.__fichaMedica

    @fichamedica.setter
    def fichamedica(self, FichaMedica):
        self.__fichaMedica = FichaMedica
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def fechaNac(self):
        return self.__fechaNac

    @fechaNac.setter
    def fechaNac(self, fechaNac):
        self.__fechaNac = fechaNac

    @property
    def tipoAnimal(self):
        return self.__tipoAnimal

    @tipoAnimal.setter
    def tipoAnimal(self, tipoAnimal):
        self.__tipoAnimal = tipoAnimal

    def habilitar(self):
        self.__estado = True

    def anular(self):
        self.__estado = False

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def veterinaria(self, codigo):
        self.__codigo = codigo