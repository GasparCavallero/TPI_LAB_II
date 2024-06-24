from Vistas.VistaGeneral import VistaGeneral

class VistaMascota(VistaGeneral):
    def menu(self):
        opcion: int = 0
        while opcion not in range(1, 6):
            try:
                opcion = int(input("""🐱 Menú de mascotas 🐱
[1] Ver un listado de todas las mascotas en el sistema
[2] Dar de alta una mascota PENDIENTE PORQUE TIENE QUE VER CON PROPIETARIO
[3] Modificar datos de una mascota existente
[4] Anular una mascota del sistema
[5] Volver
> """))
            except ValueError:
                self.mostrarErrorStrEnInt()
        return opcion
    
    def modificarMascota(self, mascota):
        print(f"Modificando mascota: {mascota}")
        nombre = self.inputStringNoVacia("Ingrese el nuevo nombre de la mascota: ")
        fechaNac = self.inputStringNoVacia("Ingrese la nueva fecha de nacimiento formato DD/MM/AAAA: ")
        return nombre, fechaNac