from excepciones.ErrorAplicacion import ErrorAplicacion

class ExceptionC2(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__(mensaje)