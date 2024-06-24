from Vistas.VistaGeneral import VistaGeneral

class VistaDiagnostico(VistaGeneral):
    def menu(self):
        opcion: int = 0
        while opcion not in range(1, 6):
            try:
                opcion = int(input("""📝 Menú de diagnósticos 📝
[1] Ver el listado de todos los diagnósticos en el sistema
[2] Modificar un diagnóstico
[3] Crear un nuevo diagnóstico # FALTA, DEPENDE DE UNA FUNCION DE MASCOTA
[4] Eliminar un diagnóstico del sistema
[5] Volver
> """))
            except ValueError:
                self.mostrarErrorStrEnInt()
        return opcion
    
    def modificarDiagnostico(self, diagnostico):
        print(f"Modificando diagóstico: {diagnostico}")
        descripcion = self.inputStringNoVacia("Ingrese la nueva descripción: ")
        return descripcion