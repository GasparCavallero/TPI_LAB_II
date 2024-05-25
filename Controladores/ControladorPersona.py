from Models.Persona import Persona

class ControladorPersona:
    def __init__(self, vista):
        self.vista = vista
    
    def crear_persona(self):
        self.persona = Persona(
            self.vista.solicitar_nombre(),
            self.vista.solicitar_apellido(),
            self.vista.solicitar_fecha(),
            self.vista.solicitar_correo()
        )

    def mostrar_informacion(self):
        data = self.persona
        self.vista.mostrar_informacion(data)