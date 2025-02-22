class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        super().__init__(f"Manejo de errores de la Aplicación: {mensaje}")
