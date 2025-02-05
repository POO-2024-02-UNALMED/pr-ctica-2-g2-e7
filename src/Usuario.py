class Usuario:
    membresia = ""
    vecesComprado = 0
    puntos = 0
    nombre = ""
    cuentaBancaria = None

    def __init__(self, nombre, cuentaBancaria):
        self.nombre = nombre
        self.cuentaBancaria = cuentaBancaria

    def  getCuentaBancaria(self):
        return self.cuentaBancaria
    
    def setCuentaBancaria(self, value):
        self.cuentaBancaria = value
    
    def pago(self, usuarioRemitente, usuarioReceptor, cantidadTransferir, tipoTransaccion):
        # Espacio para eso xd
        pass
