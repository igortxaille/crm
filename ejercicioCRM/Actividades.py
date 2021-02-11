import Etapas
import main
lista_actividad = []


def __init__(self, nombre, fecha, descripcion, etapa):
    self.nombre = nombre
    self.fecha = fecha
    self.descripcion = descripcion
    self.etapas = Etapas.Etapas


lista_actividad.append('igor')
lista_actividad.append('sdf')
lista_actividad.append('gnf')


def nuevaActividad(self, nombre, fecha, descripcion, etapa):
    lista_actividad = [nombre, fecha, descripcion, etapa]
    print(lista_actividad)


def cambiarEtapa(activ, lista_actividad):
    if activ == Etapas.Etapas.nuevo:
        activ = Etapas.Etapas.propuesta


def MenuActivo():
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
        nuevaActividad(nombreActividad, fecha, descripcion, etapa)
        print(lista_actividad)
    elif elige == '2':
        for activo in lista_actividad:
            activ = input("elige actividad: ")
            cambiarEtapa(activ, lista_actividad)
    elif elige == '3':
        main.Menu()