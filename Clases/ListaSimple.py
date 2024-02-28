from Clases.Nodo import Nodo as Nodo

class ListaSimple:
    def __init__(self):
        self.inicio = None

    def agregar(self, valor):
        if self.inicio == None:
            self.inicio = Nodo(valor)
        else:
            temp = self.inicio
            while temp.siguiente != None:
                temp = temp.siguiente
            temp.siguiente = Nodo(valor)

    def desplegar(self):
        temp = self.inicio
        while temp != None:
            print(temp.valor)
            temp = temp.siguiente

