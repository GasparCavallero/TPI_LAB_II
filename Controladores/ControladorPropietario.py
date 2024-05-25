from Models.Propietario import Propietario
from Vistas.Vista_Propietario import Vista_Propietario


class Controlador_Propietario:
    def __init__(self):
        self._vista = Vista_Propietario()
        self._modelo = Propietario()

    def Buscar_Propietario(self, codigo):
        with open("Archivos\\propietario.txt", "r") as file:
            for line in file:
                linea = line.split(",")
                if int(linea[0]) == int(codigo):
                    self._modelo = Propietario(linea[0], linea[1])
                    self._modelo.setDatos_Propietario([])
                    return self._modelo
        return None

    def Mostrar_Datos(self):
        self._vista.Visualizar_Datos(self._modelo.getDatos_Propietario())
