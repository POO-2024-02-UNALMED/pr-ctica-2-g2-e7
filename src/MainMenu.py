from gestorAplicacion.usuario.Comprador import Comprador
from gestorAplicacion.usuario.Vendedor import Vendedor
from gestorAplicacion.tienda.Producto import Producto
from gestorAplicacion.pasarelaPago.CuentaBancaria import CuentaBancaria
from gestorAplicacion.compras.CarritoCompras import CarritoCompras
from gestorAplicacion.usuario.Notificacion import Notificacion
from gestorAplicacion.tienda.Inventario import Inventario
from gestorAplicacion.fabrica.Fabrica import Fabrica
from excepciones.DatoNoExistenteError import DatoNoExistenteError
from excepciones.CantidadInvalidaError import CantidadInvalidaError
from multimethod import multimethod
from baseDatos.Serializador import serializar
from baseDatos.Deserializador import deserializar

class MainMenu:
    fila = None
    columna = None
    filas = ["1", "2", "3", "4", "5", "6"]
    columnas = ["A", "B", "C", "D", "E", "F"]
    def __init__(self, comprador = None, vendedor = None, inventario = None):
        if comprador is not None and vendedor is not None and inventario is not None:
            self.comprador = comprador
            self.vendedor = vendedor
            self.inventario = inventario
        else:
            deserializar(self)
    

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
                    elif opcion == 2:
                        self.sellerMenuDisplay()
                    elif opcion == 3:
                        print("Saliendo del programa...")
                        serializar(self)
                        break
                    else:
                        print("ERROR. Por favor ingrese alguna de las opciones mostradas")
                except ValueError:
                    print("ERROR. Ingrese un valor válido.")
    
    def cart_menu_display(self):
       
        opcion = 0

        while opcion != 4:
            print("===== MENÚ CARRITO =====")
            print("1. Agregar productos/ver Catálogo")
            print("2. Eliminar productos del carrito")
            print("3. Ver el carrito")
            print("4. Regresar")
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                if len(self.comprador.getHistorialCompras().getFacturas()) == 0:
                    catalogo = self.mostrar_catalogo(None, False)
                    self.recomendaciones = False
                    self.product_selection_process()
                else:
                    print("\nDesea actualizar las recomendaciones? 1. Sí - 2. No")
                    respuesta = int(input())
                    
                    if respuesta == 1:
                        catalogo = self.mostrar_catalogo(self.comprador.get_historial_compras(), False)
                        self.recomendaciones = True
                        self.product_selection_process()
                    elif respuesta == 2:
                        self.mostrar_catalogo(None, False)
                        self.recomendaciones = False
                        self.product_selection_process()
            
            elif opcion == 2:
                print("A continuación te mostraremos tu carrito para que elijas qué quieres eliminar")
                print(self.comprador.get_carrito_compras())
                
                eliminar = input("Por favor, ingresa el nombre del producto a eliminar: ")
                
                count = 0
                while True:
                    try:
                        count = int(input("Ahora ingresa la cantidad: "))
                        if count > 0:
                            break
                        else:
                            print("La cantidad debe ser mayor que 0.")
                    except ValueError:
                        print("Por favor, ingresa un número válido para la cantidad.")
                
                producto = self.comprador.get_carrito_compras().busqueda(eliminar)
                
                if producto is None:
                    print(f"El producto '{eliminar}' no se encuentra en el carrito.")
                else:
                    resultado = self.comprador.get_carrito_compras().eliminarproducto(producto, count)
                    print(resultado)
            
            elif opcion == 3:
                print(self.comprador.get_carrito_compras())
            
            elif opcion == 4:
                print("Volviendo al menú del carrito...")
    def eliminacion(self, producto, cantidad, comprador):
        
        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                raise CantidadInvalidaError("Cantidad Inválida")

        except CantidadInvalidaError as e:
            return str(e)
        except ValueError:
            return "La cantidad debe ser un número entero."

        # Verifica si la cantidad es mayor a 0
        if cantidad <= 0:
            return "La cantidad debe ser mayor que 0."

        # Busca el producto en el carrito de compras
        producto_obj = comprador.getCarritoCompras().busqueda(producto)

        if producto_obj is None:
            return f"El producto es inválido."
        else:
            resultado = comprador.getCarritoCompras().eliminarProducto(
                producto_obj, cantidad, comprador.getCarritoCompras().getListaItems(), comprador.getCarritoCompras().getCantidadPorProducto()
            )
            return resultado
                        
                
                       
                
            
      
    def productSelectionProcess(self):
        scanner = input

        llevar = "1"
        opcion = ""

        while True:
            print("\nIngrese las coordenadas del producto que desea \n\n"
                "Ingrese primero la fila (número) y luego la columna (letra) \n"
                "en la que se encuentra el producto deseado \n")

            opcion = scanner("Ingrese la fila para continuar o 0 para salir: ")

            if opcion == "0":
                break

            if opcion in self.filas:
                fila = opcion

                opcion = scanner("Ingrese la columna (en mayúscula) para continuar o 0 para salir: ")

                if opcion == "0":
                    break

                if opcion in self.columnas:
                    columna = opcion
                    productoSeleccionado = self.catalogo[int(fila)][self.columnas.index(columna) + 2]

                    print(f"Producto seleccionado: {productoSeleccionado.getNombre()}\n")

                    if self.recomendaciones:
                        # A partir de la segunda compra ya se tiene acceso al historial,
                        # por lo que se llama al método sobrecargado de productSelectionMenu
                        # que permite calificar los productos recomendados

                        retorno = self.productSelectionMenu(self.comprador.getHistorialCompras())

                        if not retorno:
                            break
                        else:
                            self.mostrar_Catalogo(self.comprador.getHistorialCompras(), False)
                            continue

                    else:
                        # En la primera compra no hay historial, por lo que no se pueden hacer recomendaciones

                        # Este método retorna un valor booleano dependiendo de la opción que se escoja,
                        # esto con el fin de saber si se debe volver al menú de selección de productos o
                        # al menú del carrito directamente
                        retorno = self.productSelectionMenu()

                        if not retorno:
                            break
                        else:
                            self.mostrar_Catalogo(None, False)
                            continue

                else:
                    print("Columna inválida, intente de nuevo")
                    continue

            else:
                print("Fila inválida, intente de nuevo")
                continue
    @multimethod
    def productSelectionMenu(self):
        # Si retorna True, se devuelve al menú de selección de productos 
        # Si no, vuelve al menú del carrito

        scanner = input
        opcion = 0

        while True:
            print("¿Qué desea hacer?")
            print("1. Agregar al carrito")
            print("2. Ver información del producto")
            print("3. Regresar/Seleccionar otro producto")
            opcion = scanner("Seleccione una opción: ")

            try:
                opcion = int(opcion)
            except ValueError:
                print("Opción inválida, intente de nuevo")
                continue

            if opcion == 1:
                llevar = scanner("Ingresa la cantidad a llevar (máximo 5): ")
                try:
                    numerico = int(llevar)
                    if numerico not in [1, 2, 3, 4, 5]:
                        llevar = "1"
                        print("Cantidad inválida, se te asignará una por default que es 1")
                except ValueError:
                    llevar = "1"
                    print("Entrada inválida, se asignará 1 por defecto")

                if self.productoSeleccionado.getCantidad() <= 0:
                    print("Error. No hay más productos disponibles.")
                    continue
                else:
                    mensaje = self.comprador.getCarritoCompras().añadirProducto(self.productoSeleccionado, int(llevar))
                    print(mensaje)
                    return False

            elif opcion == 2:
                print(self.productoSeleccionado.toStringdif())
                continue

            elif opcion == 3:
                return True

            else:
                print("Opción inválida, intente de nuevo")
                continue
    import random
    @multimethod
    def product_selection_menu(self,historial):
        """
        Menú de selección de productos.
        Si retorna True, se devuelve al menú de selección de productos.
        Si no, vuelve al menú del carrito.
        """

        opcion = ""
        llevar = ""

        categorias_a_recomendar = 0

        # Revisa cuántas categorías hay almacenadas en categorias_mas_compradas del historial.
        # Ejemplo: puede que guarde ["TECNOLOGIA", None, None] porque solo
        # se han comprado productos de la categoría "TECNOLOGIA".
        for i in range(3):
            if historial.get_categorias_mas_compradas()[i] is not None:
                categorias_a_recomendar += 1

        if categorias_a_recomendar == 1:

            while True:

                if self.fila == "1":
                    print("¿Qué te gustaría hacer?")
                    print("1. Agregar al carrito")
                    print("2. Ver información del producto")
                    print("3. Seleccionar otro producto")
                    print("4. Calificar recomendación")
                    opcion = input("Selecciona una opción: ")

                    if opcion == "1":
                        llevar = input("Ingresa la cantidad a llevar (máximo 5): ")
                        try:
                            numerico = int(llevar)
                            if numerico < 1 or numerico > 5:
                                llevar = "1"
                                print("Cantidad inválida, se te asignará una por defecto que es 1.")
                        except ValueError:
                            llevar = "1"
                            print("Entrada no válida, se asignará la cantidad por defecto: 1.")

                        if self.productoseleccionado.cantidad <= 0:
                            print("Error. No hay más productos disponibles.")
                            continue
                        else:
                            self.comprador.carrito_compras.añadir_producto(self.productoseleccionado, int(llevar))
                            print("Producto añadido correctamente.")
                            return False

                    elif opcion == "2":
                        print(self.productoseleccionado.to_stringdif())
                        continue

                    elif opcion == "3":
                        return True

                    elif opcion == "4":
                        calificacion = input("¿Le parece adecuada esta recomendación? 1. Sí - 2. No: ")

                        if calificacion == "1":
                            reemplazo = Inventario.listacategorias[self.productoseleccionado.categoria.ordinal()][10]
                            categoria_producto_reemplazar = Inventario.listacategorias[reemplazo.categoria.ordinal()]

                            # Se añade un nuevo producto de la misma categoría al inicio de la fila.
                            self.catalogo[int(self.fila)][2] = reemplazo

                            # Se mueve el reemplazo al final de la lista de su respectiva categoría
                            # para que no se repita en recomendaciones futuras.
                            categoria_producto_reemplazar.remove(reemplazo)
                            categoria_producto_reemplazar.append(reemplazo)

                            print("Producto reemplazado en la lista de recomendaciones.")
    
    def ver_historial_compras(self):
        if len(self.comprador.getHistorialCompras().getFacturas()) == 0:
            return "Usted no ha realizado compras hasta el momento."
        else:
            return self.comprador.mostrarHistorialCompras()

    def ver_notificaciones(self, usuario):
        if len(usuario.getNotificaciones()) == 0:
            return "Usted no tiene notificaciones..."
        else: 
            return usuario.mostrarNotificaciones()

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
                    break #quitar el break cuando se implemente
                elif opcion == 2:
                    self.cuentaBancariaDisplay()
                elif opcion == 3:
                    print("\n")
                    self.returnMenuDisplay()
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
                    self.ver_historial_compras()
                elif opcion == 7:
                    self.ver_notificaciones(self.comprador)
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
            self.comprador.getCarritoCompras().setPrecioTotal(0)
            return False
        else:
            self.comprador.getCarritoCompras().setPrecioTotal(0)
            return True
        
    
    def buyProcessDisplay(self, aplica_o_no, cupon = None):
        mensaje = ""
        if aplica_o_no == True:
            precioTotal = self.comprador.getCarritoCompras().getPrecioTotal() #Se obtiene el precio total de la compra (sin el descuento generado por el cupón).
            descuento = self.comprador.getValorCupones()[cupon - 1] / 100 # Se calcula el descuento que se le aplicará al precio total de la compra.
            precioConDescuento = precioTotal - (precioTotal * descuento) # Se calcula el precio total de la compra con el descuento aplicado.
            self.comprador.getCarritoCompras().setDescuentoAplicadoCompra(cupon - 1) # guarda el descuento aplicado a la compra en el carrito de compras.
            mensaje += f"El precio total de la compra es de: {precioTotal}. Pero con descuento queda en: {precioConDescuento}. Ahora se prosigue con el pago.\n"
            self.comprador.getCarritoCompras().setPrecioTotal(precioConDescuento) # Se actualiza el precio total de la compra en el carrito de compras.
            self.comprador.getCarritoCompras().restarProductosAlComprar() # Se resta la cantidad de productos comprados a la cantidad total de productos.
            # Espacio para lo de las membresias (para que Santiago lo implemente)
            mensaje+= self.comprador.getCarritoCompras().descuentoporproductomenosvendido()
            mensaje+=self.comprador.getCarritoCompras().descuentomembresia()
            mensaje+=self.comprador.getCarritoCompras().verificardescuentopuntos()

            self.comprador.pago(self.comprador, self.vendedor, precioConDescuento, "compra") #Se inicia el proceso de pago.
            self.comprador.getValorCupones().pop(cupon - 1) # Se elimina el cupón de la lista de cupones.
            self.comprador.cantidadCupones-= 1 # Se disminuye la cantidad de cupones en 1.
            mensaje += "============COMPRA===========\n"
            mensaje += "Resumen de la compra:\n"
            mensaje += f"{self.comprador.getHistorialCompras().mostrar_factura_por_id(len(self.comprador.getHistorialCompras().getFacturas()))}\n" # Se muestra por pantalla la factura.
            mensaje += "¡Muchas gracias por su compra!\n"
           
            if self.comprador.cantidadCupones != len(self.comprador.getValorCupones()):
                mensaje += f"Felicidades. Durante la compra te ganaste un cupón del {self.comprador.getValorCupones()[self.comprador.cantidadCupones]} % de descuento para alguna compra en el futuro.\n"
                self.comprador.cantidadCupones += 1
            mensaje += f"Saldo restante en su cuenta: {self.comprador.getCuentaBancaria().getSaldo()}\n"

            self.comprador.recibirNotificacion(f"Se le informa que su compra por un valor de {self.comprador.getCarritoCompras().getPrecioTotal()} ha sido realizada con éxito.", "¡Compra realizada exitosamente!") # Se envía la notificacion al comprador.

            self.vendedor.recibirNotificacion(f"Se le informa que el usuario {self.comprador.getNombre()} ha realizado una compra por un valor de {self.comprador.getCarritoCompras().getPrecioTotal()}.", "Se le informa de una nueva compra") # Se envía la notificacion al vendedor.

            cantidadProductos = [] #Esta lista guarda la informacion de se hay productos por agotarse o no para luego enviar una notificación al vendedor.
            for producto in self.comprador.getCarritoCompras().getListaItems():
                verificacion = producto.verificarCantidadProductos()
                cantidadProductos.append(verificacion)
                producto.setCantidadVendida(producto.getCantidadVendida() + self.comprador.getCarritoCompras().getCantidadPorProductos(producto))
                
                self.inventario.ajusteProductos(producto, "compra")

            for i in range(len(cantidadProductos)):
                if cantidadProductos[i] == True:
                    self.vendedor.recibirNotificacion(f"Se le informa que el producto {self.comprador.getCarritoCompras().getListaItems()[i].getNombre()} está por agotarse.", "Producto por agotarse") # Se envía la notificacion al vendedor.
                                
            self.comprador.setCarritoCompras(CarritoCompras(self.comprador, self.inventario)) # Inicializar un nuevo carrito en forma de "vaciar" el ya existente.
        
        elif aplica_o_no == False:
            self.comprador.getCarritoCompras().restarProductosAlComprar()
            self.comprador.pago(self.comprador, self.vendedor, self.comprador.getCarritoCompras().getPrecioTotal(), "compra") #Se inicia el proceso de pago.

            mensaje+= self.comprador.getCarritoCompras().descuentoporproductomenosvendido()
            mensaje+=self.comprador.getCarritoCompras().descuentomembresia()
            mensaje+=self.comprador.getCarritoCompras().verificardescuentopuntos()

            mensaje += f"El precio total de la compra es de: {self.comprador.getCarritoCompras().getPrecioTotal()}. Ahora se prosigue con el pago.\n"
            mensaje += "============COMPRA===========\n"
            mensaje += "Resumen de la compra:\n"
            mensaje += f"{self.comprador.getHistorialCompras().mostrar_factura_por_id(len(self.comprador.getHistorialCompras().getFacturas()))}\n" # Se muestra por pantalla la factura.
            mensaje += "¡Muchas gracias por su compra!\n"
            if self.comprador.cantidadCupones != len(self.comprador.getValorCupones()):
                mensaje += f"Felicidades. Durante la compra te ganaste un cupón del {self.comprador.getValorCupones()[self.comprador.cantidadCupones]} % de descuento para alguna compra en el futuro.\n"
                self.comprador.cantidadCupones += 1
            mensaje += f"Saldo restante en su cuenta: {self.comprador.getCuentaBancaria().getSaldo()}\n"

            self.comprador.recibirNotificacion(f"Se le informa que su compra por un valor de {self.comprador.getCarritoCompras().getPrecioTotal()} ha sido realizada con éxito.", "¡Compra realizada exitosamente!") # Se envía la notificacion al comprador.

            self.vendedor.recibirNotificacion(f"Se le informa que el usuario {self.comprador.getNombre()} ha realizado una compra por un valor de {self.comprador.getCarritoCompras().getPrecioTotal()}.", "Se le informa de una nueva compra") # Se envía la notificacion al vendedor.

            cantidadProductos = [] #Esta lista guarda la informacion de se hay productos por agotarse o no para luego enviar una notificación al vendedor.
            for producto in self.comprador.getCarritoCompras().getListaItems():
                verificacion = producto.verificarCantidadProductos()
                cantidadProductos.append(verificacion)
                producto.setCantidadVendida(producto.getCantidadVendida() + self.comprador.getCarritoCompras().getCantidadPorProductos(producto))
                
                self.inventario.ajusteProductos(producto, "compra")

            for i in range(len(cantidadProductos)):
                if cantidadProductos[i] == True:
                    self.vendedor.recibirNotificacion(f"Se le informa que el producto {self.comprador.getCarritoCompras().getListaItems()[i].getNombre()} está por agotarse.", "Producto por agotarse") # Se envía la notificacion al vendedor.

            self.comprador.setCarritoCompras(CarritoCompras(self.comprador, self.inventario)) # Inicializar un nuevo carrito en forma de "vaciar" el ya existente.
        return mensaje

  

    def añada(self, producto, cantidad, comprador):
        
        try:
            numerico = int(cantidad)
            if int(cantidad)<1:
                return 
            if int(cantidad)>5:
                return
            if numerico not in [1, 2, 3, 4, 5]:
                raise CantidadInvalidaError("Cantidad inválida, se te asignó una por default que es 1")
            else:
                return comprador.getCarritoCompras().añadirProducto(producto, numerico)
        except ValueError:
            cantidad = "1"
            comprador.getCarritoCompras().añadirProducto(producto, int(cantidad))
            return "La cantidad ingresada no es un número válido, se te asignará una por default que es 1"
        except CantidadInvalidaError as e:
            cantidad = "1"
            comprador.getCarritoCompras().añadirProducto(producto, int(cantidad))
            return str(e)

                   
    def voucherMenuDisplay(self, cuponEliminar = None):
        if cuponEliminar != None:
            self.comprador.eliminarCupones(cuponEliminar)
            self.comprador.cantidadCupones -= 1
            return "El cupón ha sido eliminado exitosamente"


    def cuentaBancariaDisplay(self, monto):
        self.comprador.getCuentaBancaria().recargarCuenta(monto)
        mensaje = f"Recarga exitosa. Su saldo actual es de: {self.comprador.getCuentaBancaria().getSaldo()}"
        return mensaje

    def getComprador(self):
        return self.comprador
    def setComprador(self, comprador):
        self.comprador = comprador

    def getVendedor(self):
        return self.vendedor
    def setVendedor(self, vendedor):
        self.vendedor = vendedor

    def getInventario(self):
        return self.inventario
    def setInventario(self, inventario):
        self.inventario = inventario
    def getFabrica(self):
        return self.fabrica

    def setFabrica(self, fabrica):
        self.fabrica = fabrica
    
    def returnMenuDisplay(self, idFactura, idProducto, cantidadRetornar):
        while True:

            resultado = self.comprador.devolverProducto(idFactura, idProducto, cantidadRetornar, self.vendedor, self.inventario) # Proceso de reembolso en si
            
            if resultado == "FacturaInvalida":
                raise DatoNoExistenteError(f"La factura con ID {idFactura} no existe.")
            elif resultado == "ProductoInvalido":
                return "El producto ingresado no cumple con los requisitos para devolución.\n- No es un producto retornable."
            else:
                return "La devolución se ha procesado correctamente, en sus notificaciones encontrará más información.\n"

    def sellerMenuDisplay(self):

        while True:
            print("===== MENÚ VENDEDOR =====")
            print("1. Generar reporte de ventas")
            print("2. Consultar cuenta bancaria")
            print("3. Ver notificaciones")
            print("4. Volver al Menú Principal\n")
            print("Seleccione una opción: ")

            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    print(Inventario.generar_reporte())
                    print("A continuación, elija los productos que quiere crear en la fábrica para reponer en el inventario.\n"
                        "- Primero elija el producto y posteriormente la cantidad, puede elegir otro producto y repite el proceso.\n"
                        "- Asegúrese de que esté correcto el nombre y la cantidad de cada producto ya que si se equivoca tiene que ingresar todo de nuevo.\n"
                        "- Seleccione un máximo de 50 unidades por orden.\n"
                        "Escriba 'fin' para terminar la orden y enviarla o para salir.")

                    while True:
                        resultado = self.vendedor.crear_orden_fabricacion()
                        print(resultado)
                        if resultado.startswith("Orden creada con éxito.") or resultado == "No se seleccionaron productos. La orden no se creó.":
                            break

                    if self.vendedor.get_ordenes_pendientes():
                        mensaje_fabrica_notif = "Se han entregado los productos"
                        asunto_Vendedor = "Orden De Producción"
                        self.vendedor.recibir_notificacion(Notificacion(mensaje_fabrica_notif, asunto_Vendedor, self.vendedor))
                        self.vendedor.get_ordenes_pendientes().clear()
                elif opcion == 2:
                    print("========= CUENTA BANCARIA =========")
                    print(self.vendedor.consultarCuentaBancaria())
                elif opcion == 3:
                    self.ver_notificaciones(self.vendedor)
                elif opcion == 4:
                    print("Volviendo al Menú Principal...")
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("ERROR. Ingrese un valor válido.")
        
    def mostrar_catalogo(self, historial, reemplazo):
        # Reemplazo se usa para saber si se mostrará el catálogo luego que el usuario haya calificado
        # alguna recomendación, en cuyo caso no se realizará el proceso de las recomendaciones nuevamente, 
        # sino que se mostrará el catálogo como ha sido guardado hasta entonces, ya que en este caso solo se
        # modifica un elemento

        # Llamada a lógica para mostrar el catálogo
        print("===== CATÁLOGO ===== \n".rjust(105))

        # Se guarda la matriz de productos en la variable catálogo
        if historial is None:
            catalogo = self.tienda.get_inventario().crear_catalogo()
        else:
            if not reemplazo:
                catalogo = self.tienda.recomendar_productos(self.comprador)
        
        # Se recorre la matriz para mostrar los productos uno por uno
        # Examina si lo que hay en el índice dado es un objeto producto para
        # utilizar el método get_nombre()
        for fila in range(len(catalogo)):
            for columna in range(len(catalogo[fila])):
                if columna == 7:
                    if isinstance(catalogo[fila][columna], Producto):
                        salida = f"{catalogo[fila][columna].get_nombre():<22}"
                        print(salida)
                    else:
                        salida = f"{catalogo[fila][columna]:<22}"
                        print(salida)
                else:
                    if columna >= 2:
                        if isinstance(catalogo[fila][columna], Producto):
                            salida = f"{catalogo[fila][columna].get_nombre():<22}"
                            print(salida, end=" ")
                        else:
                            salida = f"{catalogo[fila][columna]:<22}"
                            print(salida, end=" ")
                    else:
                        print(catalogo[fila][columna], end="      ")
        
        return catalogo
