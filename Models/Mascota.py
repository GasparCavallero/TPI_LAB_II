class Mascota:
    def __init__(
        self, raza, nombre, fecha_nac, tipo_animal, propietario, estado, codigo, vacuna
    ):
        self.raza = raza
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.tipo_animal = tipo_animal
        self.propietario = propietario
        self.estado = estado
        self.codigo = codigo
        self.vacuna = vacuna

    def __str__(self):
        return f"Raza: {self.raza}, Nombre: {self.nombre}, Fecha de nacimiento: {self.fecha_nac}, Tipo de animal: {self.tipo_animal}, Propietario: {self.propietario}, Estado: {self.estado}, Código: {self.codigo}, Vacuna: {self.vacuna}."

    def __repr__(self):
        return f"Raza: {self.raza}, Nombre: {self.nombre}, Fecha de nacimiento: {self.fecha_nac}, Tipo de animal: {self.tipo_animal}, Propietario: {self.propietario}, Estado: {self.estado}, Código: {self.codigo}, Vacuna: {self.vacuna}."

    def Dar_baja(self):
        pass

    def Calc_edad(self):
        pass
