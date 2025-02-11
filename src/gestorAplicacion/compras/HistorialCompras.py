from ..tienda.Producto import Producto
from ..pasarelaPago import Factura

class HistorialCompras:
    
    def __init__(self):
        self.facturas = []
        self.cantidadDevueltos = 0

        self.cantidadTecnologia = 0
        self.cantidadAseo = 0
        self.cantidadComida = 0
        self.cantidadPapeleria = 0
        self.cantidadJugueteria = 0
        self.cantidadDeportes = 0

        self.caegoriasMasCompradas = []


    def getFacturas(self):
        return self.facturas
    
    def agregarFactura(self, factura):
        self.facturas.append(factura)

    def buscarFactura(self, id_factura):
        for factura in self.facturas:
            if factura.getIDFactura() == id_factura:
                return factura
        return None

    def mostrar_factura(self):
        factura_str = ""
        for factura in self.facturas:
            factura_str += f"ID factura: {factura.getIDFactura()}\n"
            factura_str += "{:<20} {:<20} {:<20}\n".format("Producto", "Cantidad", "ID Producto")
            for i in range(len(factura.getCarritoCompras().getListaItems())):
                item = factura.getCarritoCompras().getListaItems()[i]
                cantidad = factura.getCarritoCompras().getCantidadPorProducto()[i]
                factura_str += "{:<20} {:<20} {:<20}\n".format(item.getNombre(), cantidad, item.getID())
            factura_str += f"\nPrecio Total de la Compra: {factura.getCarritoCompras().getPrecioTotal()}\n\n"
        return factura_str

    def mostrar_factura_por_id(self, id_factura):
        factura = self.facturas[id_factura - 1]
        mensaje = ""
        mensaje += "{:<15} {:<15}\n".format("Producto", "Cantidad")
        for i in range(len(factura.getCarritoCompras().getListaItems())):
            item = factura.getCarritoCompras().getListaItems()[i]
            cantidad = factura.getCarritoCompras().getCantidadPorProducto()[i]
            mensaje += "{:<15} {:<15}\n".format(item.getNombre(), cantidad)
        mensaje += f"\nPrecio Total de la Compra: {factura.getCarritoCompras().getPrecioTotal()}\n"
        return mensaje

    def actualizarCantidadDevueltos(self, cantidad):
        self.cantidadDevueltos += cantidad

    def actualizarCantidadesCompradas(self, factura):
        categoria = None

        for producto in factura.getCarritoCompras().getListaItems():
            categoria = producto.getCategoria()

            if categoria == Producto.Categoria.TECNOLOGIA:
                pass
            #Trabajo en proceso ;)

    def getCantidadTecnologia(self):
        return self.cantidadTecnologia

    def getCantidadAseo(self):
        return self.cantidadAseo
    
    def getCantidadComida(self):
        return self.cantidadComida
    
    def getCantidadPapeleria(self):
        return self.cantidadPapeleria
    
    def getCantidadJugueteria(self):
        return self.cantidadJugueteria
    
    def getCantidadDeportes(self):
        return self.cantidadDeportes