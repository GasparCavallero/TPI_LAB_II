from Vistas.VistaGeneral import VistaGeneral

class VistaConsulta(VistaGeneral):
    def menu(self):
        opcion: int = 0
        while opcion not in range(1, 6):
            try:
                opcion = int(input("""🖋️ Menú de consultas 🖋️
[1] Ver el listado de todas las consultas en el sistema
[2] Modificar una consulta
[3] Crear una nueva consulta BLOQUEADO PORQUE NECESITO CORROBORAR CON CONTROLADOR DE VETERINARIO SI EXISTE ESE CODIGO
[4] Eliminar una consulta
[5] Volver
> """))
            except ValueError:
                self.mostrarErrorStrEnInt()
        return opcion
    
    def modificarConsulta(self, consulta):
        print(f"Modificando consulta: {consulta}")
        veterinario = self.pedirCodigo("Ingrese el código del veterinario/a: ")
        descripcion = self.inputStringNoVacia("Ingrese la descripción de la consulta: ")
        return veterinario, descripcion