from ..tienda.Inventario import Inventario
from ..usuario.Usuario import Usuario
from multimethod import multimethod
from ..tienda.Producto import Producto

class CarritoCompras:
    @multimethod
    def __init__(self, usuario : Usuario, inventario : Inventario ):
        self.usuario = usuario
        self.inventario = inventario
        self.listaItems = []
        self.cantidadPorProducto = []
        self.precioTotal = 0
        self.descuentoAplicadoCompra = 0
    @multimethod 
    def __init__(self):
        return
    
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
    
    def getCantidadPorProducto(self):
        return self.cantidadPorProducto
    
    def setDescuentoAplicadoCompra(self, descuento):
        self.descuentoAplicadoCompra = descuento

    def getCantidadPorProductos(self, producto):
        indice = self.listaItems.index(producto)
        return self.cantidadPorProducto[indice]

    def calcularTotal(self):
        for i in range(len(self.listaItems)):
            self.precioTotal += self.listaItems[i].getPrecio() * self.cantidadPorProducto[i]
        
        if self.descuentoAplicadoCompra != 0:
      
          self.precioTotal -= self.precioTotal * (self.descuentoAplicadoCompra / 100)
    @multimethod
    def añadirProducto(self, producto : Producto):
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
    @multimethod 
    def añadirProducto(self, producto : Producto , cantidadAñadir : int):
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

    def restarProductosAlComprar(self):
        for i in range(len(self.listaItems)):
            producto = self.listaItems[i]
            cantidadComprada = self.cantidadPorProducto[i]
            producto.setCantidad(producto.getCantidad() - cantidadComprada) #Esto es para restar la cantidad de productos comprados a la cantidad total de ese producto

    def restarCantidadPorProducto(self , producto, cantidad):
        indice= self.listaItems.index(producto)
        self.cantidadPorProducto[indice]-=cantidad
        if self.cantidadPorProducto[indice] == 0:
            self.listaItems.pop(indice)
        self.calcularTotal()
    def buscarProducto(self , idProducto):
        for i in range(0,len(self.listaItems),1):
            if self.listaItems[i].getID()== idProducto:
                return self.listaItems[i]
        return None   
    

    def __str__(self):
        sb = []
        sb.append(f"Carrito de {self.usuario.getNomnbre()}:\n\n")
        sb.append("Lista de productos:\n")
        
        for i in range(len(self.listaItems)):
            sb.append(f"{self.listaItems[i]} cantidad: {self.cantidadPorProducto[i]}\n\n")
        
        self.calcularTotal()
        sb.append(f"total: {self.precioTotal}\n")
        
        return "".join(sb)
    @multimethod #usando el multimethod para simular cuando a eliminar producto no le entregamos una cantidad 
    def eliminarProducto(self,producto: Producto):
        indice=self.listaItems.index(producto)
        self.listaItems.pop(indice)
        self.cantidadPorProducto.pop(indice)
        return "proceso exitoso"
    @multimethod
    def eliminarProducto(self, producto : Producto , cantidad: int):#aqui usamos el multimethos para simular cuando si le entregamos alguna cantidad 
        indice = self. listaItems.index(producto)
        cantidadproducto= self.cantidadPorProducto[indice]
        if cantidadproducto > cantidad:
            self.cantidadPorProducto[indice]-=cantidad
            return f"La cantidad del producto ahora es {self.cantidadPorProducto[indice]}"
        elif cantidadproducto==cantidad:
            self.cantidadPorProducto.pop(indice)
            self.listaItems.pop(indice)
            return f"El producto ha sido eliminado en su totalidad"
        else:
            return "ERROR: la cantidad que deseas eliminar es mayor que la disponible "


