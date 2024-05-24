import Persona
class Propietario(Persona):
    def __init__(self, estado, codigo, nombre, apellido, fecha_nac, correo, Mascotas):
        self.estado = estado
        self.codigo = codigo
        self.mascotas= list[Mascotas]
        super().__init__(nombre, apellido, fecha_nac, correo)

    def __str__(self):
        return f": *)Nombre: {self.nombre} *)Apellido: {self.apellido} *)Correo: {self.correo} *)Fecha de nacimieno: {self.fecha_nac} *)Estado: {self.estado} *)Codigo: {self.codigo}"

    def __repr__(self):
        return f": *)Nombre: {self.nombre} *)Apellido: {self.apellido} *)Correo: {self.correo} *)Fecha de nacimieno: {self.fecha_nac} *)Estado: {self.estado} *)Codigo: {self.codigo}"

    def get_estado(self):
        return self.estado
    def get_codigo(self):
        return self.codigo
    def get_mascotas(self):
        return self.mascotas