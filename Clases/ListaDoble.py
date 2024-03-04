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
    
    def desplegar(self):
        temp = self.inicio
        print("===================================")
        print("           Lista de Pisos          ")
        print("===================================")
        while temp != None:
            print(temp.getValor().getNombre())
            temp = temp.siguiente

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


    

            
