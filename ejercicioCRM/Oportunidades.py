
import main
lista_Oportunidad = []

def nuevaOportunidad(self, nombre):
    lista_Oportunidad = [nombre]
    for oportunidad in lista_Oportunidad:
        print(oportunidad)


def MenuOpor():
    print('1/ nueva oportunidad: ')
    print('2/ eliminar oportunidad : ')
    print('3/ Salir')
    elige = input('selection una opcion: ')

    while True:
        if elige == '1':
            nombre = input('nombre de la oportunidad: ')
            nuevaOportunidad(nombre)
            break
        elif elige == '2':
            for oportuno in lista_Oportunidad:
                opor = input("elige oportunidad: ")
                lista_Oportunidad.remove(opor)

        elif elige == '3':
            main.Menu()