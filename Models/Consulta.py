class Consulta:
    def __init__(self,fecha, Veterinario, descripcion, Diagnostico, veterinaria, codigo):
        self.fecha= fecha
        self.veterinario= Veterinario
        self.descripcion= descripcion
        self.diagnostico= Diagnostico
        self.veterinaria= veterinaria
        self.codigo= int(codigo)

    def __str__(self):
        return f": *)Fecha de la cosulta: {self.fecha} *)Veterinario: {self.veterinario} *)Veterinara: {self.veterinaria} *)Diagnostico: {self.diagnostico} *)Estado: {self.estado} *)Descripción: {self.descripcion} *)Codigo: {self.codigo}"

    def __repr__(self):
        return f": *)Fecha de la cosulta: {self.fecha} *)Veterinario: {self.veterinario} *)Veterinara: {self.veterinaria} *)Diagnostico: {self.diagnostico} *)Estado: {self.estado} *)Descripción: {self.descripcion} *)Codigo: {self.codigo}"

    def get_fecha(self):
        return self.fecha
    def get_veterinario(self):
        return self.veterinario
    def get_descripcion(self):
        return self.descripcion
    def get_diagnostico(self):
        return self.diagnostico
    def get_veterinaria(self):
        return self.veterinaria
    def get_codigo(self):
        return self.codigo