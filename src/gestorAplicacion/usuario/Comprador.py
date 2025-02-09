from .Usuario import Usuario
from ..compras.HistorialCompras import HistorialCompras

class Comprador(Usuario):
    def __init__(self, nombre, cuentaBancaria, carritoCompras):
        super().__init__(nombre, cuentaBancaria)
        self.carritoCompras = carritoCompras
        self.historialCompras = HistorialCompras()
        self.valorCupones = [10]
        self.cantidadCupones = 1

    def mostrarHistorialCompras(self):
        return self.historialCompras.mostrarFactura()

    def getValorCupones(self):
        return self.valorCupones
    
    def mostrarCupones(self):
        mensaje = ""
        for i in range(len(self.valorCupones)):
            mensaje += f"{i+1}. Descuento de: {self.valorCupones[i]}%\n"
        return mensaje
    
    def devolverProducto(self, idfactura, idproducto, cantidadretornar, vendedor):
        factura = self.historialCompras.buscarFactura(idfactura)
        if(factura != None):
            producto = factura.verificarProducto(idproducto, cantidadretornar)
            if(producto != None):
                descuento = factura.getCarritoCompras().getDescuentoAplicadoCompra()
                valorDevolver = vendedor.devolucionDinero(self, producto.getPrecio(), descuento, cantidadretornar)
                vendedor.reingresarProducto(cantidadretornar, producto)
                
    
    def getCarritoCompras(self):
        return self.carritoCompras
    
    def setCarritoCompras(self, carritoCompras):
        self.carritoCompras = carritoCompras

    def getHistorialCompras(self):
        return self.historialCompras
    
    def eliminarCupones(self, cuponEliminar):
        self.valorCupones.pop(cuponEliminar - 1)

    def consultarCuentaBancaria(self):
        return f"Estado de tu cuenta bancaria:\nSaldo: {self.cuentaBancaria.getSaldo()}"