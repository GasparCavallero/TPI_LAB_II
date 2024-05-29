import tkinter as tk

class VistaGeneral(tk.Frame):
    def __init__(self, parent, controlador):
        self.controlador = controlador
        tk.Frame.__init__(self, parent, bg="yellow", bd=2, 
           relief=tk.RIDGE) # Estilos, se puede modificar
        self.parent = parent
        self.pack()