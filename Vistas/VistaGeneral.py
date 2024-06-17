# import tkinter as tk
#
# class VistaGeneral(tk.Frame):
#     def __init__(self, parent, controlador):
#         self.controlador = controlador
#         tk.Frame.__init__(self, parent, bg="yellow", bd=2,
#         relief=tk.RIDGE) # Estilos, se puede modificar
#         self.parent = parent
#         self.pack()


class VistaGeneral:
    def mostrarMenu(self):
        print(
            """MENU VETERINARIA
[1]-Ver Consulta
[2]-Ver Diagnostico
[3]-Ver Ficha Medica
[4]-Ver Mascota
[5]-Ver Propietario
[6]-Ver Raza
[7]-Ver Tratamiento
[8]-Ver Vacuna
[9]-Ver Veterinario
[0]-Salir"""
        )
        op = input("Ingrese la opcion que desea: ")
        return op