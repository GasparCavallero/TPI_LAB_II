class VistaVacuna:
    def menu(self):
        opcion = "0"
        while opcion != "9":
            opcion = input("""💉 Menú de vacunas 💉 
[1] Ver un listado de todas las vacunas en el sistema
[2] Modificar una vacuna
[3] Crear una nueva vacuna
[4] Dar de baja una vacuna
[9] Volver
> """)
        return opcion