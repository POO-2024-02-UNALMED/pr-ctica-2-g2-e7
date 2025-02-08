class Inventario:
    def __init__(self, categoriaTecnologia, categoriaAseo, categoriaComida, categoriaPapeleria, categoriaJugueteria, categoriaDeportes):
        self.categoriaTecnologia = categoriaTecnologia
        self.categoriaAseo = categoriaAseo
        self.categoriaComida = categoriaComida
        self.categoriaPapeleria = categoriaPapeleria
        self.categoriaJugueteria = categoriaJugueteria
        self.categoriaDeportes = categoriaDeportes

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
