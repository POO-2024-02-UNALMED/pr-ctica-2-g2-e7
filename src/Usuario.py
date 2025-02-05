from Transaccion import Transaccion

class Usuario:

    def __init__(self, nombre, cuentaBancaria):
        self.nombre = nombre
        self.cuentaBancaria = cuentaBancaria
        self.membresia = ""
        self.vecesComprado = 0

    def  getCuentaBancaria(self):
        return self.cuentaBancaria
    
    def setCuentaBancaria(self, value):
        self.cuentaBancaria = value
    
    def pago(self, usuarioRemitente, usuarioReceptor, cantidadTransferir, tipoTransaccion):
        transaccion = Transaccion(usuarioRemitente, usuarioReceptor, tipoTransaccion)
        transaccion.setEstadoCompra(True)

        if tipoTransaccion.casefold() == "devolución":
            transaccion.ejecutarTransaccion(cantidadTransferir)
        elif tipoTransaccion.casefold() == "compra":
            transaccion.generarFactura()
            transaccion.ejecutarTransaccion(cantidadTransferir)
            pass
