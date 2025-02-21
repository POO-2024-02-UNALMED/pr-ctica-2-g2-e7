from excepciones.ExceptionC1 import ExceptionC1

class CarritoComprasVacio(ExceptionC1):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(mensaje)
        

    def comprobarCarrito(listaItems):
        if len(listaItems) == 0:
            raise CarritoComprasVacio("ERROR. Por favor verifique que su carrito de compras no este vacío.")