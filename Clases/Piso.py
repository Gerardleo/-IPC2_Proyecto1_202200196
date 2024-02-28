from Clases.ListaSimple import ListaSimple as Lista
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
    
    def crearMatriz(self):
#crear una matriz de un patron 
    
        matriz = Lista()  # Inicializamos la matriz como una lista enlazada simple vacía
        
        temp = self.patron.inicio
        while temp != None:
            letra = 0
            patron = temp.getValor()
            nombre = patron.getNombre()
            valor = patron.getValor()
            for i in range(self.filas):
                for j in range(self.columnas):
                    caracter = valor[letra]
                    matriz.agregar(caracter)
                    letra += 1
            temp = temp.siguiente
        return matriz
    
    def imprimirMatriz(self):
        matriz = self.crearMatriz()
        temp = matriz.inicio
        nombre = self.getNombre()
        print("Matriz del piso: ", nombre)
        for i in range(self.filas):
            for j in range(self.columnas):
                print(temp.getValor(), end = " ")
                temp = temp.siguiente
            print("\n")

    def graficaMatriz(self):
        matriz = self.crearMatriz()
        temp = matriz.inicio
        nombre = self.getNombre()
        dot = gv.Digraph(comment='Matriz del piso: ' + nombre)
        dot.node("Matriz", "Matriz del piso: " + nombre)
        for i in range(self.filas):
            for j in range(self.columnas):
                dot.node(str(i) + str(j), temp.getValor())
                temp = temp.siguiente
        temp = matriz.inicio
        for i in range(self.filas):
            for j in range(self.columnas):
                if j != self.columnas - 1:
                    dot.edge(str(i) + str(j), str(i) + str(j + 1))
                if i != self.filas - 1:
                    dot.edge(str(i) + str(j), str(i + 1) + str(j))
        dot.render('Matriz', view=True)
    
    def desplegar(self):
        print("Nombre: ", self.nombre)
        print("Filas: ", self.filas)
        print("Columnas: ", self.columnas)
        print("Costo Volteo: ", self.costo_voleteo)
        print("Costo Intercambio: ", self.costo_intercambio)
        print("Patron: ", self.patron)
        print("\n")

