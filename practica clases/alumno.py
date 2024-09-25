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
        data = {"nombre": f"{self.nombre}", "ap_paterno": f"{self.ap_paterno}", "ap_materno": f"{self.ap_materno}",
                "curp": f"{self.curp}", "matricula": f"{self.matricula}"}
        return data

    def __str__(self):
        if self._is_array:
            return super().__str__()
        #si no retorna los datos del objeto que se creo
        else:
            return f"{self.nombre} {self.ap_paterno} {self.ap_materno} {self.matricula} {self.curp}"


    def leer_doc(self):
        with open('alumnos.json', 'r') as json_File:
            test = json.load(json_File)

        alumnos = self.iterar_archivo(test)
        return alumnos


    def iterar_archivo(self, data):
        alumnos = Alumno()

        for doc in data:
            values = doc.values()
            lists = list(values)
            alumno = Alumno(lists[0], lists[1], lists[2], lists[3], lists[4])
            alumnos.agregar(alumno)

        return alumnos







if __name__ == "__main__":
    # #Creando alumnos
    alumno1 = Alumno("Anahi", "Alvarez", "Holguin", "AAHA020703MCLLLNA", "21170158")
    alumno2 = Alumno("Benito", "Rubio", "Franco", "BRFB050930MCLLLN04", "21170160")
    #
    # print(alumno1)
    alumnos = Alumno()
    alumnos.agregar(alumno1)
    alumnos.agregar(alumno2)
    alumnos.agregar(alumno1)
    alumnos.agregar(alumno2)

    # print(alumnos)
    # alumnos.document("alumnos")
    #
    print(alumnos.leer_doc())


    #
    # x = { 'name' : 'anahi'}
    # print(json.dumps(x))






