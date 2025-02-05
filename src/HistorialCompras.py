class HistorialCompras:
    facturas = []

    def getFacturas(self):
        return self.facturas
    
    def agregarFactura(self, factura):
        self.facturas.append(factura)