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
        self.descuentoPorproductos= 0
    @multimethod  
    def __init__(self):
        return
    def getInventario(self):
        return self.inventario
    def setInventario(self, inventario):
        self.inventario=inventario
    
    def getUsuario(self): #getters
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
    def buscarProductoMaseconomico(self):
        maseconomico=None

        for producto in self.listaItems:
            if maseconomico== None or (producto.getPrecio() < maseconomico.getPrecio()):
                maseconomico=producto
        return maseconomico
    def calcularTotal(self):
        for i in range(len(self.listaItems)):
            self.precioTotal += self.listaItems[i].getPrecio() * self.cantidadPorProducto[i]
        
        if self.descuentoAplicadoCompra != 0:
      
          self.precioTotal -= self.precioTotal * (self.descuentoAplicadoCompra / 100)
    @multimethod # en este metodo solo entregamos el producto y se asume cantidad por default : 1
    def añadirProducto(self, producto : Producto):
        #Si no se le pasa cantidad, se asume que se quiere añadir un producto
        estado = self.inventario.verificarProducto(producto, 1)# estado hace referencia a la verificacion del producto en el inventario
        #despues de la verificacion seguimos con :
        if estado == True:
            #aqui revisamos si el producto ya estaba en el carrito , para saber si se añade la referencia o si solamente se le aumenta a la cantidad 
            if producto in self.listaItems:
                #si el producto ya estaba en el carrito y queremos modificar la cantidad:
                indice = self.listaItems.index(producto)
                cantidad = self.cantidadPorProducto[indice]
                if cantidad == 0:# si la cantidad entregada es inválida 
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
    @multimethod # en este metodo entregamos el producto y su cantidad a añadir 
    def añadirProducto(self, producto : Producto , cantidadAñadir : int):
        estado = self.inventario.verificarProducto(producto, cantidadAñadir) #misma verificacion del producto que arriba 
        if estado == True: # si estado == true quiere decir que se cumplieron todas las verificaciones
                if cantidadAñadir > 5: #la cantidad maxima que se puede añadir son cinco
                    return "Error. La cantidad máxima de productos que se puede añadir es 5"
                elif producto in self.listaItems:
                    indice = self.listaItems.index(producto)# el producto ya esta en el carrito y solamente queremos modificar sus cantidades
                    cantidad = self.cantidadPorProducto[indice]
                    if (cantidad + cantidadAñadir) > 5:
                        return "Error. La cantidad máxima de productos que se puede añadir es 5"# cuando vamos a modificar la cantidad, la suma da mas que 5
                    else:
                        self.cantidadPorProducto.insert(indice, cantidad + cantidadAñadir)#cuando no se pasa de cinco solamente sumamos 
                        return "Producto añadido al carrito exitosamente"
                else: # si el producto no esta en el carrito, añadimos referencia y cantidad
                    self.listaItems.append(producto)# lista que lleva las referencias 
                    self.cantidadPorProducto.append(cantidadAñadir) # lista que lleva las cantidades 
                    return "Producto añadido al carrito exitosamente"
        else:
                return "No hay suficiente producto en stock" # no se cumplio la verificacion del inventario 

    def restarProductosAlComprar(self):
        contador =0
        self.usuario.setVecesComprado(1)
        Usuario=self.usuario
        suma=0  # recorremos la lista de las cantidades del usuario para empezar a añadirle puntos con respecto a esto
        for numero in self.cantidadPorProducto:
            suma+=numero
        if suma <= 5:
            contador+=1 #le estamos dando puntos al usuario segun la cantidad de cosas que esté comprando
        elif suma > 5 and suma <= 10:
            contador+=2
        elif suma > 10 and suma <= 15:
            contador+=4
        else:
            contador+=6
        Usuario.setPuntos(contador)

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
        sb.append(f"Carrito de {self.usuario.getNombre()}:\n\n")
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
#funcionalidad de descuentos 
    def verificardescuentopuntos(self ): #aqui vamos a verificar los descuentos del usuario por los puntos que se ha ganado en nuestra tienda 
        puntos= self.usuario.getPuntos() #obtenemos los puntos del usuario 
        descuento=0.0 #variable que va a llevar el descuento
        if puntos > 5 and puntos <10: 
            descuento=0.05
            self.descuentoAplicadoCompra=self.descuentoAplicadoCompra+(self.precioTotal*descuento) #se hace el calculo de cuanto es el descuento y se añade a la variable en la que llevamos esta cuenta
            self.precioTotal=self.precioTotal-self.descuentoAplicadoCompra #se hace el cambio en el precio 
            self.usuario.setPuntos(0) # debemos dejar los puntos del usuario de nuevo en ceros para no tener errores en las cuentas 

            return f"Gracias a tu fidelidad obtuviste un descuento de  {self.descuentoAplicadoCompra}   usando tus puntos"
        #todo lo que viene debajo es totalmente igual a cuando los puntos estaban entre cinco y diez, la unica excepcion es que el descuento aumenta proporcional a los puntos 
        elif puntos >= 10 and puntos < 20:
            descuento=0.10
            self.descuentoAplicadoCompra=self.descuentoAplicadoCompra+(self.precioTotal*descuento)
            self.precioTotal=self.precioTotal-self.descuentoAplicadoCompra
            self.usuario.setPuntos(0)

            return f"Gracias a tu fidelidad obtuviste un descuento de  {self.descuentoAplicadoCompra} usando tus puntos"
        elif puntos >=20 and puntos <30:
            descuento=0.15
            self.descuentoAplicadoCompra=self.descuentoAplicadoCompra+(self.precioTotal*descuento)
            self.precioTotal=self.precioTotal-self.descuentoAplicadoCompra
            self.usuario.setPuntos(0)

            return f"Gracias a tu fidelidad obtuviste un descuento de  {self.descuentoAplicadoCompra}  usando tus puntos"
        elif puntos >= 30:
            descuento=0.20
            self.descuentoAplicadoCompra=self.descuentoAplicadoCompra+(self.precioTotal*descuento)
            self.precioTotal=self.precioTotal-self.descuentoAplicadoCompra
            self.usuario.setPuntos(0)

            return f"Gracias a tu fidelidad obtuviste un descuento de  {self.descuentoAplicadoCompra}  usando tus puntos"
        else:
            return None
    #este es el descuento por la membresia que adquiere el cliente al comprar en la tienda 
    def descuentomembresia(self ):
        membresia=self.usuario.getMembresia()
        vecescomprado=self.usuario.getVecesComprado()
        if membresia==None:# esta es la logica en caso de que el usuario no poseyera membresia, esta es mas grande en cuanto a obsequios ya que es la primera vez del usuario
            if vecescomprado >= 3 and vecescomprado <6:
                self.usuario.setMembresia("Bronce")#membresia bronce 
                economico=self.inventario.buscarProductoMaseconomico()
                for producto in self.listaItems:#el producto mas barato del inventario
                    if producto == economico: 
                        descuento = producto.aplicardescuento(producto, 0.05)
                        self.descuentoPorproductos+= descuento
                        return f"Felicidades, ahora eres miembro bronce, por esto recibes un descuento de {descuento} en el producto {producto.getNombre()}"
                economico = self.buscarProductoMaseconomico()
                for producto in self.listaItems:#el mas barato del carrito en caso de que no tenga el mas barato de inventario
                    if producto==economico:
                        descuento=producto.aplicardescuento(producto,0.05)
                        self.descuentoPorproductos+=descuento
                        return f"Felicidades, ahora eres miembro bronce, por esto recibes un descuento de {descuento} en el producto {producto.getNombre()}"
            elif vecescomprado >=6 and vecescomprado< 12:
                self.usuario.setMembresia("Oro")#cuando el usuario es oro se le regala un producto 
                economico=self.inventario.buscarProductoMaseconomico()
                self.añadirProducto(economico,1)
                for producto in self.listaItems:
                    if producto == economico:
                        descuento = producto.aplicardescuento(producto, 1)
                        self.descuentoPorproductos+= descuento
                        return f"Felicidades, ahora eres miembro Oro, por esto recibes un obsequio de {producto.getNombre()} totalmente gratis "
            elif vecescomprado > 12:
                self.usuario.setMembresia("Platino") #cuando el usuario es platino, se le da descuento y regalo
                descuento=0.07
                self.descuentoAplicadoCompra=self.descuentoAplicadoCompra+(self.precioTotal*descuento)
                self.precioTotal=self.precioTotal-self.descuentoAplicadoCompra
                economico=self.inventario.buscarProductoMaseconomico()
                self.añadirProducto(economico,1)
                for producto in self.listaItems:
                    if producto == economico:
                        descuento = producto.aplicardescuento(producto, 1)
                        self.descuentoPorproductos+= descuento
                        return f"Felicidades, ahora eres miembro Platino, por esto recibes un obsequio de {producto.getNombre()} totalmente gratis y un descuento de {self.descuentoAplicadoCompra} en tu compra"
        elif membresia== "Bronce": #aqui esta la logica por si el usuario si posee membresía , es decir, no es su primera vez
           
            if len(self.listaItems) > 10:  # El usuario posee membresía y está llevando al mayoreo
                economico1 = self.buscarProductoMaseconomico()  # Aquí el más barato del carrito del cliente
                
                for producto in self.listaItems:
                    if producto == economico1:
                        descuento = producto.aplicardescuento(producto, 0.05)
                        self.descuentoPorproductos += descuento
                        retorno = self.getPrecioTotal() * 0.02
                        self.usuario.getCuentaBancaria().recargarCuenta(retorno)  # El retorno del dinero no se resta del carrito
                        
                        return "Por ser un cliente Bronce y llevar una compra mayorista hoy te daremos un descuento de " + str(descuento) + " en el producto " + producto.getNombre() + " y un reembolso del 0.02 para la rentabilidad"

            elif len(self.listaItems) < 10:  # El usuario solo posee membresía y no lleva al mayoreo
                economico1 = self.buscarProductoMaseconomico()  # Aquí el más barato del carrito del cliente
                
                for producto in self.listaItems:
                    if producto == economico1:
                        descuento = producto.aplicardescuento(producto, 0.02)
                        self.descuentoPorproductos += descuento
                        return "Por ser un cliente Bronce hoy te daremos un descuento de " + str(descuento) + " en el producto " + producto.getNombre()

            elif self.usuario.getMembresia() == "Oro":
                if len(self.listaItems) > 10:  # El usuario posee membresía y está llevando al mayoreo
                    economico1 = self.buscarProductoMaseconomico()
                    
                    for producto in self.listaItems:
                        if producto == economico1:
                            descuento = producto.aplicardescuento(producto, 0.10)
                            self.descuentoPorproductos += 1
                            retorno = self.getPrecioTotal() * 0.04
                            self.usuario.getCuentaBancaria().recargarCuenta(retorno)
                            
                            return "Por ser un cliente Oro y llevar una compra mayorista hoy te daremos un descuento de " + str(descuento) + " en el producto " + producto.getNombre() + " y un reembolso del 0.04 para la rentabilidad"

                elif len(self.listaItems) < 10:  # El usuario solo posee membresía y no lleva al mayoreo
                    economico1 = self.buscarProductoMaseconomico()
                    
                    for producto in self.listaItems:
                        if producto == economico1:
                            descuento = producto.aplicardescuento(producto, 0.05)
                            self.descuentoPorproductos += descuento
                            return "Por ser un cliente Oro hoy te daremos un descuento de " + str(descuento) + " en el producto " + producto.getNombre()

            elif self.usuario.getMembresia() == "Platino":
                if len(self.listaItems) > 10:  # El usuario posee membresía y está llevando al mayoreo
                    economico1 = self.buscarProductoMaseconomico
                    
                    for producto in self.listaItems:
                        if producto == economico1:
                            descuento = producto.aplicardescuento(producto, 0.15)
                            self.descuentoPorproductos += descuento
                            retorno = self.getPrecioTotal() * 0.067
                            self.usuario.getCuentaBancaria().recargarCuenta(retorno)
                            
                            return "Por ser un cliente Platino y llevar una compra mayorista hoy te daremos un descuento de " + str(descuento) + " en el producto " + producto.getNombre() + " y un reembolso del 0.067 para la rentabilidad"

                elif len(self.listaItems) < 10:  # El usuario solo posee membresía y no lleva al mayoreo
                    economico1 = self.buscarProductoMaseconomico
                    
                    for producto in self.listaItems:
                        if producto == economico1:
                            descuento = producto.aplicardescuento(producto, 0.10)
                            self.descuentoPorproductos += 1
                            return "Por ser un cliente Platino hoy te daremos un descuento de " + str(descuento) + " en el producto " + producto.getNombre()

            return None
    def descuentoporproductomenosvendido(self):
        ProductoMenosVendido=self.inventario.buscarProductoMenosVendido()
        for producto in self.listaItems:
            if producto== ProductoMenosVendido:
                descuento=producto.aplicardescuento(producto,0.10)
                self.descuentoPorproductos+=descuento
                return f"Por impulso de producto has obtenido un descuento de {descuento} en el producto {producto.getNombre()}" 
    def 