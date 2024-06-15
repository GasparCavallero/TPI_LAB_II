import tkinter as tk
from Vistas.VistaGeneral import VistaGeneral
from .ControladorRaza import Controlador_Raza

class ControladorGeneral():
    def __init__(self):
        """self.ventanaPrincipal = tk.Tk()
        self.view = VistaGeneral(self.ventanaPrincipal, self) # Le pasa la ventana que creó, y al controlador en sí
        self.ventanaPrincipal.title("Veterinaria")
        self.ventanaPrincipal.geometry("400x400")
        self.ventanaPrincipal.config(background="LightBlue4")
        self.ventanaPrincipal.mainloop()"""

        c = Controlador_Raza()
        razas = c.getListaRazas()
        [print(c) for r in razas]