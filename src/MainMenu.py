from gestorAplicacion.usuario.Comprador import Comprador
from gestorAplicacion.pasarelaPago.CuentaBancaria import CuentaBancaria
from gestorAplicacion.compras.CarritoCompras import CarritoCompras
from gestorAplicacion.usuario.Notificacion import Notificacion

class MainMenu:
    def __init__(self, comprador, vendedor, inventario):
        self.comprador = comprador
        self.vendedor = vendedor
        self.inventario = inventario

    def display(self):
        while True:
                print("===== MENÚ PRINCIPAL =====")
                print("1. Menú Comprador")
                print("2. Menú Vendedor")
                print("3. Salir\n")
                try:
                    opcion = int(input("Seleccione una opción: "))
                    if opcion == 1:
                        self.buyerMenuDisplay()
                        break
                    elif opcion == 2:
                        #Espacio para el menú del vendedor
                        break
                    elif opcion == 3:
                        print("Saliendo del programa...")
                        break
                    else:
                        print("ERROR. Por favor ingrese alguna de las opciones mostradas")
                except ValueError:
                    print("ERROR. Ingrese un valor válido.")
    
    def buyerMenuDisplay(self):
        while True:
            print("===== MENÚ COMPRADOR =====")
            print("1. Gestionar Carrito/Ver Catálogo")
            print("2. Consultar cuenta bancaria")
            print("3. Realizar Devolución")
            print("4. Realizar Compra")
            print("5. Gestionar cupones")
            print("6. Ver historial de compras")
            print("7. Ver Notificaciones")
            print("8. Volver al Menú Principal\n")
            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    #Espacio para gestionar carrito/ver catálogo
                    break
                elif opcion == 2:
                    #Espacio para consultar cuenta bancaria
                    break
                elif opcion == 3:
                    #Espacio para realizar devolución
                    break
                elif opcion == 4:
                    if len(self.comprador.getCarritoCompras().getListaItems()) == 0:
                        print("\nERROR. No hay productos en el carrito.\n")
                    elif self.verificacionCompra() == False:
                        print("\nERROR. Saldo insuficiente para hacer la compra.")
                    else:
                        self.comprador.getCarritoCompras().calcularTotal()
                        self.buyProcessDisplay()
                elif opcion == 5:
                    self.voucherMenuDisplay()
                elif opcion == 6:
                    #Espacio para ver historial de compras
                    break
                elif opcion == 7:
                    #Espacio para ver notificaciones
                    break
                elif opcion == 8:
                    print("Volviendo al Menú Principal...")
                    break
                else:
                    print("ERROR. Por favor ingrese alguna de las opciones mostradas")
            except ValueError:
                print("ERROR.Ingrese un valor válido.")

    def verificacionCompra(self):
        self.comprador.getCarritoCompras().calcularTotal()
        precioCompra = self.comprador.getCarritoCompras().getPrecioTotal()
        saldoComprador = self.comprador.getCuentaBancaria().getSaldo()
        if precioCompra > saldoComprador:
            return False
        else:
            return True
        
    
    def buyProcessDisplay(self):
        while True:
            print("================")
            print("¿Desea usted aplicar un cupón de descuento en su compra?")
            print("1. Si")
            print("2. No")
            print("3. Regresar al menú del comprador")

            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    if len(self.comprador.getValorCupones()) == 0:
                        print("ERROR. No cuentas con cupones disponibles")
                    else:
                        print(f"Actualmente usted cuenta con {len(self.comprador.getValorCupones())} cuponesde descuento. Estos cupones son los siguientes:")
                        print(self.comprador.mostrarCupones()) #Se muestra por pantalla y en orden los cupones disponibles.

                        try:
                            cupon = int(input("Seleccione el cupón que usted desea aplicar: "))
                            if cupon > len(self.comprador.getValorCupones()) or cupon < 1:
                                print("ERROR. Por favor seleccione un cupón válido.")
                            else:
                                precioTotal = self.comprador.getCarritoCompras().getPrecioTotal() #Se obtiene el precio total de la compra (sin el descuento generado por el cupón).
                                descuento = self.comprador.getValorCupones()[cupon - 1] / 100 # Se calcula el descuento que se le aplicará al precio total de la compra.
                                precioConDescuento = precioTotal - (precioTotal * descuento) # Se calcula el precio total de la compra con el descuento aplicado.
                                self.comprador.getCarritoCompras().setDescuentoAplicadoCompra(cupon - 1) # guarda el descuento aplicado a la compra en el carrito de compras.

                                print(f"El precio total de la compra es de: {precioTotal}. Pero con descuento queda en: {precioConDescuento}. Ahora se prosigue con el pago.")
                                self.comprador.getCarritoCompras().setPrecioTotal(precioConDescuento) # Se actualiza el precio total de la compra en el carrito de compras.
                                self.comprador.getCarritoCompras().restarProductosAlComprar() # Se resta la cantidad de productos comprados a la cantidad total de productos.
                                
                                # Espacio para lo de las membresias (para que Santiago lo implemente)

                                self.comprador.pago(self.comprador, self.vendedor, precioConDescuento, "compra") #Se inicia el proceso de pago.
                                self.comprador.getValorCupones().pop(cupon - 1) # Se elimina el cupón de la lista de cupones.
                                self.comprador.cantidadCupones-= 1 # Se disminuye la cantidad de cupones en 1.
                                print("============COMPRA===========")
                                print("Resumen de la compra:")
                                print(self.comprador.getHistorialCompras().mostrar_factura_por_id(len(self.comprador.getHistorialCompras().getFacturas()))) # Se muestra por pantalla la factura.
                                print("¡Muchas gracias por su compra!")
                                if self.comprador.cantidadCupones != len(self.comprador.getValorCupones()):
                                    print(f"Felicidades. Durante la compra te ganaste un cupón del {self.comprador.getValorCupones()[self.comprador.cantidadCupones]} % de descuento para alguna compra en el futuro.")
                                    self.comprador.cantidadCupones += 1
                                print(f"Saldo restante en su cuenta: {self.comprador.getCuentaBancaria().getSaldo()}")
                                
                                notificacion = Notificacion(f"Se le informa que su compra por un valor de {self.comprador.getCarritoCompras().getPrecioTotal()} ha sido realizada con éxito.", "¡Compra realizada exitosamente!", self.comprador.getNombre())
                                self.comprador.recibirNotificacion(notificacion) # Se envía la notificacion al comprador.

                                notificacion2 = Notificacion(f"Se le informa que el usuario {self.comprador.getNombre()} ha realizado una compra por un valor de {self.comprador.getCarritoCompras().getPrecioTotal()}.", "Se le informa de una nueva compra", self.vendedor.getNombre())
                                self.vendedor.recibirNotificacion(notificacion2) # Se envía la notificacion al vendedor.

                                cantidadProductos = [] #Esta lista guarda la informacion de se hay productos por agotarse o no para luego enviar una notificación al vendedor.
                                for producto in self.comprador.getCarritoCompras().getListaItems():
                                    verificacion = producto.verificarCantidadProductos()
                                    cantidadProductos.append(verificacion)
                                    producto.setCantidadVendida(producto.getCantidadVendida() + self.comprador.getCarritoCompras().getCantidadPorProductos(producto))

                                for i in range(len(cantidadProductos)):
                                    if cantidadProductos[i] == True:
                                        notificacion3 = Notificacion(f"Se le informa que el producto {self.comprador.getCarritoCompras().getListaItems()[i].getNombre()} está por agotarse.", "Producto por agotarse", self.vendedor.getnombre())
                                        self.vendedor.recibirNotificacion(notificacion3) # Se envía la notificacion al vendedor.
                                
                                self.comprador.setCarritoCompras(CarritoCompras(self.comprador, self.inventario)) # Inicializar un nuevo carrito en forma de "vaciar" el ya existente.
                                break
                        except ValueError:
                            print("ERROR. Ingrese un valor válido.")
                        break
                elif opcion == 2:
                    self.comprador.getCarritoCompras().restarProductosAlComprar()
                    self.comprador.pago(self.comprador, self.vendedor, self.comprador.getCarritoCompras().getPrecioTotal(), "compra") #Se inicia el proceso de pago.

                    # Espacio para lo de las membresias (para que Santiago lo implemente)

                    print(f"El precio total de la compra es de: {self.comprador.getCarritoCompras().getPrecioTotal()}. Ahora se prosigue con el pago.")
                    print("============COMPRA===========")
                    print("Resumen de la compra:")
                    print(self.comprador.getHistorialCompras().mostrar_factura_por_id(len(self.comprador.getHistorialCompras().getFacturas()))) # Se muestra por pantalla la factura.
                    print("¡Muchas gracias por su compra!")
                    if self.comprador.cantidadCupones != len(self.comprador.getValorCupones()):
                        print(f"Felicidades. Durante la compra te ganaste un cupón del {self.comprador.getValorCupones()[self.comprador.cantidadCupones]} % de descuento para alguna compra en el futuro.")
                        self.comprador.cantidadCupones += 1
                    print(f"Saldo restante en su cuenta: {self.comprador.getCuentaBancaria().getSaldo()}")

                    notificacion = Notificacion(f"Se le informa que su compra por un valor de {self.comprador.getCarritoCompras().getPrecioTotal()} ha sido realizada con éxito.", "¡Compra realizada exitosamente!", self.comprador.getNombre())
                    self.comprador.recibirNotificacion(notificacion) # Se envía la notificacion al comprador.

                    notificacion2 = Notificacion(f"Se le informa que el usuario {self.comprador.getNombre()} ha realizado una compra por un valor de {self.comprador.getCarritoCompras().getPrecioTotal()}.", "Se le informa de una nueva compra", self.vendedor.getNombre())
                    self.vendedor.recibirNotificacion(notificacion2) # Se envía la notificacion al vendedor.

                    cantidadProductos = [] #Esta lista guarda la informacion de se hay productos por agotarse o no para luego enviar una notificación al vendedor.
                    for producto in self.comprador.getCarritoCompras().getListaItems():
                        verificacion = producto.verificarCantidadProductos()
                        cantidadProductos.append(verificacion)
                        producto.setCantidadVendida(producto.getCantidadVendida() + self.comprador.getCarritoCompras().getCantidadPorProductos(producto))

                    for i in range(len(cantidadProductos)):
                        if cantidadProductos[i] == True:
                            notificacion3 = Notificacion(f"Se le informa que el producto {self.comprador.getCarritoCompras().getListaItems()[i].getNombre()} está por agotarse.", "Producto por agotarse", self.vendedor.getNombre())
                            self.vendedor.recibirNotificacion(notificacion3) # Se envía la notificacion al vendedor.

                    self.comprador.setCarritoCompras(CarritoCompras(self.comprador, self.inventario)) # Inicializar un nuevo carrito en forma de "vaciar" el ya existente.
                    break
                elif opcion == 3:
                    print("Regresando al menú del comprador...")
                    break
                else:
                    print("ERROR. Por favor ingrese alguna de las opciones mostradas")
            except ValueError:
                print("ERROR. Ingrese una cantidad válida.")


    def voucherMenuDisplay(self):
        while True:
            print("===== MENÚ CUPONES =====")
            print(f"Usted actualmente dispone de {len(self.comprador.getValorCupones())} cupones. ¿Que desea hacer?:")
            print("1. Ver cupones disponibles")
            print("2. Eliminar cupones")
            print("3. Regresar al menú del comprador")
            try:
                opcion = int(input(("\nSeleccione una opción: ")))
                if opcion < 1 or opcion > 3:
                    print("ERROR. Seleccione una opción válida.")
                elif opcion == 1:
                    if len(self.comprador.getValorCupones()) == 0:
                        print("No cuentas con cupones disponibles de momento...")
                    else:
                        print(self.comprador.mostrarCupones())
                elif opcion == 2:
                    if len(self.comprador.getValorCupones()) == 0:
                        print("No cuentas con cupones disponibles para eliminar...")
                    else:
                        print("Cupones dispoibles:")
                        print(self.comprador.mostrarCupones())
                        try:
                            cuponEliminar = int(input("Seleccione el cupón que desea eliminar: "))
                            if cuponEliminar < 1 or cuponEliminar > len(self.comprador.getValorCupones()):
                                print("ERROR. Seleccione un cupón válido.")
                            else:
                                self.comprador.eliminarCupones(cuponEliminar)
                                self.comprador.cantidadCupones -= 1
                                print("El cupón ha sido eliminado exitosamente")
                        except ValueError:
                            print("ERROR. Ingrese un valor válido.")
                elif opcion == 3:
                    print("Regresando al menú del comprador...")
                    break
            except ValueError:
                print("ERROR. Ingrese un valor válido.")

