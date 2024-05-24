class Raza:
    def __init__(self, nombre, codigo):
        self.nombre= nombre
        self.codigo= codigo

    def __str__(self):
        return f": *)Nombre: {self.nombre} *)Codigo: {self.codigo}"
    def __repr__(self):
        return f": *)Nombre: {self.nombre} *)Codigo: {self.codigo}"

    def get_nombre(self):
        return self.nombre
    def get_codigo(self):
        return self.codigo