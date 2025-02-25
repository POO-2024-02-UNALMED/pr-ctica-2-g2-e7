from excepciones.ExceptionC2 import ExceptionC2

class SinStock(ExceptionC2):
    def __init__(self,mensaje):
        self.mensaje=mensaje
        super().__init__(mensaje)