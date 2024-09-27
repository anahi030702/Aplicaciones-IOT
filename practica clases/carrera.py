import json

from alumno import Alumno
from arreglo import Arreglo
from grupo import Grupo

class Carrera(Arreglo):
    def __init__(self, nombre=None, clave=None):
        if all(arg is None for arg in (nombre, clave)):
            super().__init__()
            self._is_array = True
        else:
            self._is_array = False
            self.nombre = nombre
            self.clave = clave
            self.grupos = Grupo()

    def __str__(self):
        if self._is_array:
            return super().__str__()
        else:
            data = f"{self.nombre} {self.clave}"
            return json.dumps(data)

    #Funcion que agrega un grupo a una carrera
    def agregar_grupo(self, grupo):
        self.grupos.agregar(grupo)

    def getDict(self):
        if self._is_array:
            return [arreglo.getDict() for arreglo in self.arreglos]
        else:
            data = {"nombre": self.nombre, "clave": self.clave, "grupos": self.grupos.getDict() }
            return data



if __name__ == '__main__':
    #Creando alumnos
    alumno1 = Alumno("Anahi", "Alvarez", "Holguin", "AAHA020703MCLLLNA", "21170158")
    alumno2 = Alumno("Benito", "Rubio", "Franco", "BRFB050930MCLLLN04", "21170160")
    #
    #Creando grupos y agregandoles alumnos
    grupo1 = Grupo("A", "7mo")
    grupo1.agregar_alumnos(alumno1)
    grupo1.agregar_alumnos(alumno2)

    grupo2 = Grupo("B", "2do")
    grupo2.agregar_alumnos(alumno1)
    grupo2.agregar_alumnos(alumno2)

    #Creando carreras y agregandole grupos con alumnos
    carrera1 = Carrera("Tecnologias de la informacion", "TICS")
    carrera1.agregar_grupo(grupo1)

    carrera2 = Carrera("Mecatronica", "MC")
    carrera2.agregar_grupo(grupo2)

    #Mostrando las carreras con los grupos que tiene y cada grupo con los alumnos que tiene
    for grupo in carrera1.grupos:
        print(carrera1.nombre)
        print(grupo.grado + " " + grupo.seccion)
        for alumno in grupo.alumnos:
            print(alumno)


    for grupo in carrera2.grupos:
        print(carrera2.nombre)
        print(grupo.grado + " " + grupo.seccion)
        for alumno in grupo.alumnos:
            print(alumno)

    #creando arreglo de carreras y agregandole carreras
    carreras = Carrera()
    carreras.agregar(carrera1)
    carreras.agregar(carrera2)
    print(carreras.document("carreras", carreras.getDict()))