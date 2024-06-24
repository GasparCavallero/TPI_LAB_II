class VistaDiagnostico:
    def menu(self):
        opcion = "0"
        while opcion != "9":
            opcion = input("""📝 Menú de diagnósticos 📝
[1] Ver un listado de todos los diagnósticos en el sistema
[2] Modificar un diagnóstico
[3] Crear un nuevo diagnóstico
[4] Dar de baja un diagnóstico
[9] Volver
> """)