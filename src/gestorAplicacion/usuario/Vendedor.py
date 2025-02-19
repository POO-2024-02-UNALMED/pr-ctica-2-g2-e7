from .Usuario import Usuario

class Vendedor(Usuario):
    def __init__(self, nombre, cuentaBancaria, inventario, fabrica):
        super().__init__(nombre, cuentaBancaria)
        self.ventasRealizadas = 0
        self.inventario = inventario
        self.fabrica = fabrica

    def crear_orden_fabricacion(self):
        productos_seleccionados = []
        cantidades = []
        ordenes_pendientes = []

        while True:
            nombre_producto = input().strip()
            if nombre_producto.lower() == "fin":
                break

            producto = self.buscarProducto(nombre_producto)
            if producto is None:
                return f"Producto no encontrado: {nombre_producto}\nPor favor vuelva a ingresar todos los productos de nuevo"

            entrada_cantidad = input().strip()
            if not entrada_cantidad.isdigit() or int(entrada_cantidad) == 0:
                return "Cantidad inválida.\nVuelva a ingresar todos los productos nuevamente con una cantidad válida"

            cantidad = int(entrada_cantidad)

            productos_seleccionados.append(producto)
            cantidades.append(cantidad)
            orden = [productos_seleccionados[:], cantidades[:]]  # Copia de listas para evitar referencias mutables
            ordenes_pendientes.append(orden)

            if cantidad > 50:
                ordenes_pendientes.clear()

        if not productos_seleccionados:
            return "No se seleccionaron productos. La orden no se creó."

        mensaje_fabrica = self.fabrica.recibir_orden(productos_seleccionados, cantidades)
        return f"Orden creada con éxito. Productos seleccionados: {len(productos_seleccionados)}.\n{mensaje_fabrica}"

    def buscarProducto(self, nombre):
        for producto in self.inventario.getProductosTotal():
            if producto.getNombre() == nombre:
                return producto
        return None
    
    def devolucionDinero(self, usuarioReceptor, precioProducto, descuento, cantidadRetornar):
        valorDevolver = 0
        if(descuento > 0):
            precioConDescuento = precioProducto - (precioProducto * (descuento / 100.0))
            valorDevolver = (precioConDescuento - (precioConDescuento * 0.1)) * cantidadRetornar
        else:
            valorDevolver = (precioProducto - (precioProducto * 0.1)) * cantidadRetornar
        
        super().pago(self, usuarioReceptor, valorDevolver, "devolución")
        return valorDevolver
    
    def reingresarProducto(self, cantidad, producto):
        self.inventario.reabastecerProductos(cantidad, producto)

    def consultarCuentaBancaria(self):
        return f"Estado de tu cuenta bancaria:\nSaldo: {self.cuentaBancaria.getSaldo()}"
    
    def get_ordenes_pendientes(self):
        return self.ordenes_pendientes

    def actualizar_estado_orden(self, orden):
        if orden in self.ordenes_pendientes:
            self.ordenes_pendientes.remove(orden)