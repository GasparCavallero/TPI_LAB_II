from Vistas.VistaGeneral import VistaGeneral

class VistaTratamiento(VistaGeneral):
    def menu(self):
        opcion: int = 0
        while opcion not in range(1, 6):
            try:
                opcion = int(input("""🗂️  Menú de tratamientos 🗂️
[1] Ver un listado de todos los tratamientos en el sistema
[2] Modificar un tratamiento
[3] Crear un nuevo tratamiento
[4] Eliminar un tratamiento
[5] Volver
> """))
            except ValueError:
                self.mostrarErrorStrEnInt()
        return opcion
    
    def modificar_tratamiento(self, tratamiento):
        print(f"Modificando tratamiento: {tratamiento}")
        descripcion = self.inputStringNoVacia("Ingrese la nueva descripción: ")
        mascota = self.pedirCodigo("Ingrese código de la mascota: ")
        return mascota, descripcion