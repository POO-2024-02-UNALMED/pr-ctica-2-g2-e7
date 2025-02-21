from excepciones.ExceptionC1 import ExceptionC1

class SaldoInsuficienteError(ExceptionC1):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(mensaje)


