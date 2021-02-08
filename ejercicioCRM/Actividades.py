import Etapas


class Actividades():

    lista_actividad = []

    def __init__(self, nombre, fecha, descripcion, etapa):
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion
        self.etapas = Etapas.Etapas

    lista_actividad.append('igor')
    lista_actividad.append('sdf')
    lista_actividad.append('gnf')

    def nuevaActividad(self,nombre, fecha, descripcion, etapa):
        lista_actividad = [nombre, fecha, descripcion, etapa]
        print(lista_actividad)





