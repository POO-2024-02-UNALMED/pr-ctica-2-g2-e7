class HistorialCompras:
    
    def __init__(self):
        self.facturas = []

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
                factura_str += "{:<20} {:<20} {:<20}\n".format(item.getNombre(), cantidad, cantidad)
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