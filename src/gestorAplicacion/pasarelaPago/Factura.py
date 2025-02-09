from .Cupon import Cupon

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
    
    def verificarProducto(self, idproducto, cantidadRetornar):
        producto = self.carritoCompras.buscarProducto(idproducto)
        if(producto != None):
            if(producto.isRetornable()):
                cantidadVendida = self.carritoCompras.getCantidadPorProducto(producto)
                if(cantidadVendida >= cantidadRetornar and cantidadRetornar > 0):
                    return producto
        return None
    
    def modificarFactura(self, producto, cantidad, accion):
        if accion.casefold() == "eliminar":
            self.carritoCompras.restarCantidadPorProducto(producto, cantidad)
    
    def getCarritoCompras(self):
        return self.carritoCompras
    
    def getIDFactura(self):
        return self.IDFactura
