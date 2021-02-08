import Clientes
import Oportunidades
import Actividades
import Informes
import Etapas

clientes = Clientes.Clientes
oportunidad = Oportunidades.Oportunidades
actividad = Actividades.Actividades
informe = Informes.Informes
listaCliOpo = []
print('1/ Clientes: ')
print('2/ Oportunidades: ')
print('3/ Actividades: ')
print('4/ Informes: ')
print('5/ Salir')

opcion = input('selecciona una opcion: ')
while True:
    if opcion == '1':
        while True:
            print('1/ nuevo cliente: ')
            print('2/ Oportunidades: ')
            print('3/ Actividades: ')
            print('4/ Salir')
            opcion = input('selecciona una opcion: ')
            if opcion == '1':
                nombre = input("nombre del cliente: ")
                apellido = input("apellido: ")
                clientes.nuevoClientes(nombre, apellido)

            elif opcion == '2':
                for cliente in clientes.lista_clientes:
                    print(cliente)
                client =input("elige cliente: ")
                for oportuno in oportunidad.lista_Oportunidad:
                    print(oportuno)
                opor = input("elige la oportunidad: ")
                listaCliOpo[client,opor]
                print(listaCliOpo)
    elif opcion == '2':
        print('1/ nueva oprtunidad: ')
        print('2/ Oportunidades: ')
        print('3/ Salir')
        elige = input('selection una opcion: ')

        while True:
            if elige == '1':
                nombre = input('nombre de la oportunidad: ')
                oportunidad.nuevaOportunidad(nombre)
                break
            elif elige == '2':
                for oportuno in oportunidad.lista_Oportunidad:
                    print(oportuno)

            elif elige == '3':
                exit()

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
            etapa = Etapas.Etapas.nuevo
            actividad.nuevaActividad(nombreActividad, fecha, descripcion, etapa)
            print(actividad.lista_actividad)

    elif opcion == '4':
        def MenuInformes(self):
            print('1/ clientes: ')
            print('2/ oportunidades: ')
            print('3/ Actividades: ')
            print('4/ Salir')
            opcion = input('selecciona una opcion: ')
    elif opcion == '5':
        exit()
