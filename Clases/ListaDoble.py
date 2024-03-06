from Clases.Nodo import Nodo as Nodo

class ListaDoble:
    def __init__(self):
        self.inicio = None
        self.anterior = None

    def agregar(self, valor):
        if self.inicio == None:
            self.inicio = Nodo(valor)
            self.anterior = self.inicio
        else:
            nuevo = Nodo(valor)
            self.anterior.siguiente = nuevo
            nuevo.anterior = self.anterior
            self.anterior = nuevo

    def buscar(self, valor):
        temp = self.inicio
        while temp != None:
            if temp.getValor().getNombre() == valor:
                return temp
            temp = temp.siguiente
        return None
    
    def desplegarPisos(self):
        temp = self.inicio
        print("===================================")
        print("           Lista de Pisos          ")
        print("===================================")
        while temp != None:
            print(temp.getValor().getNombre())
            temp = temp.siguiente

    def desplegarPatrones(self):
        temp = self.inicio
        print("===================================")
        print("           Lista de Patrones       ")
        print("===================================")
        while temp != None:
            print(temp.getValor().getNombre())
            temp = temp.siguiente

    def desplegarPisosyPatrones(self):
        temp = self.inicio
        while temp != None:
            print("===================================")
            print("           Lista de Piso          ")
            print("===================================")
            print(temp.getValor().getNombre())
            temp2 = temp.getValor().getPatron().inicio
            print("===================================")
            print("           Lista de Patrones       ")
            print("===================================")
            if temp2 == None:
                print("No hay patrones")
            while temp2 != None:
                print(temp2.getValor().getNombre())
                temp2 = temp2.siguiente
            temp = temp.siguiente
        temp = self.inicio

    def ordenar(self):
        temp = self.inicio
        while temp != None:
            temp2 = temp.siguiente
            while temp2 != None:
                if temp.getValor().getNombre() > temp2.getValor().getNombre():
                    aux = temp.getValor()
                    temp.setValor(temp2.getValor())
                    temp2.setValor(aux)
                temp2 = temp2.siguiente
            temp = temp.siguiente

    def buscarPatron(self, nombre):
        temp = self.inicio
        while temp != None:
            if temp.getValor().getNombre() == nombre:
                return temp.getValor()
            temp = temp.siguiente
        return None
    