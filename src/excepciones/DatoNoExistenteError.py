from excepciones.ExceptionC1 import ExceptionC1

class DatoNoExistenteError(ExceptionC1):
    def __init__(self, mensaje):
        super().__init__(mensaje)