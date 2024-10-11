from carrera import Carrera
from interfaz_grupos import interfaz_grupos
import json


class InterfazCarreras:
    def __init__(self):
        self.carreras = Carrera()
        self.carreras.leer_doc()

    def menu_inicial(self):
        print("1. Ver lista de carreras")
        print("2. Crear carrera")
        print("3. Editar carrera")
        print("4. Borrar carrera")
        print("5. Salir")
        res = input("Escribe el numero de la opcion que deseas: ")

        if res == "1":
            self.ver_lista()
        elif res == "2":
            self.crear_carrera()
        elif res == "4":
            self.eliminar_carrera()
        elif res == "3":
            self.editar_carrera()


    def ver_lista(self):
        if not self.carreras:
            print("Lista de carreras vacia")
            self.exit()
        else:
            print("Lista de carreras")
            for carrera in self.carreras:
                print(carrera)

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

    def crear_carrera(self):
        nombre = input("Escribe el nombre de la carrera: ")
        clave = input("Escribe la clave de la carrera: ")
        print(nombre, clave)
        res = input("¿Desea finalizar el registro de la carrera? Escriba el numero que desea \n 1.Si \n 2.No \n ")

        if res == "1":
            carrera = Carrera(nombre, clave)
            print(carrera)
            print("¡Carrera creada exitosamente!")
            res2 = input("¿Deseas agregar grupos a la carrera creada? \n1.Si \n2.No")
            if res2 == "1":
                ig= interfaz_grupos(carrera.grupos)
                ig.menu_inicial()
                carrera.grupos =ig.grupos

                self.carreras.agregar(carrera)
                self.carreras.document("carreras", self.carreras.getDict())

            elif res2 == "2":
                self.opciones_finalizar("Crear")
                self.carreras.agregar(carrera)
                self.carreras.document("carreras", self.carreras.getDict())
            else:
                print("Opcion invalida")
        else:
            self.opciones_finalizar("Crear")


    def eliminar_carrera(self):
        for indice, carrera in enumerate(self.carreras):
            print(indice, carrera)
        num = input("Escribe el numero del registro que desea eliminar: ")
        del self.carreras[int(num)]
        self.carreras.document("carreras", self.carreras.getDict())
        print("Carrera eliminado exitosamente!")
        self.opciones_finalizar("Eliminar")

    def editar_carrera(self):
        for indice, carrera in enumerate(self.carreras):
            print(indice, carrera)
        num = input("Escribe el numero del registro que deseas modificar: ")
        self.modificar_valor(num)


    def modificar_valor(self, num):
        dic = self.carreras[int(num)].getDict()
        print(json.dumps(dic, indent=4))
        clave = input(
            "De los nombres de clave mostrados arriba, escriba el que desea modificar (por ejemplo: nombre): ")
        if clave == "grupos":
            ig = interfaz_grupos(self.carreras[int(num)].grupos)
            ig.menu_inicial()
            self.carreras[int(num)].grupos = ig.grupos
            print(self.carreras[int(num)])
        else:
            new_valor = input("Escriba el nuevo valor para " + clave + ": ")
            dic[clave] = new_valor
            self.carreras[int(num)] = Carrera(dic["nombre"], dic["clave"])
            print(self.carreras)
            print("Valor modificada exitosamente!")
        self.carreras.document("carreras", self.carreras.getDict())
        res = input("¿Deseas modificar otro valor del mismo registro? \n1.Si \n2.No\n")
        if res == "1":
            self.modificar_valor(num)
        elif res == "2":
            self.opciones_finalizar("Modificar")
        else:
            print("Opcion invalida")


    def opciones_finalizar(self, accion):
        res = input("Eliga la opcion deseada: \n1." + accion + " otra carrera \n2.Regresar al menu inicial \n")
        if res == "2":
            self.menu_inicial()
        elif res == "1":
            if accion == "Crear":
                self.crear_carrera()
            elif accion == "Modificar":
                self.crear_carrera()
            elif accion == "Eliminar":
                self.crear_carrera()
            else:
                self.crear_carrera()
        else:
            print("Opcion invalida")
            self.opciones_finalizar(accion)





if __name__ == "__main__":
    InterfazCarreras().menu_inicial()