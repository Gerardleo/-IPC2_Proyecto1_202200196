from Clases.ListaDoble import ListaDoble as Lista

class Procedimiento:
    def __init__(self):
        self.prodicimientos = Lista()
        

    def agregar(self, valor):
        self.prodicimientos.agregar(valor)

    def desplegar(self):
        total = 0
        temp = self.prodicimientos.inicio
        print("===================================")
        print("       Lista de Procedimientos     ")
        print("===================================")
        while temp != None:
            print(f"{temp.getValor().getMensaje()}- costr: {temp.getValor().getCosto()}")
            total += temp.getValor().getCosto()
            temp = temp.siguiente
        print("===================================")
        print("           Total: ", total)
        print("===================================")
    
    def limpiar(self):
        self.prodicimientos = Lista()