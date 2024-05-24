class FichaMedica:
    def __init__(self, mascota, estado, Consulta, Vacuna):
        self.mascota = mascota
        self.estado = estado
        self.consulta = list[Consulta]
        self.vacuna= list[Vacuna]

    def __str__(self):
        return f": *)Mascota: {self.mascota} *)Estado: {self.estado} *)Consulta: {self.consulta} *)Vacunas: {self.vacuna}"

    def __repr__(self):
        return f": *)Mascota: {self.mascota} *)Estado: {self.estado} *)Consulta: {self.consulta} *)Vacunas: {self.vacuna}"

    def Dar_baja(self):
        pass
    def get_mascota(self):
        return self.mascota
    def get_estado(self):
        return self.estado
    def get_consulta(self):
        return self.consulta
    def get_vacuna(self):
        return self.vacuna
