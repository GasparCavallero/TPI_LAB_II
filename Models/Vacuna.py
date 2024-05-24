class Vacuna:
    def __init__(self, nombre, estado, codigo):
        self.nombre = nombre
        self.estado = estado
        self.codigo = int(codigo)

    def __str__(self):
        return f": *)Nombre: {self.nombre}, *)Estado: {self.estado}, *)Código: {self.codigo}."

    def __repr__(self):
        return f": *)Nombre: {self.nombre}, *)Estado: {self.estado}, *)Código: {self.codigo}."

    def get_nombre(self):
        return self.nombre
    def get_estado(self):
        return self.estado
    def get_codigo(self):
        return self.codigo