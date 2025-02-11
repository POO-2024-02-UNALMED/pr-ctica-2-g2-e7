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
                self.cantidadTecnologia += factura.getCarritoCompras().getCantidadPorProductos().get(factura.getCarritoCompras().getListaItems().index(producto))
            if categoria == Producto.Categoria.ASEO: 
                self.cantidadAseo += factura.getCarritoCompras().getCantidadPorProductos().get(factura.getCarritoCompras().getListaItems().index(producto))
            if categoria == Producto.Categoria.COMIDA:
                self.cantidadComida += factura.getCarritoCompras().getCantidadPorProductos().get(factura.getCarritoCompras().getListaItems().index(producto))
            if categoria == Producto.Categoria.PAPELERIA:
                self.cantidadPapeleria += factura.getCarritoCompras().getCantidadPorProductos().get(factura.getCarritoCompras().getListaItems().index(producto))
            if categoria == Producto.Categoria.JUGUETERIA:
                self.cantidadJugueteria += factura.getCarritoCompras().getCantidadPorProductos().get(factura.getCarritoCompras().getListaItems().index(producto))
            if categoria == Producto.Categoria.DEPORTES:
                self.cantidadDeportes += factura.getCarritoCompras().getCantidadPorProductos().get(factura.getCarritoCompras().getListaItems().index(producto))

    def actualizarCategoriasMasCompradas(self):
        #Se crea una lista con las cantidades compradas
        cantidadesOrdenadas = [self.cantidadTecnologia, self.cantidadAseo, self.cantidadComida, self.cantidadPapeleria, self.cantidadJugueteria, self.cantidadDeportes]

        #Se crea una lista con las categorias
        categoriasOrdenadas = list(Producto.Categoria)

        #Ordenar ambas listas manteniendo la correspondencia entre índices

        for i in range (0, len(cantidadesOrdenadas)):
            for j in range (1, len(cantidadesOrdenadas)):
                if cantidadesOrdenadas[j] > cantidadesOrdenadas[i]:
                    #Intercambiar cantidades
                    tempCantidad = cantidadesOrdenadas[i]
                    cantidadesOrdenadas[i] = cantidadesOrdenadas[j]
                    cantidadesOrdenadas[j] = tempCantidad

                    #Intercambiar categorías para mantener correspondencia
                    tempCategoria = categoriasOrdenadas[i]
                    categoriasOrdenadas[i] = categoriasOrdenadas[j]
                    categoriasOrdenadas[j] = tempCategoria
        pass

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