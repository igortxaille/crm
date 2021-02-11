import matplotlib.pyplot as plt
import numpy as np
import Actividades
import Clientes

cliente = Clientes


def informeCliente(actividad):
    cliente = Clientes.lista_clientes
    actividades = Actividades.lista_actividad
    y_pos = np.arange(len(actividad))
    plt.bar(plt.bar(y_pos, cliente, color=(0.2, 0.7, 0.7, 1)))
    plt.title('Mis datos')
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    plt.ylim(0, 60)
    plt.xticks(y_pos, cliente)
    plt.savefig('barras.jpg')
    plt.show()
def MenuInformes():
    def MenuInformes(self):
        print('1/ clientes: ')
        print('2/ oportunidades: ')
        print('3/ Actividades: ')
        print('4/ Salir')
        opcion = input('selecciona una opcion: ')