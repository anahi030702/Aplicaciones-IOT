from arreglo import Arreglo
import json

class Alumno(Arreglo):
    def __init__(self, nombre=None, ap_paterno=None, ap_materno=None, curp=None, matricula=None):
        # Si no se pasan propiedades, actúa como lista
        if all(arg is None for arg in [nombre, ap_paterno, ap_materno, curp, matricula]):
            self._is_array = True
            super().__init__()
        else:
            # Si no actua como objeto
            self._is_array = False
            self.nombre = nombre
            self.ap_paterno = ap_paterno
            self.ap_materno = ap_materno
            self.curp = curp
            self.matricula = matricula

    def getDict(self):
        if self._is_array:
            return [ arreglo.getDict() for arreglo in self.arreglos ]
        else:
            data = {"nombre": self.nombre, "ap_paterno": self.ap_paterno, "ap_materno": self.ap_materno,
                    "curp": self.curp, "matricula": self.matricula }
            return data


    def __str__(self):
        if self._is_array:
            return super().__str__()
        #si no retorna los datos del objeto que se creo
        else:
            return f"{self.nombre} {self.ap_paterno} {self.ap_materno} {self.matricula} {self.curp}"


    def leer_doc(self):
        with open('alumnos.json', 'r') as json_File:
            data = json.load(json_File)

        alumnos = self.iterar_archivo(data)
        return alumnos


    def iterar_archivo(self, data):
        alumnos = []

        for doc in data:
            alumno = Alumno(doc["nombre"], doc["ap_paterno"], doc["ap_materno"], doc["curp"], doc["matricula"])
            alumnos.append(alumno)
        self.arreglos = alumnos
        return alumnos







if __name__ == "__main__":
    # #Creando alumnos
    alumno1 = Alumno("Anahi", "Alvarez", "Holguin", "AAHA020703MCLLLNA", "21170158")
    alumno2 = Alumno("Benito", "Rubio", "Franco", "BRFB050930MCLLLN04", "21170160")

    #creando arreglo de alumnos
    alumnos = Alumno()
    alumnos.agregar(alumno1)
    alumnos.agregar(alumno2)
    alumnos.agregar(alumno1)
    alumnos.agregar(alumno2)

    #creando documento de alumnos con arreglo alumnos
    alumnos.document("alumnos", alumnos.getDict())

    #extrayendo la informacion del archivo alumno y convirtiendolo a objetos ALUMNO
    alumnos_creados = alumnos.leer_doc()

    #mostrando los objetos alumno creados despues de extraer la informacion del documento
    for alumno in alumnos_creados:
        print(alumno)






