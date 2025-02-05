from enum import Enum

class Producto:
    cantidad = 0
    cantidadDevuelta = 0
    cantidadVendida = 0
    cantidadAlerta = 0
    categoria = None
    ID = 0
    nombre = ""
    precio = 0
    retornable = False


    class Categoria(Enum):
        TECNOLOGIA = "Tecnologia"
        ASEO = "Aseo"
        COMIDA = "Comida"
        PAPELERIA = "Papeleria"
        JUGUETERIA = "Jugueteria"
        DEPORTES = "Deportes"

        def __init__(self, nombre):
            self._nombre = nombre

        @property
        def getNombre(self):
            return self._nombre
        

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