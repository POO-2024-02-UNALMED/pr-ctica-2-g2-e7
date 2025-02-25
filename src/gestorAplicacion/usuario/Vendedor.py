from .Usuario import Usuario
from tkinter import simpledialog
from gestorAplicacion.usuario.Notificacion import Notificacion
from multimethod import multimethod

ordenes_pendientes = []
class Vendedor(Usuario):
    @multimethod
    def __init__(self, nombre, cuentaBancaria, inventario, fabrica):
        super().__init__(nombre, cuentaBancaria)
        self.ventasRealizadas = 0
        self.inventario = inventario
        self.fabrica = fabrica
    @multimethod
    def __init__(self,nombre,cuenta,inventario,fabrica,ventas):
        self.__init__(nombre,cuenta,inventario,fabrica)
        self.ventasRealizadas=ventas


    def crear_orden_fabricacion(self):
        productos_seleccionados = []
        cantidades = []

        while True:
            nombre_producto = simpledialog.askstring("Entrada", "Ingrese el nombre del producto:")
            if not nombre_producto:
                return "No se ingresó ningún producto."
            if nombre_producto.lower() == "fin":
                break

            producto = self.buscarProducto(nombre_producto)
            if producto is None:
                return f"Producto no encontrado: {nombre_producto}\nPor favor vuelva a ingresar todos los productos de nuevo"

            entrada_cantidad = simpledialog.askinteger("Cantidad", "Ingrese la cantidad a fabricar:")
            if  entrada_cantidad  <= 0:
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
        if len(ordenes_pendientes) > 0:
            mensaje_fabrica_notif = "Se han entregado los productos"
            asunto_vendedor = "Orden De Producción"
            self.recibirNotificacion(mensaje_fabrica_notif, asunto_vendedor)
            ordenes_pendientes.clear()

        mensaje_fabrica = self.fabrica.recibir_orden(productos_seleccionados, cantidades)
        return f"Orden creada con éxito. Productos seleccionados: {len(productos_seleccionados)}.\n{mensaje_fabrica}"

    def buscarProducto(self, nombre):
        for producto in self.inventario.productosTotal:
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
        return ordenes_pendientes

    def actualizar_estado_orden(self, orden):
        if orden in ordenes_pendientes:
            ordenes_pendientes.remove(orden)