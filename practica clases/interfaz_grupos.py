from textwrap import indent

from alumno import Alumno
from grupo import Grupo
import json

from interfaz_alumnos import InterfazAlumno


class interfaz_grupos():
    def __init__(self, data=None):
        if data is None:
            self.externo = False
            self.grupos = Grupo()
            self.grupos.leer_doc()
        else:
            self.externo = True
            self.grupos = data


    def menu_inicial(self):
        print("1. Ver lista de grupos")
        print("2. Crear grupo")
        print("3. Editar grupo")
        print("4. Borrar grupo")
        print("5. Salir")
        res = input("Escribe el numero de la opcion que deseas: ")

        if res == "1":
            self.ver_lista()
        elif res == "2":
            self.crear_grupo()
        elif res == "4":
            self.eliminar_grupo()
        elif res == "3":
            self.editar_grupo()

    def ver_lista(self):
        if not self.grupos:
            print("Lista de grupos vacia")
            self.exit()
        else:
            print("Lista de grupos")
            for grupo in self.grupos:
                print(grupo)

            self.exit()

    def crear_grupo(self):
        grado = input("Escribe el grado del grupo: ")
        seccion = input("Escribe el seccion del grupo: ")
        print(grado, seccion)
        res = input("¿Desea finalizar el registro del grupo? Escriba el numero que desea \n 1.Si \n 2.No \n ")

        if res == "1":
            grupo = Grupo(seccion, grado)
            print(grupo)
            print("¡Grupo creado exitosamente!")
            res2 = input("¿Deseas agregar alumnos al grupo creado? \n1.Si \n2.No")
            if res2 == "1":
                ia=InterfazAlumno(grupo.alumnos)
                ia.menu_inicial()
                grupo.alumnos=ia.alumnos

                self.grupos.agregar(grupo)
                if not self.externo:
                    self.grupos.document("grupos", self.grupos.getDict())
                else:
                    return self.grupos
                # self.grupos.document("grupos", self.grupos.getDict())

            elif res2 == "2":
                self.opciones_finalizar("Crear")
                self.grupos.agregar(grupo)
                if not self.externo:
                    self.grupos.document("grupos", self.grupos.getDict())
                else:
                    return self.grupos
                # self.grupos.document("grupos", self.grupos.getDict())
            else:
                print("Opcion invalida")
        else:
            self.opciones_finalizar("Crear")


    def eliminar_grupo(self):
        for indice, grupo in enumerate(self.grupos):
            print(indice, grupo)
        num = input("Escribe el numero del registro que desea eliminar: ")
        del self.grupos[int(num)]
        # self.grupos.document("grupos", self.grupos.getDict())
        print("Grupo eliminado exitosamente!")
        self.opciones_finalizar("Eliminar")
        if not self.externo:
            self.grupos.document("grupos", self.grupos.getDict())
        else:
            return self.grupos

    def editar_grupo(self):
        for indice, grupo in enumerate(self.grupos):
            print(indice, grupo)
        num = input("Escribe el numero del registro que deseas modificar: ")
        self.modificar_valor(num)

    def modificar_valor(self, num):
        dic = self.grupos[int(num)].getDict()
        print(json.dumps(dic, indent=4))
        clave = input(
            "De los nombres de clave mostrados arriba, escriba el que desea modificar (por ejemplo: nombre): ")
        if clave == "alumnos":
            ia = InterfazAlumno(self.grupos[int(num)].alumnos)
            ia.menu_inicial()
            self.grupos[int(num)].alumnos = ia.alumnos
        else:
            new_valor = input("Escriba el nuevo valor para " + clave + ": ")
            dic[clave] = new_valor
            self.grupos[int(num)] = Grupo(dic["seccion"], dic["grado"])
            print(self.grupos)
            print("Valor modificada exitosamente!")
        # self.grupos.document("grupos", self.grupos.getDict())
        res = input("¿Deseas modificar otro valor del mismo registro? \n1.Si \n2.No\n")
        if res == "1":
            self.modificar_valor(num)
        elif res == "2":
            self.opciones_finalizar("Modificar")
            if not self.externo:
                self.grupos.document("grupos", self.grupos.getDict())
            else:
                return self.grupos
        else:
            print("Opcion invalida")

    def opciones_finalizar(self, accion):
        res = input("Eliga la opcion deseada: \n1." + accion + " otro grupo \n2.Regresar al menu inicial \n")
        if res == "2":
            self.menu_inicial()
        elif res == "1":
            if accion == "Crear":
                self.crear_grupo()
            elif accion == "Modificar":
                self.crear_grupo()
            elif accion == "Eliminar":
                self.eliminar_grupo()
            else:
                self.crear_grupo()
        else:
            print("Opcion invalida")
            self.opciones_finalizar(accion)

    def exit(self):
        res = input("\nDesea regresar al menu principal? \n1.Si \n2.No\n")
        if res == "1":
            self.menu_inicial()
        elif res == "2":
            print("¡Hasta luego!")
        else:
            print("Opcion invalida")
            self.exit()

if __name__ == "__main__":
    interfaz_grupos().menu_inicial()