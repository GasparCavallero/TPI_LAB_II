import tkinter

def crear_usuario():
    # Lógica para crear un usuario
    print("Usuario creado")

def mostrar_usuario():
    # Lógica para mostrar información del usuario
    ...


def vista():
    ventana_principal = tkinter.Tk()
    ventana_principal.title("Mi Ventana Principal")
    ventana_principal.geometry("400x400")
    
    nombre_tex = tkinter.Label(ventana_principal, text="Ingrese nombre del dueño: ")
    nombre_tex.pack()
    nombre = tkinter.Entry(ventana_principal)
    nombre.pack()
    
    apellido_tex = tkinter.Label(ventana_principal, text="Ingrese apellido del dueño: ")
    apellido_tex.pack()
    apellido = tkinter.Entry(ventana_principal)
    apellido.pack()
    
    dni_tex = tkinter.Label(ventana_principal, text="Ingrese DNI del dueño:")
    dni_tex.pack()
    dni = tkinter.Entry(ventana_principal)
    dni.pack()

    tipo_tex = tkinter.Label(ventana_principal, text="Ingrese tipo de animal internado:")
    tipo_tex.pack()
    tipo = tkinter.Entry(ventana_principal)
    tipo.pack()
    
    raza_tex = tkinter.Label(ventana_principal, text="Ingrese raza del animal internado:")
    raza_tex.pack()
    raza = tkinter.Entry(ventana_principal)
    raza.pack()

    boton_crear = tkinter.Button(ventana_principal, text="Crear Usuario", command=crear_usuario)
    boton_crear.pack()

    boton_mostrar = tkinter.Button(ventana_principal, text="Mostrar Usuario", command=mostrar_usuario)
    boton_mostrar.pack()

    ventana_principal.mainloop()