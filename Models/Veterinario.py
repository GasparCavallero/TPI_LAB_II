import Persona
class Veterinario(Persona):
    def __init__(self, codigo, especialidad, nombre, apellido, fecha_nac, correo):
        self.codigo= int(codigo)
        self.especialidad= especialidad
        super().__init__(nombre, apellido, fecha_nac, correo)

    def __str__(self):
        return f": *)Nombre: {self.nombre} *)Apellido: {self.apellido} *)Especialidad: {self.especialidad} *)Correo: {self.correo} *)Fecha de nacimieno: {self.fecha_nac} *)Codigo: {self.codigo}"
    def __repr__(self):
        return f": *)Nombre: {self.nombre} *)Apellido: {self.apellido} *)Especialidad: {self.especialidad} *)Correo: {self.correo} *)Fecha de nacimieno: {self.fecha_nac} *)Codigo: {self.codigo}"

    def get_codigo(self):
        return self.codigo
    def get_especialidad(self):
        return self.especialidad
