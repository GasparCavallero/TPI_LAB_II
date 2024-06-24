class VistaRaza:
    def menu():
        opcion = "0"
        while opcion != "9":
            opcion = input("""🦍 Menú de razas 🦍
[1] Ver un listado de todas las razas en el sistema
[2] Modificar una raza
[3] Crear una nueva raza
[4] Eliminar una raza
[9] Volver
> """)
        return opcion