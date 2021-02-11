import Actividades
import Clientes
import Informes
import Oportunidades

oportunidad = Oportunidades
actividad = Actividades
informe = Informes
listaCliOpo = []


def Menu():
    print('1/ Clientes: ')
    print('2/ Oportunidades: ')
    print('3/ Actividades: ')
    print('4/ Informes: ')
    print('5/ Salir')

Menu()
opcion = input('selecciona una opcion: ')
while True:
    if opcion == '1':
        Clientes.MenuClientes()
    elif opcion == '2':
        oportunidad.MenuOpor()
    elif opcion == '3':
        actividad.MenuActivo()
    elif opcion == '4':
        informe.MenuInformes()
    elif opcion == '5':
        exit()
