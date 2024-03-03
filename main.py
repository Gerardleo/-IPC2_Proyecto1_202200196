import xml.etree.ElementTree as ET
from Clases.Piso import Piso
from Clases.Patron import Patron
from Clases.ListaDoble import ListaDoble as Lista
import time

ListaPisos = Lista()
def leer_xml(archivo):
    try:
        tree = ET.parse(archivo)
        root = tree.getroot()
       
        for pisos in root.findall('piso'):
            nombre = pisos.get('nombre')
            fila = pisos.find('R').text
            columna = pisos.find('C').text
            costo_volteo = pisos.find('F').text
            costo_intercambio = pisos.find('S').text
            piso = Piso(nombre, fila, columna, costo_volteo, costo_intercambio)
           # piso.desplegar()
    
            # Buscar los patrones dentro de cada piso
            for patron in pisos.findall('.//patron'): 
                codigo = patron.get('codigo')
                valor = patron.text.strip()  # Eliminar espacios en blanco al inicio y al final
                patron = Patron(codigo, valor)
               # patron.desplegar()
                piso.agregarPatron(patron)
                #matriz = patron.matriz(int(columna))
                #patron.imprimir_matriz(matriz)
                
                #arbol = patron.generar_dot(matriz)
                #patron.generar_imagen_dot(arbol, codigo)

            ListaPisos.agregar(piso)
            #ListaPisos.ordenar()
            #ListaPisos.desplegar()
            
                

            # Crear la matriz de patrones

    except Exception as e:
        print("Error: ", e)
        return None  # Devolver None si hay un error    

def main():
    validador = True
    while validador:
        print("===================================")
        print("           Menú Principal          ")
        print("===================================")
        print("1. Cargar archivo XML")
        print("2. Gestionar Pisos")
        print("3. Ordenar Pisos")
        print("4. Salir")
        print("")
        opcion_principal = str(input("Ingrese una opcion: "))

        if opcion_principal in ('1', '2', '3', '4', '5'):
            if opcion_principal == '1':
                limpiarVariables()
                archivo = input("Ingrese el nombre del archivo: ")
                leer_xml(archivo)

            elif opcion_principal == '2':
                nombrePiso = input("Ingrese el nombre del piso: ")
                while True:
                    print("===================================")
                    print("           Gestionar Pisos         ")
                    print("===================================")
                    print("1. Mostrar Patron de Original")
                    print("2. Mostrar Paso a Paso solucion de Piso")
                    print("3. Mostrar Patron de Destino")
                    print("4. Regresar")
                    opcion_submenu = str(input("Ingrese una opcion: "))
                    if opcion_submenu in ('1', '2', '3', '4'):
                        if opcion_submenu == '1':
                            print("Generando patron original...")
                            time.sleep(2)
                            mostrarPatronOriginal(nombrePiso)
                            print("Patron generado")

                            pass
                        elif opcion_submenu == '2':
                            pass
                        elif opcion_submenu == '3':
                            print("Generando patron destino...")
                            time.sleep(2)
                            mostrarPatronDestino(nombrePiso)
                            print("Patron generado")
                        elif opcion_submenu == '4':
                            break
                    else:
                        print("Opcion Invalida")

            elif opcion_principal == '3':
                print("Ordenando Pisos...")
                time.sleep(2)
                ListaPisos.ordenar()
                ListaPisos.desplegar()
            elif opcion_principal == '4':
                pass
            elif opcion_principal == '5':
                print("Muchas gracias por usar el programa UwU")
                validador = False
        else:
            print("Opcion Invalida")


def mostrarPatronOriginal(nombrePiso):
    piso = ListaPisos.buscar(nombrePiso)
    if piso is None:
        print("No se encontró el piso")
        return
    Patron = piso.getValor().mostrarPatronOrigen()
    matriz = Patron.matriz(piso.getValor().getcolumnas())
    Patron.imprimir_matriz(matriz)
    arbol = Patron.generar_dot(matriz)
    Patron.generar_imagen_dot(arbol, f"Original-{nombrePiso}")

def mostrarPatronDestino(nombrePiso):
    Piso = ListaPisos.buscar(nombrePiso)
    if Piso is None:
        print("No se encontró el piso")
        return
    Patron = Piso.getValor().mostrarPatronDestino()
    matriz = Patron.matriz(Piso.getValor().getcolumnas())
    Patron.imprimir_matriz(matriz)
    arbol = Patron.generar_dot(matriz)
    Patron.generar_imagen_dot(arbol, f"Destino-{nombrePiso}")

def limpiarVariables():
    ListaPisos = Lista()
    archivo = ""


if __name__ == "__main__":
    print("Bienvenido al programa")
    archivo = ""
    try:
        main()
    except Exception as e:
        print("Error: ", e)
