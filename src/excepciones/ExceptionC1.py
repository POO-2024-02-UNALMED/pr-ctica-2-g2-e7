from ErrorAplicacion import ErrorAplicacion

class ExceptionC1(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__(mensaje)