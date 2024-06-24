from Vistas.VistaGeneral import VistaGeneral

class VistaVeterinario(VistaGeneral):
    def menu(self):
        opcion: int = 0
        while opcion not in range(1, 6):
            try:
                opcion = int(input("""⛑️  Menú de personal veterinario ⛑️
[1] Listado de todos los veterinarios
[2] Dar de alta un nuevo veterinario
[3] Modificar un veterinario ya registrado
[4] Dar de baja un veterinario del sistema
[5] Volver
> """))
            except ValueError:
                self.mostrarErrorStrEnInt()
        return opcion
    
    def crearVeterinario(self):
        nombre = self.inputStringNoVacia("Ingrese el nombre: ")
        apellido = self.inputStringNoVacia("Ingrese el apellido: ")
        fechaNac = self.inputStringNoVacia("Ingrese la fecha de nacimiento formato DD/MM/AAAA: ")
        correo = self.inputStringNoVacia("Ingrese el correo: ")
        especialidad = self.inputStringNoVacia("Ingrese la especialidad: ")
        return nombre, apellido, fechaNac, correo, especialidad

    def modificarVeterinario(self, veterinario):
        print(f"Modificando veterinario/a: {veterinario}")
        nombre = self.inputStringNoVacia("Ingrese el nuevo nombre: ")
        apellido = self.inputStringNoVacia("Ingrese el nuevo apellido: ")
        fechaNac = self.inputStringNoVacia("Ingrese la nueva fecha de nacimiento formato DD/MM/AAAA: ")
        correo = self.inputStringNoVacia("Ingrese el nuevo correo: ")
        especialidad = self.inputStringNoVacia("Ingrese la nueva especialidad: ")
        return nombre, apellido, fechaNac, correo, especialidad