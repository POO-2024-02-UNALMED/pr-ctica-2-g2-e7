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

        self.categoriasMasCompradas = [None, None, None]


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
        # (101, [("Laptop",1, 1, True), ("Mouse",2, 3, False)], "$1080"). (ESTE ES EL FORMATO DE RETORNO)
        lista_facturas = []
        for factura in self.facturas:
            lista_items = []
            for i in range(len(factura.getCarritoCompras().getListaItems())):
                item = factura.getCarritoCompras().getListaItems()[i]
                cantidad = factura.getCarritoCompras().getCantidadPorProducto()[i]
                lista_items.append((item.getNombre(),item.getID(), cantidad, item.isRetornable()))
            lista_facturas.append((factura.getIDFactura(), lista_items, factura.getCarritoCompras().getPrecioTotal()))
        return lista_facturas
    


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
                self.cantidadTecnologia += factura.getCarritoCompras().getCantidadPorProductos(producto)
            if categoria == Producto.Categoria.ASEO: 
                self.cantidadAseo += factura.getCarritoCompras().getCantidadPorProductos(producto)
            if categoria == Producto.Categoria.COMIDA:
                self.cantidadComida += factura.getCarritoCompras().getCantidadPorProductos(producto)
            if categoria == Producto.Categoria.PAPELERIA:
                self.cantidadPapeleria += factura.getCarritoCompras().getCantidadPorProductos(producto)
            if categoria == Producto.Categoria.JUGUETERIA:
                self.cantidadJugueteria += factura.getCarritoCompras().getCantidadPorProductos(producto)
            if categoria == Producto.Categoria.DEPORTES:
                self.cantidadDeportes += factura.getCarritoCompras().getCantidadPorProductos(producto)

    def actualizarCategoriasMasCompradas(self):
        # Lista con las cantidades compradas
        cantidadesOrdenadas = [self.cantidadTecnologia, self.cantidadAseo, self.cantidadComida, 
                            self.cantidadPapeleria, self.cantidadJugueteria, self.cantidadDeportes]

        # Lista con las categorías (asumo que Producto.Categoria es una lista/enum ordenada correctamente)
        categoriasOrdenadas = list(Producto.Categoria)

        # Aplicar Bubble Sort para ordenar ambas listas de mayor a menor
        n = len(cantidadesOrdenadas)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if cantidadesOrdenadas[j] < cantidadesOrdenadas[j + 1]:  # Orden descendente
                    # Intercambiar cantidades
                    cantidadesOrdenadas[j], cantidadesOrdenadas[j + 1] = cantidadesOrdenadas[j + 1], cantidadesOrdenadas[j]

                    # Intercambiar categorías para mantener correspondencia
                    categoriasOrdenadas[j], categoriasOrdenadas[j + 1] = categoriasOrdenadas[j + 1], categoriasOrdenadas[j]
        
        for i in range(3):
            if cantidadesOrdenadas[i] != 0:
                self.categoriasMasCompradas[i] = categoriasOrdenadas[i]

        

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
    
    def getCategoriasMasCompradas(self):
        return self.categoriasMasCompradas