from ..tienda.Producto import Producto
import random

class Inventario:
    
    def __init__(self, categoriaTecnologia, categoriaAseo, categoriaComida, categoriaPapeleria, categoriaJugueteria, categoriaDeportes):
        self.categoriaTecnologia = categoriaTecnologia
        self.categoriaAseo = categoriaAseo
        self.categoriaComida = categoriaComida
        self.categoriaPapeleria = categoriaPapeleria
        self.categoriaJugueteria = categoriaJugueteria
        self.categoriaDeportes = categoriaDeportes
        self.productosTotal = []
        self.listaCategorias=[]
        self.listaCategorias.append(categoriaTecnologia)
        self.listaCategorias.append(categoriaAseo)
        self.listaCategorias.append(categoriaComida)
        self.listaCategorias.append(categoriaPapeleria)
        self.listaCategorias.append(categoriaJugueteria)
        self.listaCategorias.append(categoriaDeportes)

    def generar_reporte_por_categoria(self, nombre_categoria, categoria):
        reporte = []
        for producto in categoria:
            estado = f"Vendido: {producto.getCantidadVendida()} unidades" if producto.getCantidadVendida() > 0 else "No vendido"
            estado_dev = f"Devuelto {producto.getCantidadDevuelta()} unidades" if producto.getCantidadDevuelta() > 0 else "Sin devoluciones"

            reporte.append({
                "Categoría": nombre_categoria,
                "Nombre": producto.nombre,
                "Estado": estado,
                "Cantidad en stock": producto.cantidad,
                "Devoluciones": estado_dev
            })

        return reporte 
    
    def generar_reporte(self):
        reporte = []

        reporte.extend(self.generar_reporte_por_categoria("Tecnología", self.categoriaTecnologia))
        reporte.extend(self.generar_reporte_por_categoria("Aseo", self.categoriaAseo))
        reporte.extend(self.generar_reporte_por_categoria("Comida", self.categoriaComida))
        reporte.extend(self.generar_reporte_por_categoria("Papelería", self.categoriaPapeleria))
        reporte.extend(self.generar_reporte_por_categoria("Juguetería", self.categoriaJugueteria))
        reporte.extend(self.generar_reporte_por_categoria("Deportes", self.categoriaDeportes))

        return reporte

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
        elif nombreCategoria == "Jugueteria":
            for p in self.categoriaJugueteria:
                if (p.getNombre() == producto.getNombre()) and (p.getCantidad() >= unidades):
                    verificacion = True
                    break
        return verificacion
    
    def buscarProductoMaseconomico(self):
        maseconomico=None
        categorias= []
        categorias+=self.categoriaAseo+self.categoriaComida+self.categoriaDeportes+self.categoriaJugueteria+self.categoriaPapeleria+self.categoriaTecnologia
        for producto in categorias:
                if maseconomico== None or (producto.getPrecio()< maseconomico.getPrecio() and producto.getCantidad()>=1):
                    maseconomico = producto
        return maseconomico
    def buscarProductoMenosVendido(self):
        menosvendido=None
        categorias= []
        categorias+=self.categoriaAseo+self.categoriaComida+self.categoriaDeportes+self.categoriaJugueteria+self.categoriaPapeleria+self.categoriaTecnologia
        for producto in categorias:
                if menosvendido == None or (producto.getCantidadVendida()< menosvendido.getCantidadVendida() ) :
                    menosvendido = producto
        return menosvendido
    
    def reabastecerProductos(self, cantidad, producto):
        producto.setCantidadVendida(producto.getCantidadVendida() - cantidad)
        producto.setCantidadDevuelta(producto.getCantidadDevuelta() + cantidad)
        producto.reabastecer_cantidad(cantidad)

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

    def buscarCategoria(self, nombre):
        if nombre == "Tecnologia":
            return self.categoriaTecnologia
        elif nombre == "Aseo":
            return self.categoriaAseo
        elif nombre == "Comida":
            return self.categoriaComida
        elif nombre == "Papeleria":
            return self.categoriaPapeleria
        elif nombre == "Jugueteria":
            return self.categoriaJugueteria
        elif nombre == "Deportes":
            return self.categoriaDeportes
    
    def ajusteProductos(self, producto, accion):
        categoriaNombre = producto.getCategoria().value
        categoria = self.buscarCategoria(categoriaNombre)

        for producto2 in categoria:
            if producto2.getID() == producto.getID():
                producto2.setCantidad(producto.getCantidad())
                producto2.setCantidadVendida(producto.getCantidadVendida())
                if accion == "devolucion":
                    producto2.setCantidadDevuelta(producto.getCantidadDevuelta())

    import random
    def recibirProductosFabricados(self, productos_fabricados):
        for producto, cantidad in productos_fabricados.items():
            producto.reabastecer_cantidad(cantidad)

    def crearCatalogo(self):
        # Creamos una matriz de 5x6 usando list comprehension
        catalogo = [[None] * 6 for _ in range(5)]

        for i in range(30):
            fila = i // 6  # Divide en filas (cada 6 elementos pasa a la siguiente fila)
            columna = i % 6  # Asegura que las columnas sean de 0 a 5
        
            # Selecciona una categoría aleatoria (asegúrate de que tiene suficientes elementos)
            categoria = random.randint(0, 5)
        
            # Accede al elemento correspondiente dentro de la categoría
            indice = i - 16 if i >= 16 else i
            catalogo[fila][columna] = self.listaCategorias[categoria][indice]

        return catalogo
    
    def crearCatalogoRecomendaciones(self, historialCompra):
        
        # Creamos una matriz de 5x6 usando list comprehension
        catalogo = [[None] * 6 for _ in range(5)]

        categoriaRecomendada1 = None
        categoriaRecomendada2 = None
        categoriaRecomendada3 = None

        productosRecomendados1 = []
        productosRecomendados2 = []
        productosRecomendados3 = []

        categorias = 0
        #Revisa cuántas categorías hay almacenadas en categoriasMas compradas
        #ejemplo: puede que guarde [TECNOLOGIA, None, None] porque solo se han
        #comprado productos de la categoría TECNOLOGIA

        for i in range(3):
            if historialCompra.getCategoriasMasCompradas()[i] != None:
                categorias += 1
        


        if categorias == 1:

            categoriaRecomendada = historialCompra.getCategoriasMasCompradas()[0]
            productosRecomendados = self.listaCategorias[Producto.getListaCategorias().index(categoriaRecomendada)]

            for i in range (6):
                catalogo[0][i] = productosRecomendados[i]               
            
            #Se añaden los productos al resto de la matriz

            fila = 1
            columna = 0

            #Luego de agregar una fila de productos recomendados, quedan 24 espacios
            #disponibles para productos no recomendados

            for i in range(24):
                fila = i // 6  # Divide en filas (cada 6 elementos pasa a la siguiente fila)
                columna = i % 6  # Asegura que las columnas sean de 0 a 5

                categoria = random.randint(0, 5)
                indice = i - 16 if i >= 16 else i
                catalogo[fila+1][columna] = self.listaCategorias[categoria][indice]


            return catalogo, categorias
        
        if categorias == 2:
            categoriaRecomendada1 = historialCompra.getCategoriasMasCompradas()[0]
            categoriaRecomendada2 = historialCompra.getCategoriasMasCompradas()[1]

            productosRecomendados1 = self.listaCategorias[Producto.getListaCategorias().index(categoriaRecomendada1)]
            productosRecomendados2 = self.listaCategorias[Producto.getListaCategorias().index(categoriaRecomendada2)]

            for i in range (6):
                catalogo[0][i] = productosRecomendados1[i]
                catalogo[1][i] = productosRecomendados2[i]
            
            #Se añaden los productos al resto de la matriz

            fila = 2
            columna = 0

            #Luego de agregar dos filas de productos recomendados, quedan 18 espacios
            #disponibles para productos no recomendados

            for i in range(18):
                fila = i // 6
                columna = i % 6

                categoria = random.randint(0, 5)
                indice = i - 16 if i >= 16 else i
                catalogo[fila+2][columna] = self.listaCategorias[categoria][indice]
            
            return catalogo, categorias
        
        if categorias == 3:
            categoriaRecomendada1 = historialCompra.getCategoriasMasCompradas()[0]
            categoriaRecomendada2 = historialCompra.getCategoriasMasCompradas()[1]
            categoriaRecomendada3 = historialCompra.getCategoriasMasCompradas()[2]

            productosRecomendados1 = self.listaCategorias[Producto.getListaCategorias().index(categoriaRecomendada1)]
            productosRecomendados2 = self.listaCategorias[Producto.getListaCategorias().index(categoriaRecomendada2)]
            productosRecomendados3 = self.listaCategorias[Producto.getListaCategorias().index(categoriaRecomendada3)]

            for i in range (6):
                catalogo[0][i] = productosRecomendados1[i]
                catalogo[1][i] = productosRecomendados2[i]
                catalogo[2][i] = productosRecomendados3[i]
            
            #Se añaden los productos al resto de la matriz

            fila = 3
            columna = 0

            #Luego de agregar tres filas de productos recomendados, quedan 12 espacios
            #disponibles para productos no recomendados

            for i in range(12):
                fila = i // 6
                columna = i % 6

                categoria = random.randint(0, 5)
                indice = i - 16 if i >= 16 else i
                catalogo[fila+3][columna] = self.listaCategorias[categoria][indice]
            
            return catalogo, categorias

                
