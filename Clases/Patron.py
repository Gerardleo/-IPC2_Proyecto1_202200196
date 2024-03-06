from Clases.ListaDoble import ListaDoble as Lista
import graphviz as gv

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

    def setValor(self, valor):
        self.valor = valor

    def desplegar(self):
        print("Nombre: ", self.nombre)
        print("Valor: ", self.valor)
        print("\n")

    def matriz(self, columnas):
        matriz = Lista()
        contador = 0
        fila_actual = Lista()
        for letra in self.valor:
            if contador < columnas:
                fila_actual.agregar(letra)
                contador += 1
            else:
                matriz.agregar(fila_actual)
                fila_actual = Lista()
                fila_actual.agregar(letra)
                contador = 1  # Reiniciar contador para la nueva fila
        matriz.agregar(fila_actual)  # Agregar la última fila
        return matriz
    
    def imprimir_matriz(self,matriz):
        nodo_fila = matriz.inicio
        while nodo_fila is not None:
            nodo_columna = nodo_fila.valor.inicio
            while nodo_columna is not None:
                nodo_columna = nodo_columna.siguiente
            nodo_fila = nodo_fila.siguiente

    def generar_dot(self,matriz):
        dot_code = 'digraph G {\n'
        dot_code += 'node [shape=plaintext];\n'
        dot_code += 'matriz [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="5" CELLPADDING="5">\n'  # Modificación aquí

        nodo_fila = matriz.inicio
        while nodo_fila is not None:
            dot_code += '<TR>'
            nodo_columna = nodo_fila.valor.inicio
            while nodo_columna is not None:
                if nodo_columna.valor == 'B' :
                    color = 'white'
                else :
                    color = 'black'
                dot_code += f'<TD BGCOLOR="{color}" WIDTH="30" HEIGHT="30"></TD>'
                nodo_columna = nodo_columna.siguiente
            dot_code += '</TR>\n'
            nodo_fila = nodo_fila.siguiente

        dot_code += '</TABLE>>];\n'
        dot_code += '}'

        return dot_code
    
    
    def generar_imagen_dot(self,dot_code, file_path='matriz.png'):
        graph = gv.Source(dot_code)
        graph.render(file_path, format='png', cleanup=True)
