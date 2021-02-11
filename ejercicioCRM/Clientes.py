import Oportunidades
import main

lista_clientes = []


def nuevoClientes(nombre, apellidos):
    lista_clientes = [nombre, apellidos]
    for clientes in lista_clientes:
        print(lista_clientes)


def MenuClientes():
    while True:
        print('1/ nuevo cliente: ')
        print('2/ Oportunidades: ')
        print('3/ eliminar Cliente: ')
        print('4/ Salir')
        opcion = input('selecciona una opcion: ')
        if opcion == '1':
            nombre = input("nombre del cliente: ")
            apellido = input("apellido: ")
            nuevoClientes(nombre, apellido)

        elif opcion == '2':
            for cliente in lista_clientes:
                print(cliente)
            client = input("elige cliente: ")
            for oportuno in Oportunidades.Oportunidades.lista_Oportunidad:
                print(oportuno)
            opor = input("elige la oportunidad: ")
            ClioOpo = {client: opor}
            print(ClioOpo[client])
        elif opcion == '3':
            for cliente in lista_clientes:
                print(cliente)
                client = input("elige cliente: ")
                lista_clientes.remove(client)
        else:
            main.Menu()
