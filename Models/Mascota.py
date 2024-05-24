class Mascota:
    def __init__(self, Raza, nombre, fecha_nac, Fichamedica, tipo_animal, Propietario, estado, codigo):
        self.raza = Raza
        self.propietario= Propietario
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.fichamedica= Fichamedica
        self.tipo_animal = tipo_animal
        self.estado = estado
        self.codigo = codigo

    def __str__(self):
        return (f": *)Raza: {self.raza} *)Nombre: {self.nombre} *)Fecha de nacimiento: {self.fecha_nac} *)Tipo de animal: {self.tipo_animal} *)Propietario: {self.propietario} *)Estado: {self.estado} *)Código: {self.codigo} *)Ficha médica: {self.fichamedica}")

    def __repr__(self):
        return f": *)Raza: {self.raza} *)Nombre: {self.nombre} *)Fecha de nacimiento: {self.fecha_nac} *)Tipo de animal: {self.tipo_animal} *)Propietario: {self.propietario} *)Estado: {self.estado} *)Código: {self.codigo} *)Ficha médica: {self.fichamedica}"

    def calc_edad(self):
        pass

    def get_raza(self):
        return self.raza
    def get_nombre(self):
        return self.nombre
    def get_fichamedica(self):
        return self.fichamedica
    def get_codigo(self):
        return self.codigo
    def get_estado(self):
        return self.estado
