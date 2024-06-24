import tkinter as tk
from Vistas.VistaGeneral import VistaGeneral
from .ControladorRaza import ControladorRaza
from .ControladorVacuna import ControladorVacuna
from .ControladorMascota import ControladorMascota
from .ControladorPropietario import ControladorPropietario
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

        self.cp = ControladorPropietario()
        cfm = ControladorFichaMedica()
        self.cv = ControladorVeterinario()
        self.cr = ControladorRaza()
        self.cm = ControladorMascota(self.cp, cfm)
        cvv = ControladorVacuna()
        cr = ControladorRaza()
        ct = ControladorTratamiento()
        cd = ControladorDiagnostico()
        cc = ControladorConsulta()
        
        self.cv.crear_nuevo_veterinario()
        self.cv.guardar_veterinarios()

        """cv.baja_veterinario()
        [print(c) for c in cv.get_lista_veterinarios()]"""
        # self.menu()

    def guardar(self):
        ...

    def menu(self):
        opcion = VistaGeneral.menu()
        match opcion:
            case 1:
                self.cr.menu()
            case 2:
                self.cm.menu()
            case 3:
                self.cv.menu()
            case 4:
                self.cp.menu()
            case 5:
                ...
            case 6:
                ...
            case 7:
                ...
            case 8:
                ...
            case 0:
                ...
            case _:
                ...