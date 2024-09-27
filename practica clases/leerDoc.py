import json
from alumno import Alumno
#
# with open('alumnos.json', 'r') as json_File:
#     test = json.load(json_File)
#
# alumnos = Alumno()
#
# for tes in test:
#     values = tes.values()
#     lists = list(values)
#     alumno = Alumno(lists[0], lists[1], lists[2], lists[3], lists[4])
#     alumnos.agregar(alumno)
#
# print(alumnos)

alumnos = Alumno()
alumno1 = Alumno("ANAHI", "ALVAREZ", "HOLGUIN", "AAAAAAAAAA", "21170158")
alumnos.agregar(alumno1)
data = alumnos.getArrayDict()

print(data)





