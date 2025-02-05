from Cupon import Cupon

class Factura(Cupon):

    def __init__(self, carritoCompras, IDFactura, transaccion):
        super().__init__()
        self.carritoCompras = carritoCompras
        self.IDFactura = IDFactura
        self.transaccion = transaccion

        verificacion = self.crearCupon()
        if verificacion == True:
            valorDescuentoAleatorio = Cupon.generarValorCupon()
            comprador = transaccion.getUsuarioRemitente()
            comprador.getValorCupones().append(valorDescuentoAleatorio)
        
    
    def getCarritoCompras(self):
        return self.carritoCompras
    
    def getIDFactura(self):
        return self.IDFactura
