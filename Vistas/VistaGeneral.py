import tkinter as tk

class VistaGeneral(): #tk.Frame    
    def menu():
        opcion: int = int(input("""💊 ¡Bienvenido/a al sistema de administración de veterinarias de Impulsive! 💊
[1] Gestión de razas 🦍
[2] Gestión de mascotas 🐱
[3] Gestión de personal veterinario 👩
[4] Gestión de propietarios/as 🧑‍🦲
[5] Gestión de fichas médicas 📄
[6] Gestión de vacunas 💉
[7] Gestión de diagnósticos 📝
[8] Gestión de tratamientos 🗂️
[9] Salir del sistema 👋
> """))
        return opcion