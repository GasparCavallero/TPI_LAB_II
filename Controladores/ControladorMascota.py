from Models.Mascota import Mascota
from Vistas.VistaMascota import VistaMascota


class Controlador_Mascota:
    def __init__(self):
        self._vista = VistaMascota()
        self._modelo = Mascota()
        self.listaMascotas = []

    def cargarMascota(self):
        with open("Archivos\\mascota.txt", "r") as file:
            linea = file.readlines()
        for l in linea:
            Propietario, Raza, FichaMedica, nombre, fechaNac, tipoAnimal, codigo = (
                l.strip().split(",")
            )
            self.listaMascotas.append(
                Mascota(
                    Propietario, Raza, FichaMedica, nombre, fechaNac, tipoAnimal, codigo
                )
            )
        return self.listaMascotas

    def buscarMascota(self, mascota):
        for i in self.listaMascotas:
            if i.codigo == mascota:
                return i

    def agregarMascota(self):
        Propietario = self._vista.getPropietario()
        Raza = self._vista.getRaza()
        FichaMedica = self._vista.getFichaMedica()
        nombre = self._vista.getNombre()
        fechaNac = self._vista.getFechaNac()
        tipoAnimal = self._vista.getTipoAnimal()
        codigo = self._vista.getCodigo()
        self.listaMascotas.append(
            Mascota(
                Propietario, Raza, FichaMedica, nombre, fechaNac, tipoAnimal, codigo
            )
        )
        with open("Archivos\\mascotas.txt", "a") as f:
            f.write(
                f"\n{Propietario},{Raza},{FichaMedica},{nombre},{fechaNac},{tipoAnimal}, {codigo}"
            )

    def anularMascota(self, mascota):
        for i in self.listaMascotas:
            if i.codigo == mascota:
                i.estado = False

    def verMascota(self, mascota):
        for i in self.listaMascotas:
            if i.codigo == mascota:
                self._vista.mostrarMascota(i)

    def verTodasLasMascotas(self):
        for i in self.listaMascotas:
            self._vista.mostrarMascota(i)

    def verMascotasHabilitadas(self):
        for i in self.listaMascotas:
            if i.estado == True:
                self._vista.mostrarMascota(i)
