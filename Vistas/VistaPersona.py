class VistaPersona:
    def solicitar_nombre(self):
        return input("Ingrese su nombre: ")
    
    def solicitar_apellido(self):
        return input("Ingrese su apellido: ")
    
    def solicitar_fecha(self):
        return input("Ingrese su fecha de nacimiento: ")
    
    def solicitar_correo(self):
        return input("Ingrese un correo electrónico: ")
    
    def mostrar_informacion(self, data):
        return print(data)