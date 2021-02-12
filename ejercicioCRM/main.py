import Actividades
from Clientes import Clientes
import Informes
import Oportunidades
cliente = Clientes
oportunidad = Oportunidades
actividad = Actividades
informe = Informes
lista_clientes = []
lista_Oportunidad = []
lista_actividad = []
lista_Etapas = ["nuevo","calificado","propuesta", "ganadas"]


def Menu():
    print('1/ Clientes: ')
    print('2/ Oportunidades: ')
    print('3/ Actividades: ')
    print('4/ Informes: ')
    print('5/ Salir')
    if len(lista_clientes) >0:
        print(lista_clientes[0].nombre)
    opcion = input('selecciona una opcion: ')

    while True:
        if opcion == '1':

            while True:
                print('1/ nuevo cliente: ')
                print('2/ Oportunidades: ')
                print('3/ eliminar Cliente: ')
                print('4/ Salir')
                opcion = input('selecciona una opcion: ')
                if opcion == '1':
                    nombre = input("nombre del cliente: ")
                    movil = input("movil: ")
                    client = Clientes(nombre, movil)
                    lista_clientes.append(client)

                elif opcion == '2':
                    for cliente in lista_clientes:
                        print(cliente)

                    client = input("elige cliente: ")
                    for oportuno in lista_Oportunidad:
                        print(oportuno)
                    opor = input("elige la oportunidad: ")


                elif opcion == '3':
                    for cliente in lista_clientes:
                        print(cliente)
                        client = input("elige cliente: ")
                        lista_clientes.remove(client)
                elif opcion == '4':
                    Menu()
        elif opcion == '2':
            print('1/ nueva oportunidad: ')
            print('2/ eliminar oportunidad : ')
            print('3/ Salir')
            elige = input('selection una opcion: ')

            while True:
                if elige == '1':
                    nombre = input('nombre de la oportunidad: ')
                    ingreso = input('añade cantidad: ')


                elif elige == '2':
                    for oportuno in lista_Oportunidad:
                        opor = input("elige oportunidad: ")
                        lista_Oportunidad.remove(opor)

                elif elige == '3':
                    Menu()
        elif opcion == '3':
            print('1/ nueva actividad: ')
            print('2/ etapas: ')
            print('3/ Actividades: ')
            print('4/ Salir')

            elige = input('selecciona una opcion: ')
            if elige == '1':
                nombreActividad = input('nombre de la acciòn: ')
                fecha = input('fecha de vencimiento: ')
                descripcion = input('describe la actividad: ')

                print(lista_actividad)
            elif elige == '2':
                for activo in lista_actividad:
                    activ = input("elige actividad: ")

                    print(lista_actividad)
            elif elige == '3':
                Menu()

        elif opcion == '4':
            informe.MenuInformes()
        elif opcion == '5':
            exit()


Menu()
