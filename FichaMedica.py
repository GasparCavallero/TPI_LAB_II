class FichaMedica:
    def __init__(self, mascota, estado, consulta):
        self.mascota = mascota
        self.estado = estado
        self.consulta = consulta

    def __str__(self):
        return f"Mascota: {self.mascota}, Estado: {self.estado}, Consulta: {self.consulta}."

    def __repr__(self):
        return f"Mascota: {self.mascota}, Estado: {self.estado}, Consulta: {self.consulta}."

    def Dar_baja(self):
        pass
