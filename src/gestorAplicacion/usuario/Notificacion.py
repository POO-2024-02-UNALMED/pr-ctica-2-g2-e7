from .Usuario import Usuario
from datetime import datetime

class Notificacion:
    def __init__(self, mensaje, asunto, destinatario):
        self.mensaje = mensaje
        self.asunto = asunto
        self.destinatario = destinatario

        fecha_actual = datetime.now()

        self.fecha = fecha_actual.strftime("%Y-%m-%d %H:%M")
    
    def getMensaje(self):
        return self.mensaje
    
    def setMensaje(self, value):
        self.mensaje = value

    def getAsunto(self):
        return self.asunto
    
    def setAsunto(self, value):
        self.asunto = value

    def getDestinatario(self):
        return self.destinatario
    
    def setDestinatario(self, value):
        self.destinatario = value
    
    def getFecha(self):
        return self.fecha
    
    def mostrarResumen(self):

        return f"Fecha: {self.fecha}\nDestinatario: {self.destinatario}\nAsunto: {self.asunto}\nMensaje: {self.mensaje[:80]}\n"
    