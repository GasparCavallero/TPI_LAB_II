class VistaVeterinario:
    def menu():
        opcion = "0"
        while opcion != "9":
            opcion = input("""⛑️  Menú de personal veterinario ⛑️
[1] Dar de alta un nuevo veterinario
[2] Modificar un veterinario ya registrado
[3] Eliminar un veterinario del sistema
[9] Volver
> """)