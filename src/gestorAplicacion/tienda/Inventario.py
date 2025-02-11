from tienda.Producto import Producto

class Inventario:

    def __init__(self, categoriaTecnologia, categoriaAseo, categoriaComida, categoriaPapeleria, categoriaJugueteria, categoriaDeportes):
        self.categoriaTecnologia = categoriaTecnologia
        self.categoriaAseo = categoriaAseo
        self.categoriaComida = categoriaComida
        self.categoriaPapeleria = categoriaPapeleria
        self.categoriaJugueteria = categoriaJugueteria
        self.categoriaDeportes = categoriaDeportes
        self.productosTotal = []

    def verificarProducto(self, producto, unidades):
        categoria = producto.getCategoria()
        nombreCategoria = categoria.value
        verificacion = False 

        if nombreCategoria == "Tecnologia":
            for p in self.categoriaTecnologia:
                if (p.getNombre() == producto.getNombre()) and (p.getCantidad() >= unidades):
                    verificacion = True
                    break
        elif nombreCategoria == "Aseo":
            for p in self.categoriaAseo:
                if (p.getNombre() == producto.getNombre()) and (p.getCantidad() >= unidades):
                    verificacion = True
                    break
        elif nombreCategoria == "Comida":
            for p in self.categoriaComida:
                if (p.getNombre() == producto.getNombre()) and (p.getCantidad() >= unidades):
                    verificacion = True
                    break
        elif nombreCategoria == "Papeleria":
            for p in self.categoriaPapeleria:
                if (p.getNombre() == producto.getNombre()) and (p.getCantidad() >= unidades):
                    verificacion = True
                    break
        elif nombreCategoria == "Deportes":
            for p in self.categoriaDeportes:
                if (p.getNombre() == producto.getNombre()) and (p.getCantidad() >= unidades):
                    verificacion = True
                    break
        return verificacion
    
    def buscarProductoMaseconomico(self):
        maseconomico=None
        categorias= []
        categorias+=self.categoriaAseo+self.categoriaComida+self.categoriaDeportes+self.categoriaJugueteria+self.categoriaPapeleria+self.categoriaTecnologia
        for categoria in categorias:
            for producto in categoria:
                if maseconomico== None or (producto.getPrecio()< maseconomico.getPrecio() and producto.getCantidad()>=1):
                    maseconomico = producto
        return maseconomico
    def buscarProductoMenosVendido(self):
        menosvendido=None
        categorias= []
        categorias+=self.categoriaAseo+self.categoriaComida+self.categoriaDeportes+self.categoriaJugueteria+self.categoriaPapeleria+self.categoriaTecnologia
        for categoria in categorias:
            for producto in categoria:
                if menosvendido == None or (producto.getCantidadVendida()< menosvendido.getCantidadVendida() ) :
                    menosvendido = producto
        return menosvendido
    
    def reabastecerProductos(self, cantidad, producto):
        producto.setCantidadVendida(producto.getCantidadVendida() - cantidad)
        producto.setCantidadDevuelta(producto.getCantidadDevuelta() + cantidad)
        producto.reabastecerCantidad(cantidad)

    def añadirProducto(self, producto):
        self.productosTotal.append(producto)

        categoria = producto.getCategoria()

        if categoria == Producto.Categoria.TECNOLOGIA:
            self.categoriaTecnologia.append(producto)
        if categoria == Producto.Categoria.ASEO:
            self.categoriaAseo.append(producto)
        if categoria == Producto.Categoria.COMIDA:
            self.categoriaComida.append(producto)
        if categoria == Producto.Categoria.PAPELERIA:
            self.categoriaPapeleria.append(producto)
        if categoria == Producto.Categoria.JUGUETERIA:
            self.categoriaJugueteria.append(producto)
        if categoria == Producto.Categoria.DEPORTES:
            self.categoriaDeportes.append(producto)