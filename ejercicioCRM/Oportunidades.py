class Oportunidades():
    lista_Oportunidad = []
    def __init__(self, nombre):
        self.nombre = nombre

    def nuevaOportunidad(self,nombre):
        lista_Oportunidad = [nombre]
        for  oportunidad in  lista_Oportunidad:
            print(oportunidad)


