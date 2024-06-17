# import tkinter as tk
# from Vistas.VistaGeneral import VistaGeneral

# class ControladorGeneral():
#     def __init__(self):
#         self.ventanaPrincipal = tk.Tk()
#         self.view = VistaGeneral(self.ventanaPrincipal, self) # Le pasa la ventana que creó, y al controlador en sí
#         self.ventanaPrincipal.title("Veterinaria")
#         self.ventanaPrincipal.geometry("400x400")
#         self.ventanaPrincipal.config(background="LightBlue4")
#         self.ventanaPrincipal.mainloop()
from Vistas.VistaGeneral import VistaGeneral
from Controladores.ControladorConsulta import Controlador_Consulta
from Controladores.ControladorDiagnostico import Controlador_Diagnostico
from Controladores.ControladorFichaMedica import ControladorFichaMedica
from Controladores.ControladorMascota import ControladorMascota
from Controladores.ControladorPropietario import Controlador_Propietario
from Controladores.ControladorRaza import ControladorRaza
from Controladores.ControladorTratamiento import Controlador_Tratamiento
from Controladores.ControladorVacuna import Controlador_Vacuna
from Controladores.ControladorVeterinario import Controlador_Veterinario

class ControladorGeneral:
    def __init__(self) -> None:
        self.vista = VistaGeneral()
    
    def iniciar(self):
        op = self.vista.mostrarMenu()
        if op == "1":
            Controlador_Consulta()
        elif op == "2":
            Controlador_Diagnostico()
        elif op == "3":
            ControladorFichaMedica()
        elif op == "4":
            ControladorMascota()
        elif op == "5":
            Controlador_Propietario()
        elif op == "6":
            ControladorRaza()
        elif op == "7":
            Controlador_Tratamiento()
        elif op == "8":
            Controlador_Vacuna()
        elif op == "9":
            Controlador_Veterinario()