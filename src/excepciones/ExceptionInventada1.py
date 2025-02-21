from ExceptionC1 import ExceptionC1

class ExceptionInventada1(ExceptionC1):
    def __init__(self):
        super().__init__("Error específico 1 en ExceptionC1.")