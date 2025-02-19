from gestorAplicacion.usuario.Comprador import Comprador
from gestorAplicacion.usuario.Notificacion import Notificacion
from gestorAplicacion.pasarelaPago.CuentaBancaria import CuentaBancaria
from gestorAplicacion.compras.CarritoCompras import CarritoCompras
from MainMenu import MainMenu
from gestorAplicacion.tienda.Producto import Producto
from gestorAplicacion.tienda.Inventario import Inventario
from gestorAplicacion.usuario.Vendedor import Vendedor



def instanciar():
    inventario = Inventario([], [], [], [], [], [])

    # Productos creados
    categorias = list(Producto.Categoria)
    
    nombresTecnologia = ["Celular", "Laptop", "Tableta", "Audifonos", "Camara", "Smartwatch", "Teclado", 
          "Mouse", "Monitor", "Drone", "Impresor", "Router", "Smart TV", "Cargador", "Auriculares", "Memoria Flash", 
          "Bafle", "Reproductor Blu-ray", "Consola Gamium", "Proyector HD"] 
    
    nombresAseo = ["Jabon Liquido", "Shampoo", "Cepillo Dental", "Pasta Dental", "Desinfectante", "Esponja", 
         "Toallas", "Gel Antibacterial", "Cera de Piso", "Limpiavidrios", "Desodorante", "Hilo Dental", "Enjuague Bucal", "Lavaplatos",
          "Detergente", "Ambientador", "Papel Higienico", "Toallas", "Cepillo", "Clorox"]
    
    nombresComida = ["Manzana", "Queso", "Leche", "Yogur", "Pan", "Aceite", "Cereal", 
         "Galletas", "Mantequilla", "Pasta", "Miel", "Jugo de Naranja", "Avena", "Mermelada", 
         "Agua", "Frijoles", "Atun", "Sopa de Pollo", "Barra de Granola", "Palomitas"]
    
    nombresPapeleria = ["Cuaderno A4", "Lapiz HB", "Boligrafo Azul", "Borrador Magico", "Libreta", "Carpeta", "Borrador", "Tijeras",
         "Pegamento", "Cinta", "Regla", "Marcadores", "Lapices", "Bloc de Dibujo", "Corrector",
         "Papel de Colores", "Grapadora", "Perforadora", "Cartulina", "Compas"]
    
    nombresJugueteria = ["Muñeca", "Auto Rayo", "Pelota Saltarina", "Lego", "Puzzle", "Figura de Accion", "Bicicleta",
         "Patinete", "Dron Junior", "Set de Tren", "Juguete de Cocina", "Castillo de Princesa", "Helicoptero RC", "Avion de Pasajeros", "Torre de Bloques",
         "Rompecabezas", "Bate de beisbol", "Robot Interactivo", "Tabla de Skate", "Cubo Rubik"]
    
    nombresDeportes = ["Balon de Futbol", "Raqueta de Tenis", "Gorra de Running", "Tennis", "Guantes de Boxeo", "Pesa Kettlebell", "Bolsa de Deporte",
         "Gafas de Natacion", "Bicicleta de Montaña", "Patineta Freestyle", "Mancuerna Ajustable", "Camiseta de futbol", "Pantalon de Yoga", "Protector Bucal", "Cuerda para Saltar",
         "Banco de Pesas", "Chaleco Reflectivo", "Casco de Ciclismo", "Balon de Baloncesto", "Reloj Deportivo"]
    
    nombresCategorias = [nombresTecnologia, nombresAseo, nombresComida, nombresPapeleria, nombresJugueteria, nombresDeportes]
    
    id = 1

    for i in range(len(categorias)): 
        categoria = categorias[i]
        nombres = nombresCategorias[i]

        for j in range(len(nombres)):
            cantidad = id * 5  # Ejemplo de valor para cantidad
            cantidadAlerta = id * 2  # Ejemplo de cantidad alerta
            precio = 10 + id * 3  # Ejemplo de precio
            retornable = (id % 2 == 0)  # Alterna retornabilidad

            producto = Producto(cantidad, cantidadAlerta, 0, 0, categoria, id, nombres[j], precio, retornable)

            # Crear el producto y agregarlo al inventario
            inventario.añadirProducto(producto)

            id += 1

    
    return inventario
    
    # Menu serializado (Para serializar se hace exactamente igual que en el proyecto de Java):
#     test = MainMenu()
 #   test.display()