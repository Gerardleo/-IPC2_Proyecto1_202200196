import Clases.ListaSimple as Lista

class Patron:
    def __init__(self, nombre,valor):
        self.nombre = nombre
        self.valor = valor

    def getNombre(self):
        return self.nombre
    
    def getValor(self):
        return self.valor
    
    def setNombre(self, nombre):
        self.nombre = nombre    

    def desplegar(self):
        print("Nombre: ", self.nombre)
        print("Valor: ", self.valor)
        print("\n")

    