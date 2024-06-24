class VistaTratamiento:
    def menu(self):
        opcion = "0"
        while opcion != "9":
            opcion = input("""🗂️  Menú de tratamientos 🗂️
[1] Ver un listado de todos los tratamientos en el sistema
[2] Modificar un tratamiento
[3] Crear un nuevo tratamiento
[4] Eliminar un tratamiento
[9] Volver
""")