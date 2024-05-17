class Consulta:
    def __init__(
        self,
        detalles,
        tratamiento,
        diagnostico,
        fecha,
        mascota,
        veterinaria,
        estado,
        veterinario,
    ):
        self.detalles = detalles
        self.tratamiento = tratamiento
        self.diagnostico = diagnostico
        self.fecha = fecha
        self.mascota = mascota
        self.veterinaria = veterinaria
        self.estado = estado
        self.veterinario = veterinario

    def __str__(self):
        return f"Detalles: {self.detalles}, Tratamiento: {self.tratamiento}, Diagnóstico: {self.diagnostico}, Fecha: {self.fecha}, Mascota: {self.mascota}, Veterinaria: {self.veterinaria}, Estado: {self.estado}, Veterinario: {self.veterinario}."

    def __repr__(self):
        return f"Detalles: {self.detalles}, Tratamiento: {self.tratamiento}, Diagnóstico: {self.diagnostico}, Fecha: {self.fecha}, Mascota: {self.mascota}, Veterinaria: {self.veterinaria}, Estado: {self.estado}, Veterinario: {self.veterinario}."

    def Dar_baja(self):
        pass

    def Sum_consulta(self):
        pass
