import xml.etree.ElementTree as ET
from Clases.Piso import Piso
from Clases.Patron import Patron
#from Clases.Nodo import Nodo

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
            piso.desplegar()
    
            # Buscar los patrones dentro de cada piso
            for patron in pisos.findall('.//patron'): 
                codigo = patron.get('codigo')
                valor = patron.text.strip()  # Eliminar espacios en blanco al inicio y al final
                patron = Patron(codigo, valor)
                patron.desplegar()
                piso.agregarPatron(patron)
                piso.imprimirMatriz()
                
        piso.graficaMatriz()

            # Crear la matriz de patrones
           

        
            
        

    except Exception as e:
        print("Error: ", e)
        return None  # Devolver None si hay un error    

def main():
    validador = True
    while validador:
        print("1. Mostrar graficamente el patron")
        print("2. Seleccionar un nuevo código de patrón")
        print("3. opcion")
        print("4. opcion")
        print("5. opcion")
        opcion_principal = str(input("Ingrese una opcion: "))

        if opcion_principal in ('1', '2', '3', '4', '5'):
            if opcion_principal == '1':
                archivo = input("Ingrese el nombre del archivo: ")
                leer_xml(archivo)

            elif opcion_principal == '2':
                while True:
                    print("1. Ingresar nuevo patron")
                    print("2. Usar patron existente")
                    print("3. Regresar")
                    opcion_submenu = str(input("Ingrese una opcion: "))
                    if opcion_submenu in ('1', '2', '3'):
                        if opcion_submenu == '1':
                            pass
                        elif opcion_submenu == '2':
                            pass
                        elif opcion_submenu == '3':
                            break
                    else:
                        print("Opcion Invalida")

            elif opcion_principal == '3':
                pass
            elif opcion_principal == '4':
                pass
            elif opcion_principal == '5':
                print("Muchas gracias por usar el programa UwU")
                validador = False
        else:
            print("Opcion Invalida")

if __name__ == "__main__":
    print("Bienvenido al programa")
    archivo = ""
    try:
        main()
    except Exception as e:
        print("Error: ", e)
