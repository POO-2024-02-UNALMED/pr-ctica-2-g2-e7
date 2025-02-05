from Comprador import Comprador
from CuentaBancaria import CuentaBancaria
from CarritoCompras import CarritoCompras

class MainMenu:
    comprador = None
    def __init__(self, comprador):
        self.comprador = comprador

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
                elif opcion == 5:
                    #Espacio para gestionar cupones
                    break
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
                                break
                        except ValueError:
                            print("ERROR. Ingrese un valor válido.")
                        break
                elif opcion == 2:
                    #Espacio para hacer el proceso
                    break
                elif opcion == 3:
                    print("Regresando al menú del comprador...")
                    break
                else:
                    print("ERROR. Por favor ingrese alguna de las opciones mostradas")
            except ValueError:
                print("ERROR. Ingrese una cantidad válida.")


if __name__ == "__main__":
    comprador = Comprador("Juan", None, None)
    cuenta = CuentaBancaria(comprador)
    comprador.setCuentaBancaria(cuenta)
    carrito = CarritoCompras(comprador)
    comprador.setCarritoCompras(carrito)
    test = MainMenu(comprador)
    test.display()