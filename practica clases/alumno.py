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
    print(alumnos.document("alumnos"))


    #
    # x = { 'name' : 'anahi'}
    # print(json.dumps(x))






