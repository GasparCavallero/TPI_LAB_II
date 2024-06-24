from Vistas.VistaGeneral import VistaGeneral

class VistaRaza(VistaGeneral):
    def menu(self):
        opcion: int = 0
        while opcion not in range(1,6):
            try:
                opcion = int(input("""🦍 Menú de razas 🦍
[1] Ver un listado de todas las razas en el sistema
[2] Modificar una raza
[3] Crear una nueva raza
[4] Eliminar una raza
[5] Volver
> """))
            except ValueError:
                self.mostrarErrorStrEnInt()
        return opcion

    def modificarRaza(self, raza):
        print(f"Modificando raza: {raza}")
        tipoAnimal = input("Nuevo tipo de animal: ")
        nombre = input("Nuevo nombre de raza: ")
        return tipoAnimal, nombre

    def crearNuevaRaza(self):
        nombre = self.inputStringNoVacia("Ingrese el nombre de la raza: ")
        tipoAnimal = self.inputStringNoVacia("Ingrese el tipo de animal: ")
        return tipoAnimal, nombre

