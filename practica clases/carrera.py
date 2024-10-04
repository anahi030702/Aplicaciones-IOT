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

    def leer_doc(self):
        with open('carreras.json', 'r') as json_File:
            data = json.load(json_File)

        carreras = self.iterar_archivo(data)


    def iterar_archivo(self, data):
        carreras = []
        grupos= Grupo()
        for doc in data:
            carrera = Carrera(doc["nombre"], doc["clave"])
            grupos.iterar_archivo(doc["grupos"])
            carrera.grupos=grupos
            carreras.append(carrera)

        self.arreglos = carreras


if __name__ == '__main__':
    carreras = Carrera()

    carreras.leer_doc()
    print(json.dumps(carreras.getDict(), indent=4))
