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
        self.cp = ControladorPropietario()
        self.cfm = ControladorFichaMedica()
        self.cvt = ControladorVeterinario()
        self.cr = ControladorRaza()
        self.cm = ControladorMascota(self.cp, self.cfm)
        self.cvc = ControladorVacuna()
        self.cr = ControladorRaza()
        self.ct = ControladorTratamiento()
        self.cd = ControladorDiagnostico()
        self.cc = ControladorConsulta()
        self.menu()

    def guardar(self):
        ... # Todos los métodos de guardar de los controladores

    def menu(self):
        opcion = None
        while opcion != 9:
            opcion = VistaGeneral.menu()
            match opcion:
                case 1:
                    self.cr.menu() # Razas
                case 2:
                    self.cm.menu() # Mascotas
                case 3:
                    self.cvt.menu() # Personal veterinario
                case 4:
                    self.cp.menu() # Clientes
                case 5:
                    self.cfm.menu() # Fichas Médicas
                case 6:
                    self.cvc.menu() # Vacunas
                case 7:
                    self.cd.menu() # Diagnósticos
                case 8:
                    self.ct.menu() # Tratamientos
                case 9:
                    break # Salir del sistema
                case _:
                    ...