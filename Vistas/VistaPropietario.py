class VistaPropietario:
    def menu(self):
        opcion = "0"
        while opcion != "9":
            opcion = input("""🧑‍🦲 Menú de propietarios/as 🧑‍🦲
[1] Dar de alta un nuevo propietario
[2] Modificar un propietario ya registrado
[3] Eliminar un propietario del sistema
[9] Volver
> """)
        return opcion