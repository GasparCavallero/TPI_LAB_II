import tkinter as tk

class VistaGeneral(): #tk.Frame
    """def __init__(self, parent, controlador):
        self.controlador = controlador
        tk.Frame.__init__(self, parent, bg="yellow", bd=2, 
           relief=tk.RIDGE) # Estilos, se puede modificar
        self.parent = parent
        self.pack()"""
    
    def menu():
        opcion: int = int(input("""💊 ¡Bienvenido al sistema de administración de veterinarias! 💊
[1] Gestión de razas 🦍
[2] Gestión de mascotas 🐱
[3] Gestión de personal veterinario 👩
[4] Gestión de clientes 🧑‍🦲
[5] Gestión de fichas médicas 📄
[6] Gestión de vacunas 💉
[7] Gestión de diagnósticos 📝
[8] Gestión de tratamientos 🗂️
[0] Salir del sistema 👋
> """))
        return opcion