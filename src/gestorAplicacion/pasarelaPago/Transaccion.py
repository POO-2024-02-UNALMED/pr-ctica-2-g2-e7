from .Factura import Factura

class Transaccion:

    def __init__(self, usuarioRemitente, usuarioReceptor, tipoTransaccion):
        self.usuarioRemitente = usuarioRemitente
        self.usuarioReceptor = usuarioReceptor
        self.tipoTransaccion = tipoTransaccion
        self.estadoCompra = False


    def setEstadoCompra(self, estadoCompra):
        self.estadoCompra = estadoCompra
    
    def getUsuarioRemitente(self):
        return self.usuarioRemitente

    def ejecutarTransaccion(self, cantidadTransferir):
        if self.estadoCompra == True:
            self.usuarioRemitente.getCuentaBancaria().transferirDinero(self.usuarioReceptor, cantidadTransferir)

    def generarFactura(self):
        comprador = self.usuarioRemitente
        factura = Factura(comprador.getCarritoCompras(), len(comprador.getHistorialCompras().getFacturas()) + 1, self)
        comprador.getHistorialCompras().agregarFactura(factura)
        comprador.getHistorialCompras().actualizarCantidadesCompradas(factura)
        comprador.getHistorialCompras().actualizarCategoriasMasCompradas()
