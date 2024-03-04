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

    def getPatron(self):
        return self.patron

    def buscarPorNombre(self, nombre):
        temp = self.filas.siguiente
        while temp != None:
            if temp.getValor() == nombre:
                return temp
            temp = temp.siguiente
        return None
    
    def mostrarPatronOrigen(self, nombre):
        temp = self.patron.inicio
        while temp != None:
            if temp.getValor().getNombre() == nombre:
                return temp.getValor()
            temp = temp.siguiente
        return temp.getValor()
    
    def mostrarPatronDestino(self, nombre):
        temp = self.patron.inicio
        while temp != None:
            if temp.getValor().getNombre() == nombre:
                return temp.getValor()
            temp = temp.siguiente
        
        return temp.getValor()
    
    def mostrarPatronPisos(self):
        temp = self.patron.inicio
        print("===================================")
        print("           Lista de Pisos          ")
        print("===================================")
        while temp != None:
            print(temp.getValor().getNombre())
            temp = temp.siguiente


    def validarPatrones(self, PisoOrigen,PisoDestino):
        if PisoOrigen.getValor().getfilas() == PisoDestino.getValor().getfilas() and PisoOrigen.getValor().getcolumnas() == PisoDestino.getValor().getcolumnas():
            return True
        else:
            return False
    

    def desplegar(self):
        print("Nombre: ", self.nombre)
        print("Filas: ", self.filas)
        print("Columnas: ", self.columnas)
        print("Costo Volteo: ", self.costo_voleteo)
        print("Costo Intercambio: ", self.costo_intercambio)
        print("Patron: ", self.patron)
        print("\n")

