import json
from textwrap import indent

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

    def leer_doc(self):
        with open('grupos.json', 'r') as json_File:
            data = json.load(json_File)

        self.iterar_archivo(data)

    def iterar_archivo(self, data):
        grupos = []
        alumnos=Alumno()
        for doc in data:
            grupo = Grupo(doc["seccion"], doc["grado"])
            alumnos.iterar_archivo(doc["alumnos"])
            grupo.alumnos=alumnos
            grupos.append(grupo)

        self.arreglos = grupos



if __name__ == "__main__":

    grupos = Grupo()
    grupos.leer_doc()

    print(json.dumps(grupos.getDict(), indent=4))



