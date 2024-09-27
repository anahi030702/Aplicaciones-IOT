import json

from alumno import Alumno
from arreglo import Arreglo


class Grupo(Arreglo):
    def __init__(self, seccion=None, grado=None):
        if all(arg is None for arg in (seccion, grado)):
            super().__init__()
            self._is_array = True #para uso interno/privado de la clase
        else:
            self._is_array = False
            self.seccion = seccion
            self.grado = grado
            self.alumnos = Alumno()

    def __str__(self):
        if self._is_array:
            return super().__str__()
        else:
            return  f"{self.grado} {self.seccion}"

    #funcion que agrega un alumno a un grupo
    def agregar_alumnos(self, alumno):
        self.alumnos.agregar(alumno)

    def getDict(self):
        if self._is_array:
            return [arreglo.getDict() for arreglo in self.arreglos]
        else:
            data = {"grado": self.grado, "seccion": self.seccion, "alumnos": self.alumnos.getDict() }
            return data



if __name__ == "__main__":
    #Creando alumnos
    alumno1 = Alumno("Anahi", "Alvarez", "Holguin", "AAHA020703MCLLLNA", "21170158")
    alumno2 = Alumno("Benito", "Rubio", "Franco", "BRFB050930MCLLLN04", "21170160")

    # #Creando grupos y agregando alumnos a los grupos
    grupo2 = Grupo("B", "2do")
    grupo2.agregar_alumnos(alumno1)
    grupo1 = Grupo("A", "7mo")
    grupo1.agregar_alumnos(alumno2)
    grupo1.agregar_alumnos(alumno1)

    print(grupo1.getDict())

    #creando el arreglo de grupos y agregandole grupos
    grupos = Grupo()
    grupos.agregar(grupo1)
    grupos.agregar(grupo2)
    print(grupos.document("grupos", grupos.getDict()))
    # print(grupos.getDict())

    #Mostrando los grupos con sus alumnos
    # print(grupo1.grado + " " + grupo1.seccion)
    # for alumno in grupo1.alumnos:
    #     print(alumno)
    #
    # print(grupo2.grado + " " + grupo2.seccion)
    # for alumno in grupo2.alumnos:
    #     print(alumno)
