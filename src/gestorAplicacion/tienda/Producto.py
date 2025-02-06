from enum import Enum

class Producto:

    class Categoria(Enum):
        TECNOLOGIA = "Tecnologia"
        ASEO = "Aseo"
        COMIDA = "Comida"
        PAPELERIA = "Papeleria"
        JUGUETERIA = "Jugueteria"
        DEPORTES = "Deportes"

        def __init__(self, nombre):
            self._nombre = nombre


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
    
    def getCategoria(self):
        return self.categoria
    
    def getPrecio(self):
        return self.precio