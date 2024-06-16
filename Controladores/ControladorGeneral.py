import tkinter as tk
from Vistas.VistaGeneral import VistaGeneral
from .ControladorRaza import ControladorRaza
from .ControladorVacuna import Controlador_Vacuna
from .ControladorMascota import Controlador_Mascota
from .ControladorPropietario import Controlador_Propietario
from .ControladorVeterinario import ControladorVeterinario
from .ControladorFichaMedica import ControladorFichaMedica
from .ControladorConsulta import ControladorConsulta
from .ControladorDiagnostico import ControladorDiagnostico
from .ControladorTratamiento import ControladorTratamiento

class ControladorGeneral():
    def __init__(self):
        """self.ventanaPrincipal = tk.Tk()
        self.view = VistaGeneral(self.ventanaPrincipal, self) # Le pasa la ventana que creó, y al controlador en sí
        self.ventanaPrincipal.title("Veterinaria")
        self.ventanaPrincipal.geometry("400x400")
        self.ventanaPrincipal.config(background="LightBlue4")
        self.ventanaPrincipal.mainloop()"""

        c = ControladorRaza()
        c.crear_nueva_raza("hola", "test")
        print(c.buscar_raza(2))
        c.modificar_raza(2)
        