class CuentaBancaria:


    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo = 0
    
    def getSaldo(self):
        return self.saldo
    
    def transferirDinero(self, usuarioReceptor, cantidadTransferir):
        self.saldo -= cantidadTransferir
        usuarioReceptor.getCuentaBancaria().recargarCuenta(cantidadTransferir)

    def recargarCuenta(self, nuevoSaldo):
        self.saldo += nuevoSaldo