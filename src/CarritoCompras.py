from Inventario import Inventario

class CarritoCompras:
    def __init__(self, usuario, inventario):
        self.usuario = usuario
        self.inventario = inventario
        self.listaItems = []
        self.cantidadPorProducto = []
        self.precioTotal = 0
        self.descuentoAplicadoCompra = 0
    
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

    def getCantidadPorProducto(self):
        return self.cantidadPorProducto

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

    def añadirProducto(self, producto):
        #Si no se le pasa cantidad, se asume que se quiere añadir un producto
        estado = self.inventario.verificarProducto(producto, 1)
        if estado == True:
            if producto in self.listaItems:
                indice = self.listaItems.index(producto)
                cantidad = self.cantidadPorProducto[indice]
                if cantidad == 0:
                    return "Error. La cantidad mínima de productos que se puede añadir es 1"
                else:
                    self.cantidadPorProducto.insert(indice, cantidad + 1)
                    return "Producto añadido al carrito exitosamente"
            else:
                self.listaItems.append(producto)
                self.cantidadPorProducto.append(1)
                return "Producto añadido al carrito exitosamente"
        else:
            return "No hay suficiente producto en stock"
        
    
    def añadirProductoConCantidad(self, producto, cantidadAñadir):
        estado = self.inventario.verificarProducto(producto, cantidadAñadir)
        if estado == True:
            if cantidadAñadir > 5:
                return "Error. La cantidad máxima de productos que se puede añadir es 5"
            elif producto in self.listaItems:
                indice = self.listaItems.index(producto)
                cantidad = self.cantidadPorProducto[indice]
                if (cantidad + cantidadAñadir) > 5:
                    return "Error. La cantidad máxima de productos que se puede añadir es 5"
                else:
                    self.cantidadPorProducto.insert(indice, cantidad + cantidadAñadir)
                    return "Producto añadido al carrito exitosamente"
            else:
                self.listaItems.append(producto)
                self.cantidadPorProducto.append(cantidadAñadir)
                return "Producto añadido al carrito exitosamente"
        else:
            return "No hay suficiente producto en stock"