from gestorAplicacion.usuario.Comprador import Comprador
from gestorAplicacion.pasarelaPago.CuentaBancaria import CuentaBancaria
from gestorAplicacion.compras.CarritoCompras import CarritoCompras
from MainMenu import MainMenu
from gestorAplicacion.tienda.Producto import Producto
from gestorAplicacion.tienda.Inventario import Inventario
from gestorAplicacion.usuario.Vendedor import Vendedor



if __name__ == "__main__":
    producto1 = Producto(10, 2, 0, 0, Producto.Categoria.TECNOLOGIA, 1, "Iphone", 1000, True)
    producto2 = Producto(20, 5, 0, 0, Producto.Categoria.COMIDA, 1, "Manzana", 20, False)
    producto3 = Producto(40, 3, 0, 0, Producto.Categoria.ASEO, 1, "Escoba", 50, True)

    inventario = Inventario([producto1], [producto3], [producto2], [], [], [])
    comprador = Comprador("Juan", None, None)
    cuenta = CuentaBancaria(comprador)
    comprador.setCuentaBancaria(cuenta)
    comprador.getCuentaBancaria().recargarCuenta(10000)
    carrito = CarritoCompras(comprador, inventario)
    carrito.añadirProducto(producto1)
    carrito.añadirProducto(producto2, 5)
    carrito.añadirProducto(producto3, 2)
    comprador.setCarritoCompras(carrito)
    vendedor = Vendedor("pedro", None, inventario, None)
    cuenta2 = CuentaBancaria(vendedor)
    vendedor.setCuentaBancaria(cuenta2)
    test = MainMenu(comprador, vendedor, inventario)
    test.display()