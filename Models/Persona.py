class Persona:
    def __init__(self, nombre, apellido, fecha_nac, correo, estado):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.correo = correo
        self.estado= estado

    def __str__(self):
        return f": *)Nombre: {self.nombre} *)Apellido: {self.apellido} *)Fecha de nacimiento: {self.fecha_nac} *)Correo: {self.correo} *)Estado: {self.estado}"

    def __repr__(self):
        return f": *)Nombre: {self.nombre} *)Apellido: {self.apellido} *)Fecha de nacimiento: {self.fecha_nac} *)Correo: {self.correo} *)Estado: {self.estado}"

    def dar_baja(self):
        pass

    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_fecha_nac(self):
        return self.fecha_nac
    def get_correo(self):
        return self.correo
    def get_estado(self):
        return self.estado