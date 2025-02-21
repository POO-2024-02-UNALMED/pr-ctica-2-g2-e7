from excepciones.ExceptionC2 import ExceptionC2

class CantidadInvalidaError(ExceptionC2):
    def __init__(self, mensaje):
        super().__init__(mensaje)