from Cupon import Cupon

class Factura(Cupon):
    carritoCompras = None
    IDFactura = 0
    transaccion = None

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
