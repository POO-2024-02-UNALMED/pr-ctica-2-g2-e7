from excepciones.ExceptionC2 import ExceptionC2

class ExceptionSugerida2(ExceptionC2):
    def __init__(self):
        super().__init__("Dato ingresado no es válido en esta categoría.")