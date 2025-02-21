from ExceptionC1 import ExceptionC1

class ExceptionSugerida1(ExceptionC1):
    def __init__(self):
        super().__init__("Dato ingresado no existe. Por favor, ingrese un valor válido.")