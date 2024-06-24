class VistaMascota:
    def menu():
        opcion = "0"
        while opcion != "9":
            opcion = input("""🐱 Menú de mascotas 🐱
[1] Ver un listado de todas las mascotas en el sistema
[2] Dar de alta una mascota
[3] Modificar datos de una mascota existente
[4] Eliminar una mascota del sistema
[9] Volver
> """)
        return opcion
        