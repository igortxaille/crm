class Clientes():
    lista_clientes = []

    def __init__( self,nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def nuevoClientes(nombre, apellidos):
        lista_clientes = [nombre, apellidos]
        for clientes in lista_clientes:
            print(lista_clientes)
