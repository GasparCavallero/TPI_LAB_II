class Tratamiento:
    def __init__(self, estado, fecha, descripcion):
        self.estado= int(estado)
        self.fecha = fecha
        self.descripcion = descripcion

    def __str__(self):
        return f": *)Estado: {self.estado} *)Fecha {self.fecha} *)Descripción: {self.descripcion}"
    def __repr__(self):
        return f": *)Estado: {self.estado} *)Fecha {self.fecha} *)Descripción: {self.descripcion}"

    def get_estado(self):
        return self.estado
    def get_fecha(self):
        return self.fecha
    def get_descripcion(self):
        return self.descripcion