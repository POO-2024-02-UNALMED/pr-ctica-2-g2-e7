from .Usuario import Usuario

class Vendedor(Usuario):
    def __init__(self, nombre, cuentaBancaria, inventario, fabrica):
        super().__init__(nombre, cuentaBancaria)
        self.ventasRealizadas = 0
        self.inventario = inventario
        self.fabrica = fabrica


    def consultarCuentaBancaria(self):
        return f"Estado de tu cuenta bancaria:\nSaldo: {self.cuentaBancaria.getSaldo()}"
    
    def devolucionDinero(self, usuarioReceptor, precioProducto, descuento, cantidadRetornar):
        valorDevolver = 0
        if(descuento > 0):
            precioConDescuento = precioProducto - (precioProducto * (descuento / 100.0))
            valorDevolver = (precioConDescuento - (precioConDescuento * 0.1)) * cantidadRetornar
        else:
            valorDevolver = (precioProducto - (precioProducto * 0.1)) * cantidadRetornar
        
        super().pago(self, usuarioReceptor, valorDevolver, "devolución")
        return valorDevolver
    
    def reingresarProducto(self, cantidad, producto):
        self.inventario.reabastecerProductos(cantidad, producto)

