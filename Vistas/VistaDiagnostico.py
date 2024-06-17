class VistaDiagnostico:
    def menuDiagnostico(self):
        print('''[1]-Dar De Alta Nuevo Diagnostico
[2]-Modificar Diagnostico
[3]-Eliminar Diagnostico Del Sistema
[0]-Volver Al Menu Principal''')
        op = input("Ingrese la opcion que desea: ")
        return op