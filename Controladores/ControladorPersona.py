from Models.Persona import Persona


class ControladorPersona:
    def __init__(self, vista):
        self._vista = vista

    def crear_persona(self):
        self.persona = Persona(
            self._vista.solicitar_nombre(),
            self._vista.solicitar_apellido(),
            self._vista.solicitar_fecha(),
            self._vista.solicitar_correo(),
        )

    def mostrar_informacion(self):
        data = self.persona
        self._vista.mostrar_informacion(data)
