class CarritoCompras:
    usuario = None
    listaItems = []
    cantidadPorProducto = []
    precioTotal = 0
    descuentoAplicadoCompra = 0

    def __init__(self, usuario):
        self.usuario = usuario
    
    def getUsuario(self):
        return self.usuario
    def setUsuario(self, usuario):
        self.usuario = usuario

    def getPrecioTotal(self):
        return self.precioTotal
    def setPrecioTotal(self, value):
        self.precioTotal = value

    def getListaItems(self):
        return self.listaItems
    
    def setDesceuntoAplicadoCompra(self, descuento):
        self.descuentoAplicadoCompra = descuento

    def calcularTotal(self):
        for i in range(len(self.listaItems)):
            self.precioTotal += self.listaItems[i].getPrecio() * self.cantidadPorProducto[i]
        
        if self.descuentoAplicadoCompra != 0:
            self.precioTotal -= self.precioTotal * self.descuentoAplicadoCompra / 100

    def restarProductosAlComprar(self):
        for i in range(len(self.listaItems)):
            producto = self.listaItems[i]
            cantidadComprada = self.cantidadPorProducto[i]
            producto.setCantidad(producto.getCantidad() - cantidadComprada) #Esto es para restar la cantidad de productos comprados a la cantidad total de ese producto