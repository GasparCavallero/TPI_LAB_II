### Import de módulos
import os

## Import Tkinter
import tkinter

### Import de vistas
from Vistas.VistaPersona import VistaPersona

### Import de controladores
from Controladores.ControladorPersona import ControladorPersona

### Funciones

def volver(): # Limpia la consola
    opcion = input("Presione [ENTER] para volver al menu...\n")
    if os.name == 'nt': os.system("cls") # Si el sistema es Windows
    else: os.system("clear") # Si es Linux/POSIX
    return opcion


def wrapper(funcion): # Devuelve función + limpieza de consola para evitar copypaste
    return funcion, volver()


def salir():
    return print("Cerrando el programa...")


def menu():
    opcion = int
    while opcion != 0:
        try:
            opcion = int(input(("Seleccione una opción y presione [ENTER]:\n[1] Crear un nuevo usuario\n[2] \n[0] Salir del programa\n> ")))
            match opcion:
                case 1:
                    pass
                case 2:
                    pass
                case 0:
                    pass # No hace falta break 
                case _:
                    print("Opción inválida.")
        except ValueError:
            print("Ingrese un número que esté en el menú.")
        except KeyboardInterrupt:
            break
    return salir()


def main():
    #menu() Menu en consola, comentado para proyecto MVC
    controlador = ControladorPersona(VistaPersona())
    controlador.crear_persona()
    controlador.mostrar_informacion()

if __name__ == "__main__":
    main()
