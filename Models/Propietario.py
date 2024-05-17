class Propietario:
    def __init__(self, estado, codigo):
        self.estado = estado
        self.codigo = codigo

    def __str__(self):
        return f"Estado: {self.estado}, Código: {self.codigo}."

    def __repr__(self):
        return f"Estado: {self.estado}, Código: {self.codigo}."
