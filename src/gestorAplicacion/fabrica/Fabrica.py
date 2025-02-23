from gestorAplicacion.fabrica.Trabajador import Trabajador

class Fabrica:
    def __init__(self, inventario):
        self.trabajadores = [Trabajador(i, f"Trabajador {i}", "08:00-20:00") for i in range(1, 101)]
        self.ordenes_pendientes = []
        self.inventario = inventario


    def get_ordenes_pendientes(self):
        return self.ordenes_pendientes

    def recibir_orden(self, productos, cantidades):
        orden = [productos, cantidades]

        trabajadores_requeridos = self.calcular_trabajadores_requeridos(cantidades)
        if self.asignar_trabajadores(trabajadores_requeridos):
            self.ordenes_pendientes.append(orden)
            self.liberar_trabajadores(trabajadores_requeridos)
            return f"Orden de fabricación recibida.\n{self.entregar_productos(productos, cantidades)}"
        else:
            return "No hay suficientes trabajadores disponibles para procesar esta orden."

    def entregar_productos(self, productos, cantidades):
        productos_fabricados = {producto: cantidad for producto, cantidad in zip(productos, cantidades)}
        self.inventario.recibirProductosFabricados(productos_fabricados)
        return "Le mandaremos un correo cuando se entreguen sus productos"

    def asignar_trabajadores(self, trabajadores_requeridos):
        asignados = 0
        for trabajador in self.trabajadores:
            if trabajador.get_estado() == "Disponible" and asignados < trabajadores_requeridos:
                trabajador.set_estado("Ocupado")
                asignados += 1
            if asignados == trabajadores_requeridos:
                return True  
        return False  

    def liberar_trabajadores(self, trabajadores_liberar):
        liberados = 0
        for trabajador in self.trabajadores:
            if trabajador.get_estado() == "Ocupado" and liberados < trabajadores_liberar:
                trabajador.set_estado("Disponible")
                liberados += 1
            if liberados == trabajadores_liberar:
                break  

    def calcular_trabajadores_requeridos(self, cantidades):
        trabajadores_por_unidad = 2  
        cantidad_total = sum(cantidades)
        return cantidad_total * trabajadores_por_unidad

    def get_vendedor(self):
        return self.vendedor

    def set_vendedor(self, value):
        self.vendedor = value
