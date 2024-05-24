from Models.Raza import Raza
from Vistas.Vista_Raza import Vista_Raza


class Controlador_Raza:
    def __init__(self):
        self._vista = Vista_Raza()
        self._modelo = Raza()

    def Buscar_Raza(self, codigo):
        with open("raza.txt", "r") as file:
            for line in file:
                linea = line.split(",")
                if int(linea[0]) == int(codigo):
                    self._modelo = Raza(linea[0], linea[1])
                    self._modelo.setDatos_Raza([])
                    return self._modelo
        return None

    def Mostrar_Datos(self):
        self._vista.Visualizar_Datos(self._modelo.getDatos_Raza())
