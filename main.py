import xml.etree.ElementTree as ET
from Clases.Piso import Piso
from Clases.Patron import Patron
from Clases.ListaDoble import ListaDoble as Lista
from Clases.Procedimiento import Procedimiento
from Clases.Mensaje import Mensaje
import time

ListaPisos = Lista()
procedimientos = Procedimiento()
archivo = ""
pisoDestino= None
pisoOrigen= None
patronOrigen= None
patronDestino= None
matrizOrigen = None
matrizDestino = None

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
                print("Archivo cargado con exito")

            elif opcion_principal == '2':
                limpiarPisos()
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
                            nombrePiso = input("Ingrese el nombre del piso: ")
                            validacion = mostrarPatronOriginal(nombrePiso)
                            if validacion == False:
                                validacion = True
                                break
                            print("Generando patron original...")
                            time.sleep(2)
                            print("Patron generado")
                        elif opcion_submenu == '2':
                            logicaCostoMinimo(pisoOrigen.getValor().getCostoVolteo(), pisoOrigen.getValor().getCostoIntercambio())
                            procedimientos.desplegar()
                            procedimientos.limpiar()
                        elif opcion_submenu == '3':
                            nombrePiso = input("Ingrese el nombre del piso: ")
                            validacion = mostrarPatronDestino(nombrePiso)
                            if validacion == False:
                                validacion = True
                                break
                            print("Generando patron destino...")
                            time.sleep(2)
                            print("Patron generado")
                        elif opcion_submenu == '4':
                            break
                    else:
                        print("Opcion Invalida")

            elif opcion_principal == '3':
                print("Ordenando Pisos...")
                time.sleep(2)
                ListaPisos.ordenar()
                ListaPisos.desplegarPisos()
            elif opcion_principal == '4':
                print("Muchas gracias por usar el programa UwU")
                validador = False
        else:
            print("Opcion Invalida")


def mostrarPatronOriginal(nombrePiso):
    global pisoOrigen, patronOrigen,matrizOrigen
    pisoOrigen = ListaPisos.buscar(nombrePiso)
    if pisoOrigen is None:
        print("No se encontró el piso")
        return False
    
    pisoOrigen.getValor().mostrarPatronPisos()
    nombrePatron = input("Ingrese el nombre del patron: ")
    patronOrigen = pisoOrigen.getValor().getPatron().buscarPatron(nombrePatron)
    if patronOrigen is None:
        print("No se ha seleccionado ")
        return False
    
    #Genera la matriz del patron
    matrizOrigen = patronOrigen.matriz(pisoOrigen.getValor().getcolumnas())


    #Genera la imagen del patron
    patronOrigen.imprimir_matriz(matrizOrigen)
    arbol = patronOrigen.generar_dot(matrizOrigen)
    patronOrigen.generar_imagen_dot(arbol, f"Original-{nombrePatron}")


def mostrarPatronDestino(nombrePiso):
    global pisoDestino, pisoOrigen, patronOrigen, patronDestino,matrizDestino
    pisoDestino = ListaPisos.buscar(nombrePiso)
    if pisoDestino is None:
        print("No se encontró el piso")
        return False
    pisoDestino.getValor().mostrarPatronPisos()
    nombrePatron = input("Ingrese el nombre del patron: ")
    patronDestino = pisoDestino.getValor().getPatron().buscarPatron(nombrePatron)
    if patronDestino is None:
        print("No se ha seleccionado ")
        return False
    elif pisoDestino is None or pisoOrigen is None:
        print("No se ha seleccionado un patron origen o destino")
        return False
    elif not pisoDestino.getValor().validarPatrones(pisoOrigen, pisoDestino):
        limpiarPisos()
        print("Los patrones no tienen las mismas dimensiones")
        return False
    #Genera la matriz del patron
    matrizDestino = patronDestino.matriz(pisoDestino.getValor().getcolumnas())
    
    #Genera la imagen del patron
    patronDestino.imprimir_matriz(matrizDestino)
    arbol = patronDestino.generar_dot(matrizDestino)
    patronDestino.generar_imagen_dot(arbol, f"Destino-{nombrePatron}")


def limpiarVariables():
    global ListaPisos, archivo, pisoDestino, pisoOrigen, patronOrigen, patronDestino
    ListaPisos = Lista()
    archivo = ""
    pisoDestino= None
    pisoOrigen= None
    patronOrigen= None
    patronDestino= None

def limpiarPisos():
    global ListaPisos, pisoDestino, pisoOrigen, patronOrigen, patronDestino, matrizDestino, matrizOrigen
    pisoDestino= None
    pisoOrigen= None
    patronOrigen= None
    patronDestino= None
    matrizDestino = None
    matrizOrigen = None
    procedimientos = Procedimiento()

def logicaCostoMinimo(costoVolteo, costoIntercambio):
    global matrizDestino, matrizOrigen, patronOrigen, patronDestino, pisoOrigen, pisoDestino

    if matrizOrigen is None or matrizDestino is None:
        print("No se ha seleccionado un patrón origen o destino")
        return 

    if patronOrigen.getNombre() == patronDestino.getNombre():
        mensaje = Mensaje("Los patrones son iguales, no se realizará ninguna operación", 0)
        procedimientos.agregar(mensaje)
        return    

    tempO = matrizOrigen.inicio
    tempD = matrizDestino.inicio

    try:
        # Iterar sobre todas las celdas de ambas matrices
        while tempO is not None and tempD is not None:
            filaO = tempO.valor.inicio
            filaD = tempD.valor.inicio

            # Iterar sobre todas las celdas de la fila actual
            while filaO is not None and filaD is not None:
                # Si los valores no coinciden
                if filaO.valor != filaD.valor:
                    # Si los valores adyacentes coinciden
                    if filaO.siguiente is not None and filaD.siguiente is not None:
                        if filaO.siguiente.valor == filaD.valor: 
                            mensaje = Mensaje(f"Se ha encontrado un intercambio en la posición {filaO.valor} y {filaD.valor}", costoIntercambio)
                            procedimientos.agregar(mensaje)
                        
                        elif filaD.siguiente is None:
                            mensaje = Mensaje(f"Se ha encontrado un volteo en la posición {filaO.valor} y {filaD.valor}", costoVolteo)
                            procedimientos.agregar(mensaje)
                
                # Avanzar a la siguiente celda en ambas filas
                filaO = filaO.siguiente
                filaD = filaD.siguiente

            # Avanzar a la siguiente fila en ambas matrices
            tempO = tempO.siguiente
            tempD = tempD.siguiente
    except Exception as e:
        print("Error: ", e)
        return

        

    
    





    

    

if __name__ == "__main__":
    print("Bienvenido al programa")
    archivo = ""
    try:
        main()
    except Exception as e:
        print("Error: ", e)
