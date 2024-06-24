from Vistas.VistaGeneral import VistaGeneral

class VistaVacuna(VistaGeneral):
    def menu(self):
        opcion: int = 0
        while opcion not in range(1, 6):
            try:
                opcion = int(input("""💉 Menú de vacunas 💉 
[1] Ver el listado de todas las vacunas en el sistema
[2] Modificar una vacuna
[3] Registrar una nueva vacuna
[4] Dar de baja una vacuna
[5] Volver
> """))
            except ValueError:
                self.mostrarErrorStrEnInt()
        return opcion
    
    def modificarVacuna(self, vacuna):
        print(f"Modificando vacuna: {vacuna.nombre}")
        nombre = self.inputStringNoVacia("Ingrese el nuevo nombre: ")
        return nombre
