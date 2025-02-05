from Usuario import Usuario

class Comprador(Usuario):
    carritoCompras = None
    historialCompras = None
    valorCupones = [10]
    cantidadCupones = 1

    def __init__(self, nombre, cuentaBancaria, carritoCompras):
        super().__init__(nombre, cuentaBancaria)
        self.carritoCompras = carritoCompras


    def getValorCupones(self):
        return self.valorCupones
    
    def mostrarCupones(self):
        mensaje = ""
        for i in range(len(self.valorCupones)):
            mensaje += f"{i+1}. Descuento de: {self.valorCupones[i]}%\n"
        return mensaje
    
    
    def getCarritoCompras(self):
        return self.carritoCompras
    def setCarritoCompras(self, carritoCompras):
        self.carritoCompras = carritoCompras