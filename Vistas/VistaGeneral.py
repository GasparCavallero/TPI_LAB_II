import tkinter as tk

class VistaGeneral(): #tk.Frame    
    def menu(self):
        opcion: int = 0
        while opcion not in range(1, 10):
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
[9] Salir del sistema 👋
> """))
            except ValueError:
                self.mostrarErrorStrEnInt()
        return opcion
    
    def pedirCodigo(self, mensaje):
        codigo = self.inputIntNoVacioNoNegativo(mensaje)
        return codigo

    def mostrarLista(self, lista):
        [print(c) for c in lista]

    def mostrarErrorStrEnInt(self):
        print("Solo permitidos valores numéricos. Intente nuevamente.")

    def inputStringNoVacia(self, mensaje):
        valor = ""
        while valor == "":
            valor = input(mensaje)
            if valor == "":
                print("El campo no puede estar vacío.")
        return valor

    def mostrarObjetoEliminadoExitosamente(self, objeto):
        print(f"{objeto} eliminado/a exitosamente.")

    def mostrarObjetoAnuladoExitosamente(self, objeto):
        print(f"{objeto} anulada/o exitosamente.")

    def codigoInvalido(self):
        print("Código inválido. Vuelva a intentar.")

    def inputIntNoVacioNoNegativo(self, mensaje):
        valor = 0
        while valor == 0:
            try:
                valor = int(input(mensaje))
            except ValueError:
                self.mostrarErrorStrEnInt()
        return valor
    
    def mostrarCreacionExitosa(self):
        print("Creación exitosa.")

    def mostrarCambioExitoso(self):
        print("Cambio efectuado exitosamente.")