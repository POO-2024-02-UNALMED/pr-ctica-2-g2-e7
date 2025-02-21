from excepciones.ExceptionC1 import ExceptionC1

class ExceptionInventada2(ExceptionC1):
    def __init__(self):
        super().__init__("Error específico 2 en ExceptionC1.")