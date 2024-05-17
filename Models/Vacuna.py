class Vacuna:
    def __init__(self, nombre, estado, codigo):
        self.nombre = nombre
        self.estado = estado
        self.codigo = codigo

    def __str__(self):
        return f"Nombre: {self.nombre}, Estado: {self.estado}, Código: {self.codigo}."

    def __repr__(self):
        return f"Nombre: {self.nombre}, Estado: {self.estado}, Código: {self.codigo}."

    def Dar_baja(self):
        pass
