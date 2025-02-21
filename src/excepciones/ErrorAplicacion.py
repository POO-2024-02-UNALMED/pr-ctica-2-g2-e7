class ErrorAplicacion(Exception):
    
    def __init__(self, mensaje, codigo_error):
        super().__init__("Manejo de errores de la aplicacion")
        self.codigo_error = codigo_error
        self.mensaje=mensaje
    def mostrar(self):
        return (f"Manejo de errores de la Aplicación {self.mensaje} codigo de error: {self.codigo_error}")
