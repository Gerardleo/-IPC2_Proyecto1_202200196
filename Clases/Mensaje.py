class Mensaje:
    def __init__(self, mensaje, costo):
        self.mensaje = mensaje
        self.costo = costo


    def getMensaje(self):
        return self.mensaje
    
    def getCosto(self):
        return self.costo
    
    def setCosto(self, costo):
        self.costo = costo
        
    def setMensaje(self, mensaje):
        self.mensaje = mensaje