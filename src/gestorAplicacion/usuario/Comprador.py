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
    
    def devolverProducto(self, idfactura, idproducto, cantidadRetornar, vendedor):
        factura = self.historialCompras.buscarFactura(idfactura)
        if(factura != None):
            producto = factura.verificarProducto(idproducto, cantidadRetornar)
            if(producto != None):
                descuento = factura.getCarritoCompras().getDescuentoAplicadoCompra()
                valorDevolver = vendedor.devolucionDinero(self, producto.getPrecio(), descuento, cantidadRetornar)
                vendedor.reingresarProducto(cantidadRetornar, producto)
                self.historialCompras.actualizarCantidadDevueltos(cantidadRetornar)
                factura.modificarFactura(producto, cantidadRetornar, "eliminar")
                mensajeComprador = f"Su devolución de {cantidadRetornar} {producto.getNombre()}/s por un valor de {valorDevolver} pesos (corresponde a lo pagado menos un 10% de retención) ha sido procesada exitosamente."; 
                asuntoComprador = "Devolución procesada"; 
                mensajeVendedor = f"Ha recibido una devolución de {cantidadRetornar} productos por un valor de {valorDevolver}."; 
                asuntoVendedor = "Devolución recibida";
                self.recibirNotificacion(mensajeComprador, asuntoComprador)
                vendedor.recibirNotificacion(mensajeVendedor, asuntoVendedor)
                return "DevolucionExitosa"
            return "ProductoInvalido"
        return "FacturaInvalida"
    
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