import os

class VistaGeneral():
    def menu(self):
        opcion: int = 0
        while opcion not in range(1, 11):
            try:
                opcion = int(input("""💊 ¡Bienvenido al sistema de administración de veterinarias de Impulsive! 💊
[1] Gestión de razas 🦍
[2] Gestión de mascotas 🐱
[3] Gestión de personal veterinario 👩
[4] Gestión de propietarios/as 🧑‍🦲
[5] Gestión de fichas médicas 📄
[6] Gestión de vacunas 💉
[7] Gestión de diagnósticos 📝
[8] Gestión de tratamientos 🗂️
[9] Gestión de consultas 🖋️
[10] Salir del programa👋
> """))
            except ValueError:
                self.mostrarErrorStrEnInt()
        return opcion
    
    def limpiarPantalla(self):
        if os.name in ('nt','dos'):
            os.system("cls")
        elif os.name in ('linux','osx','posix'):
            os.system("clear")

    def mostrarAdios(self):
        print("Guardando datos...")
        print("¡Gracias por utilizar el sistema!")

    def mostrarObjeto(self, objeto, mensaje=None):
        if mensaje == None:
            pass
        else:
            print(mensaje)
        print(objeto)
    
    def pedirCodigo(self, mensaje):
        codigo = self.inputIntNoVacioNoNegativo(mensaje)
        return codigo

    def mostrarLista(self, lista):
        [print(c) for c in lista]

    def mostrarMensaje(self, mensaje):
        print(mensaje)

    def mostrarErrorStrEnInt(self):
        self.limpiarPantalla()
        print("Solo permitidos valores numéricos. Intente nuevamente.")

    def inputStringNoVacia(self, mensaje):
        valor = ""
        while valor == "":
            valor = input(mensaje)
            if valor == "":
                self.limpiarPantalla()
                print("El campo no puede estar vacío.")
        return valor

    def mostrarObjetoEliminadoExitosamente(self, objeto):
        print(f"{objeto} eliminado/a exitosamente.")

    def mostrarObjetoAnuladoExitosamente(self, objeto):
        print(f"{objeto} anulada/o exitosamente.")

    def codigoInvalido(self):
        self.limpiarPantalla()
        print("Código inválido. Vuelva a intentar.")

    def inputIntNoVacioNoNegativo(self, mensaje):
        valor = 0
        while valor == 0:
            try:
                valor = int(input(mensaje))
            except ValueError:
                self.limpiarPantalla()
                self.mostrarErrorStrEnInt()
        return valor
        
    
    def mostrarCreacionExitosa(self):
        print("Creación exitosa.")

    def mostrarCambioExitoso(self):
        print("Cambio efectuado exitosamente.")

    def mostrarEnterParaVolver(self):
        input("Presione [ENTER] para volver ")

    def mostrarEliminadoExitosamente(self, objeto):
        print(f"{objeto} eliminado/a exitosamente.")