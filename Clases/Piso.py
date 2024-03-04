from Clases.ListaDoble import ListaDoble as Lista

import graphviz as gv

class Piso:
    def __init__(self,nombre,fila,columna,costoVolteo, costoIntercambio):
        self.nombre = nombre
        self.filas = int(fila)
        self.columnas = int(columna)
        self.costo_voleteo = int(costoVolteo)
        self.costo_intercambio = int(costoIntercambio)
        self.patron = Lista()

   
    def getNombre(self):
        return self.nombre
    
    def getfilas(self):
        return self.filas
    
    def getcolumnas(self):
        return self.columnas
    
    def getCostoVolteo(self):
        return self.costo_voleteo
    
    def getCostoIntercambio(self):
        return self.costo_intercambio
    
    def setCostoVolteo(self, costoVolteo):
        self.costo_voleteo = costoVolteo

    def setCostoIntercambio(self, costoIntercambio):
        self.costo_intercambio = costoIntercambio

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setFilas(self, filas):
        self.filas = filas
    
    def setColumnas(self, columnas):
        self.columnas = columnas

    def agregarPatron(self, patron):
        self.patron.agregar(patron)

    def buscarPorNombre(self, nombre):
        temp = self.filas.siguiente
        while temp != None:
            if temp.getValor() == nombre:
                return temp
            temp = temp.siguiente
        return None
    
    def mostrarPatronOrigen(self):
        temp = self.patron.inicio
        # print("Nombre: ", temp.getValor().getNombre())
        # print("Valor: ", temp.getValor().getValor())
        # print("\n")
        return temp.getValor()
    
    def mostrarPatronDestino(self):
        temp = self.patron.inicio
        temp = temp.siguiente
        # print("Nombre: ", temp.getValor().getNombre())
        # print("Valor: ", temp.getValor().getValor())
        # print("\n")
        return temp.getValor()
    

    def desplegar(self):
        print("Nombre: ", self.nombre)
        print("Filas: ", self.filas)
        print("Columnas: ", self.columnas)
        print("Costo Volteo: ", self.costo_voleteo)
        print("Costo Intercambio: ", self.costo_intercambio)
        print("Patron: ", self.patron)
        print("\n")

