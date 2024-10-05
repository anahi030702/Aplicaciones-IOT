from alumno import Alumno
import json
from arreglo import Arreglo


class interfaz_alumnos():
    def __init__(self):
        self.alumnos = Alumno()
        self.alumnos.leer_doc()

    def menu_inicial(self):
        print("1. Ver lista de alumnos")
        print("2. Crear alumno")
        print("3. Editar alumno")
        print("4. Borrar alumno")
        print("5. Salir")
        res = input("Escribe el numero de la opcion que deseas: ")

        if res == "2":
            self.crear_alumno()
        elif res == "1":
            self.ver_lista()
        elif res == "4":
            self.eliminar_alumno()
        elif res == "3":
            self.editar_alumno()
        elif res == "5":
            print("¡Hasta luego!")
        else:
            print("Opcion invalida. Eliga una opcion valida en el menú\n")
            self.menu_inicial()

    def crear_alumno(self):
        nombre = input("Escribe el nombre del alumno: ")
        apellido_paterno = input("Escribe el apellido paterno del alumno: ")
        apellido_materno = input("Escribe el apellido materno del alumno: ")
        curp = input("Escribe la CURP del alumno: ")
        matricula = input("Escribe la matricula del alumno: ")

        print(nombre)
        print(apellido_paterno)
        print(apellido_materno)
        print(curp)
        print(matricula)
        res = input("¿Desea finalizar el registro del alumno? Escriba el numero que desea \n 1.Si \n 2.No \n ")

        if res == "1":
            alumno = Alumno(nombre, apellido_paterno, apellido_materno, curp, matricula)
            self.alumnos.agregar(alumno)
            self.alumnos.document("alumnos", self.alumnos.getDict())
            print(alumno)
            print("¡Alumno creado exitosamente!")
            self.opciones_finalizar("Crear")
        else:
            self.opciones_finalizar("Crear")


    def opciones_finalizar(self, accion):
        res = input("Eliga la opcion deseada: \n1." + accion + " otro alumno \n2.Regresar al menu inicial \n")
        if res == "2":
            self.menu_inicial()
        elif res == "1":
            if accion == "Crear":
                self.crear_alumno()
            elif accion == "Modificar":
                self.crear_alumno()
            else:
                self.crear_alumno()
        else:
            print("Opcion invalida")
            self.opciones_finalizar(accion)

    def ver_lista(self):
        if not self.alumnos:
            print("Lista de alumnos vacia")
            self.exit()
        else:
            print("Lista de alumnos")
            for alumno in self.alumnos:
                print(alumno)
            self.exit()

    def exit(self):
        res = input("\nDesea regresar al menu principal? \n1.Si \n2.No\n")
        if res == "1":
            self.menu_inicial()
        elif res == "2":
            print("¡Hasta luego!")
        else:
            print("Opcion invalida")
            self.exit()

    def eliminar_alumno(self):
        for indice, alumno in enumerate(self.alumnos):
            print(indice, alumno)
        num = input("Escribe el numero del registro que desea eliminar: ")
        del self.alumnos[int(num)]
        self.alumnos.document("alumnos", self.alumnos.getDict())
        print("Alumno eliminado exitosamente!")
        self.opciones_finalizar("Eliminar")

    def editar_alumno(self):
        for indice, alumno in enumerate(self.alumnos):
            print(indice, alumno)
        num = input("Escribe el numero del registro que deseas modificar: ")
        self.modificar_valor(num)



    def modificar_valor(self, num):
        dic = self.alumnos[int(num)].getDict()
        print(json.dumps(dic, indent=4))
        clave = input(
            "De los nombres de clave mostrados arriba, escriba el que desea modificar (por ejemplo: nombre): ")
        new_valor = input("Escriba el nuevo valor para " + clave + ": ")
        dic[clave] = new_valor
        self.alumnos[int(num)] = Alumno(dic["nombre"], dic["ap_paterno"], dic["ap_materno"], dic["curp"], dic["matricula"])
        self.alumnos.document("alumnos", self.alumnos.getDict())
        print(self.alumnos)
        print("Valor modificada exitosamente!")
        res = input("¿Deseas modificar otro valor del mismo registro? \n1.Si \n2.No\n")
        if res == "1":
            self.modificar_valor(num)
        elif res == "2":
            self.opciones_finalizar("Modificar")
        else:
            print("Opcion invalida")






if __name__ == "__main__":
    interfaz_alumnos().menu_inicial()
