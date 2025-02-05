class CuentaBancaria:
    saldo = 0
    usuario = None

    def __init__(self, usuario):
        self.usuario = usuario
    
    def getSaldo(self):
        return self.saldo
    
    def transferirDinero(self, usuarioReceptor, cantidadTransferir):
        self.saldo -= cantidadTransferir
        usuarioReceptor.getCuentaBancaria().recargarCuenta(cantidadTransferir)

    def recargarCuenta(self, nuevoSaldo):
        self.saldo += nuevoSaldo