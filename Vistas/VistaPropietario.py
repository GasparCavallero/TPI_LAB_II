from Vistas.VistaGeneral import VistaGeneral

class VistaPropietario(VistaGeneral):
    def menu(self):
        opcion: int = 0
        while opcion not in range(1, 6):
            try:
                opcion = int(input("""🧑‍🦲 Menú de propietarios/as 🧑‍🦲
[1] Listado de todos los propietarios
[2] Dar de alta un nuevo propietario
[3] Modificar un propietario ya registrado
[4] Eliminar un propietario del sistema
[5] Volver
> """))
            except ValueError:
                self.mostrarErrorStrEnInt()
        return opcion
    
    def crearPropietario(self):
        nombre = self.inputStringNoVacia("Ingrese el nombre: ")
        apellido = self.inputStringNoVacia("Ingrese el apellido: ")
        fechaNac = self.inputStringNoVacia("Ingrese la fecha de nacimiento formato DD/MM/AAAA: ")
        correo = self.inputStringNoVacia("Ingrese el correo: ")
        return nombre, apellido, fechaNac, correo
    
    def modificarPropietario(self, nombre, apellido):
        print(f"Modificando propietario/a: {nombre} {apellido}")
        nombre = self.inputStringNoVacia("Ingrese el nuevo nombre: ")
        apellido = self.inputStringNoVacia("Ingrese el nuevo apellido: ")
        fechaNac = self.inputStringNoVacia("Ingrese la nueva fecha de nacimiento formato DD/MM/AAAA: ")
        correo = self.inputStringNoVacia("Ingrese el nuevo correo: ")
        return nombre, apellido, fechaNac, correo