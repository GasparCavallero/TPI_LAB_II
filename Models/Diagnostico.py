class Diagnostico:
    def __init__(self, Tratamiento, fecha, descripcion):
        self.fecha= fecha
        self.tratamiento = Tratamiento
        self.descripcion= descripcion

    def __str__(self):
        return f": *)Fecha: {self.fecha} *)Tratamiento: {self.tratamiento} *)Descripción: {self.descripcion}"
    def __repr__(self):
        return f": *)Fecha: {self.fecha} *)Tratamiento: {self.tratamiento} *)Descripción: {self.descripcion}"

    def get_fecha(self):
        return self.fecha
    def get_tratamiento(self):
        return self.tratamiento
    def get_descripcion(self):
        return self.descripcion
