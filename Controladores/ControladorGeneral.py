from Vistas.VistaGeneral import VistaGeneral
from .ControladorRaza import ControladorRaza
from .ControladorVacuna import ControladorVacuna
from .ControladorMascota import ControladorMascota
from .ControladorPropietario import ControladorPropietario
from .ControladorVeterinario import ControladorVeterinario
from .ControladorFichaMedica import ControladorFichaMedica
from .ControladorConsulta import ControladorConsulta
from .ControladorDiagnostico import ControladorDiagnostico
from .ControladorTratamiento import ControladorTratamiento

class ControladorGeneral():
    def __init__(self):
        self.__vista = VistaGeneral()
        self.cp = ControladorPropietario()
        self.cfm = ControladorFichaMedica()
        self.cvt = ControladorVeterinario()
        self.cr = ControladorRaza()
        self.cm = ControladorMascota(self.cp, self.cfm)
        self.cvc = ControladorVacuna()
        self.ct = ControladorTratamiento()
        self.cd = ControladorDiagnostico()
        self.cc = ControladorConsulta()
        self.menu()

    def guardar(self):
        self.cp.guardar_propietarios()
        self.cfm.guardar_fichasmedicas()
        self.cvt.guardar_veterinarios()
        self.cr.guardar_razas()
        self.cm.guardar_mascotas()
        self.cvc.guardar_vacunas()
        self.ct.guardar_tratamientos()
        self.cd.guardar_diagnosticos()
        self.cc.guardar_consultas() # Todos los métodos de guardar de los controladores

    def menu(self):
        opcion = 0
        while opcion != 10:
            opcion = self.__vista.menu()
            match opcion:
                case 1:
                    self.__vista.limpiarPantalla()
                    self.cr.menu() # Razas
                    self.__vista.limpiarPantalla()
                case 2:
                    self.__vista.limpiarPantalla()
                    self.cm.menu() # Mascotas
                    self.__vista.limpiarPantalla()
                case 3:
                    self.__vista.limpiarPantalla()
                    self.cvt.menu() # Personal veterinario
                    self.__vista.limpiarPantalla()
                case 4:
                    self.__vista.limpiarPantalla()
                    self.cp.menu() # Clientes
                    self.__vista.limpiarPantalla()
                case 5:
                    self.__vista.limpiarPantalla()
                    self.cfm.menu() # Fichas Médicas
                    self.__vista.limpiarPantalla()
                case 6:
                    self.__vista.limpiarPantalla()
                    self.cvc.menu() # Vacunas
                    self.__vista.limpiarPantalla()
                case 7:
                    self.__vista.limpiarPantalla()
                    self.cd.menu() # Diagnósticos
                    self.__vista.limpiarPantalla()
                case 8:
                    self.__vista.limpiarPantalla()
                    self.ct.menu() # Tratamientos
                    self.__vista.limpiarPantalla()
                case 9:
                    self.__vista.limpiarPantalla()
                    self.cc.menu() # Consultas
                    self.__vista.limpiarPantalla()
                case 10:
                    self.__vista.limpiarPantalla()
                    self.guardar()
                    self.__vista.mostrarAdios() # Salir del sistema