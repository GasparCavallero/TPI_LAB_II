class Mascota:
    def __init__(self, Propietario, Raza, FichaMedica, nombre, fechaNac,codigo):
        self.__propietario = Propietario
        self.__raza = Raza
        self.__nombre = nombre
        self.__fechaNac = fechaNac
        self.__fichaMedica = FichaMedica
        self.__estado = True
        self.__codigo= int(codigo)

    def __str__(self):
        return f"""Propietario: {self.__propietario}
Raza: {self.__raza}
Nombre: {self.__nombre}
Fecha de nacimiento: {self.__fechaNac}
Ficha médica: {self.__fichaMedica}
Estado: {self.__estado}
Codigo: {self.__codigo}"""

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