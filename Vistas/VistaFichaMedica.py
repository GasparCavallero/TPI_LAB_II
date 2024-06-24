from Vistas.VistaGeneral import VistaGeneral

class VistaFichaMedica(VistaGeneral):
    def menu(self):
        opcion: int = 0
        while opcion not in range(1, 6):
            try:
                opcion = int(input("""📄 Menú de fichas médicas 📄
[1] Ver el listado de todas las fichas médicas en el sistema
[2] Ver una ficha médica específica # FALTA
[3] Agregar una vacuna a una mascota # FALTA
[4] Anular una ficha médica
[5] Volver
> """))
            except ValueError:
                self.mostrarErrorStrEnInt()
        return opcion

