def menu():
    op = -1
    while opcion != 0:
        try:
            print("Seleccione una opción")
            print("""[1] \n[2] \n[0] Salir.""")
            opcion = int(input(": "))
            match opcion:
                case 1:
                    pass
                case 2:
                    pass
                case 0:
                    break
                case _:
                    print("Opción inválida.")
        except ValueError:
            print("Ingrese un número entero.")


def main():
    menu()


if __name__ == "__main__":
    main()
