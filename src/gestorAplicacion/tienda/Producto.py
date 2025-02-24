from enum import Enum

class Producto:

    class Categoria(Enum):
        TECNOLOGIA = "Tecnologia"
        ASEO = "Aseo"
        COMIDA = "Comida"
        PAPELERIA = "Papeleria"
        JUGUETERIA = "Jugueteria"
        DEPORTES = "Deportes"


    def __init__(self, cantidad, cantidadAlerta, cantidadVendida, cantidadDevuelta, categoria, ID, nombre, precio, retornable):
        self.cantidad = cantidad
        self.cantidadAlerta = cantidadAlerta
        self.cantidadVendida = cantidadVendida
        self.cantidadDevuelta = cantidadDevuelta
        self.categoria = categoria
        self.ID = ID
        self.nombre = nombre
        self.precio = precio
        self.retornable = retornable

    def getCantidad(self):
        return self.cantidad
    def setCantidad(self, value):
        self.cantidad = value
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getCategoria(self):
        return self.categoria
    
    def getPrecio(self):
        return self.precio
    def getID(self):
        return self.ID
    def setPrecio(self, precio):
        self.precio=precio
    
    def getCantidadVendida(self):
        return self.cantidadVendida
    def setCantidadVendida(self, value):
        self.cantidadVendida = value
    
    def setCantidadDevuelta(self, cantidadDevuelta):
        self.cantidadDevuelta = cantidadDevuelta

    def getCantidadDevuelta(self):
        return self.cantidadDevuelta

    
    def verificarCantidadProductos(self):
        if self.cantidad <= self.cantidadAlerta:
            return True
        return False
    def aplicardescuento(self, producto  , descuento ): #este es el metodo encargado de hacer los productos mas baratos 
        resta= producto.getPrecio()*descuento # cantidad del descuento 
        final=producto.getPrecio()-resta # precio final del producto 
        producto.setPrecio(final)
        return resta

    def registrar_venta(self, cantidad):
        self.cantidad_vendida += cantidad
        self.cantidad -= cantidad

    def reabastecer_cantidad(self, cantidad):
        self.cantidad += cantidad

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

    def __str__(self):
       return f"Producto seleccionado: {self.nombre}\n \
                ID: {self.ID}\n \
                Retornable: {'Sí' if self.retornable else 'No'}\n \
                Categoría: {self.categoria.value} \n \
                Precio: {self.precio}\n \
                Cantidad disponible: {self.cantidad}"
    def otrostr(self):
        return self.nombre
    
    def isRetornable(self):
        return self.retornable
    
    #Necesario para las recomendaciones
    @classmethod
    def getListaCategorias(cls):
        return list(Producto.Categoria)

        