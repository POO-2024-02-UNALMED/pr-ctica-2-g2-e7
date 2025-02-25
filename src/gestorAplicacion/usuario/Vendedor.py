from .Usuario import Usuario
from tkinter import simpledialog
from gestorAplicacion.usuario.Notificacion import Notificacion

ordenes_pendientes = []
class Vendedor(Usuario):
    def __init__(self, nombre, cuentaBancaria, inventario, fabrica):
        super().__init__(nombre, cuentaBancaria)
        self.ventasRealizadas = 0
        self.inventario = inventario
        self.fabrica = fabrica

    def crear_orden_fabricacion(self, productos_seleccionados, cantidades):
        if not productos_seleccionados or not cantidades:
            return "No se ingresaron productos."

        orden = [productos_seleccionados[:], cantidades[:]]  # Copia de listas para evitar referencias mutables
        ordenes_pendientes.append(orden)

        if any(cantidad > 50 for cantidad in cantidades):
            ordenes_pendientes.clear()
            return "Se ingresó una cantidad mayor a 50. La orden ha sido cancelada."

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