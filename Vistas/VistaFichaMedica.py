class VistaFichaMedica:
    def menu(self):
        opcion = "0"
        while opcion != "9":
            opcion = input("""📄 Menú de fichas médicas 📄
[1] Listado de todas las fichas médicas en el sistema
[2] Modificar una ficha médica
[3] Dar de baja una ficha médica
[9] Volver
> """)
        return opcion