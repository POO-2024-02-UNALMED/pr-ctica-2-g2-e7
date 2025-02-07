from .Usuario import Usuario

class Vendedor(Usuario):
    def __init__(self, nombre, cuentaBancaria, inventario, fabrica):
        super().__init__(nombre, cuentaBancaria)
        self.ventasRealizadas = 0
        self.inventario = inventario
        self.fabrica = fabrica


    def consultarCuentaBancaria(self):
        return f"Estado de tu cuenta bancaria:\nSaldo: {self.cuentaBancaria.getSaldo()}"

