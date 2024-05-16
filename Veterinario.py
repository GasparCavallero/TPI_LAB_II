class Veterinario:
    def __init__(self, estado, codigo, especialidad):
        self.estado = estado
        self.codigo = codigo
        self.especialidad = especialidad

    def __str__(self):
        return f"Estado: {self.estado}, Código: {self.codigo}, Especialidad: {self.especialidad}."

    def __repr__(self):
        return f"Estado: {self.estado}, Código: {self.codigo}, Especialidad: {self.especialidad}."
