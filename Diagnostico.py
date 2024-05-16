class diagnostico:
    def __init__(self, estado, veterinario, fecha, descripcion):
        self.estado = estado
        self.veterinario = veterinario
        self.fecha = fecha
        self.descripcion = descripcion

    def __str__(self):
        return f"Estado: {self.estado}, Veterinario: {self.veterinario}, Fecha: {self.fecha}, Descripción: {self.descripcion}."

    def __repr__(self):
        return f"Estado: {self.estado}, Veterinario: {self.veterinario}, Fecha: {self.fecha}, Descripción: {self.descripcion}."

    def Dar_baja(self):
        pass
