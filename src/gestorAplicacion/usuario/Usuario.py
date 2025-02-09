from ..pasarelaPago.Transaccion import Transaccion
from .Notificacion import Notificacion
from abc import ABC, abstractmethod

class Usuario(ABC):

    def __init__(self, nombre, cuentaBancaria):
        self.nombre = nombre
        self.cuentaBancaria = cuentaBancaria
        self.membresia = None
        self.vecesComprado = 0
        self.puntos = 0
        self.notificaciones = []

    def  getCuentaBancaria(self):
        return self.cuentaBancaria
    
    def setCuentaBancaria(self, value):
        self.cuentaBancaria = value

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, value):
        self.nombre = value

    def getNotificaciones(self):
        return self.notificaciones
    
    def getMembresia(self): 
        return self.membresia
    
    def setMembresia(self, value):
        self.membresia = value

    def getVecesComprado(self):
        return self.vecesComprado
    
    def setVecesComprado(self, value):
     self.vecesComprado+=value

    def getPuntos(self):
        return self.puntos
    
    def setPuntos(self, value):
        self.puntos = value
    
    def pago(self, usuarioRemitente, usuarioReceptor, cantidadTransferir, tipoTransaccion):
        transaccion = Transaccion(usuarioRemitente, usuarioReceptor, tipoTransaccion)
        transaccion.setEstadoCompra(True)

        if tipoTransaccion.casefold() == "devolución":
            transaccion.ejecutarTransaccion(cantidadTransferir)
        elif tipoTransaccion.casefold() == "compra":
            transaccion.generarFactura()
            transaccion.ejecutarTransaccion(cantidadTransferir)
            pass

    def mostrarNotificaciones(self):
        cont = 1
        notificaciones = ""
        for notificacion in self.notificaciones:
            notificaciones += f"\n{cont}. {notificacion.mostrarResumen()}\n"
            cont += 1
        return notificaciones
    
    def recibirNotificacion(self, mensaje, asunto):
        notificacion = Notificacion(mensaje, asunto, self)
        self.notificaciones.append(notificacion)
    
    @abstractmethod
    def consultarCuentaBancaria(self):
        pass