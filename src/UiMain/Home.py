import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from tkinter import ttk
import sys
import os



# Añadir el directorio src al sys.path
sys.path.append(os.path.abspath('src'))
ruta_superior = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Agregarla al sys.path
sys.path.append(ruta_superior)

# Ahora puedes importar lo que quieras
from gestorAplicacion.tienda.Inventario import Inventario
from gestorAplicacion.tienda.Producto import Producto

from gestorAplicacion.usuario.Comprador import Comprador
from gestorAplicacion.usuario.Notificacion import Notificacion
from gestorAplicacion.pasarelaPago.CuentaBancaria import CuentaBancaria
from gestorAplicacion.compras.CarritoCompras import CarritoCompras
from MainMenu import MainMenu
from App import instanciar
from gestorAplicacion.tienda.Producto import Producto
from gestorAplicacion.tienda.Inventario import Inventario
from gestorAplicacion.usuario.Vendedor import Vendedor
from UiMain.FieldFrame import FieldFrame
from baseDatos.Serializador import serializar
from excepciones.DatoNoExistenteError import DatoNoExistenteError
from excepciones.CantidadInvalidaError import CantidadInvalidaError
from excepciones.CarritoComprasVacio import CarritoComprasVacio
from excepciones.SaldoInsuficienteError import SaldoInsuficienteError

class App:
    def __init__(self, ventana_principal = None, mainMenu = None):
        # POR FAVOR NO BORRAR ESTO
        if ventana_principal != None:
            ventana_principal.destroy() # Esto es para destruir la nueva ventana principal
        #Catálogo de productos a mostrar por pantalla
        #self.catalogo = catalogo = instanciar().crearCatalogo()
        
        self.ventana_principal = ventana_principal
        self.main_menu = mainMenu #Esta será la instancia del Main Menu con la cual todos trabajaremos 
        self.contador = 0
        self.indice_imagenes = 0
        self.imagen_tk = None
        self.imagen1 = None
        self.imagen2 = None
        self.imagen3 = None
        self.imagen4 = None

        # Datos de los desarrolladores
        self.desarrolladores = [
            {"nombre": "Tomás Aristizábal Gómez", "bio": "Desarrollador especializado en arquitectura de software y sistemas empresariales.",
             "imagenes": ["src/imagenes/tomas1.jpg", "src/imagenes/tomas2.jpg", "src/imagenes/tomas3.jpg", "src/imagenes/tomas4.jpg"]},
            {"nombre": "Santiago Barrientos Medina", "bio": "Full Stack Developer con experiencia en Python y desarrollo web.",
             "imagenes": ["src/imagenes/santiago1.jpg", "src/imagenes/santiago2.jpg", "src/imagenes/santiago3.jpg", "src/imagenes/santiago4.jpg"]},
            {"nombre": "Juan Nicolás Chaparro Rodríguez", "bio": "Desarrollador en Inteligencia Artificial y Ciencia de Datos.",
             "imagenes": ["src/imagenes/juan1.jpg", "src/imagenes/juan2.jpg", "src/imagenes/juan3.jpg", "src/imagenes/juan4.jpg"]},
            {"nombre": "Simón David Díaz Rojas", "bio": "Especialista en ciberseguridad y redes informáticas.",
             "imagenes": ["src/imagenes/simon1.jpg", "src/imagenes/simon2.jpg", "src/imagenes/simon3.jpg", "src/imagenes/simon4.jpg"]},
            {"nombre": "José Alejandro Castro Rey", "bio": "Ingeniero de software con experiencia en videojuegos y desarrollo móvil.",
             "imagenes": ["src/imagenes/jose1.jpg", "src/imagenes/jose2.jpg", "src/imagenes/jose3.jpg", "src/imagenes/jose4.jpg"]}
        ]

        # Crear ventana principal
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.title("Inicio")
        # configurar grid es quien configura las columnas y filas de la ventana principal
        self.configurar_grid()
        #despues de tener bien organizadas las columnas y filas donde van a estar los frames , pasamos a crear los frames
        self.crear_frames()
        self.menu()
        
        self.etiqueta.config(image=self.imagen_tk)
        self.p4.after(100, self.cargar_imagen_inicial)
        self.p4.bind("<Enter>", self.imagenes)
        self.p6.after(100, self.mostrar_hoja_de_vida_y_fotos)
        Inventario=self.instanciar()
        
        
        
        self.window.mainloop()
    #metodo para configurar el grid de la ventana principal 
    def configurar_grid(self):
        margin_x = 10#margenes 
        margin_y = 10
        spacing = 20 # espacio entre frame p1 y p2

        self.window.columnconfigure(0, weight=1, minsize=margin_x)
        self.window.columnconfigure(1, weight=10)
        self.window.columnconfigure(2, weight=1, minsize=spacing)
        self.window.columnconfigure(3, weight=15)
        self.window.columnconfigure(4, weight=1, minsize=margin_x)
        #abajo configuramos las filas
        self.window.rowconfigure(0, weight=1, minsize=margin_y)
        self.window.rowconfigure(1, weight=30)
        self.window.rowconfigure(2, weight=1, minsize=margin_y)
    



    
    def crear_frames(self): 
        #frames principales
        self.p1 = tk.Frame(self.window)
        self.p2 = tk.Frame(self.window)

        self.p1.grid(row=1, column=1, sticky="nsew")
        self.p2.grid(row=1, column=3, sticky="nsew")

        self.p1.columnconfigure(0, weight=1)
        self.p1.rowconfigure(1, weight=1)
        self.p1.rowconfigure(2, weight=1)

        self.p3 = tk.Frame(self.p1)
        self.p3.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.p4 = tk.Frame(self.p1)
        self.p4.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.p4.grid_propagate(False)
        

        self.p2.rowconfigure(1, weight=1)
        self.p2.rowconfigure(2, weight=1)
        self.p2.columnconfigure(0, weight=1)
        
        self.p5 = tk.Frame(self.p2, bg="purple")
        self.p5.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        self.p6 = tk.Frame(self.p2)
        self.p6.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.p6.grid_propagate(False)
        
        self.p3.columnconfigure(0, weight=2)
        self.p3.rowconfigure(1, weight=2)
        self.p6.columnconfigure(0, weight=2)
        self.p6.rowconfigure(0, weight=2)
        self.p6.columnconfigure(1, weight=2)
        self.p6.rowconfigure(1, weight=2)
        #el label que da la bienvenida
        texto_bienvenida = tk.Label(
            self.p3, 
           text="Bienvenido a nuestra tienda virtual, \n\nesperamos que nuestro proyecto de \n\nprogramación orientada a objetos \n\nsatisfaga todas tus necesidades.",
            wraplength=350,
            font=("Arial", 11, "bold"), 
            justify="left"
        )
        texto_bienvenida.grid(column=0, row=1, sticky="nsew", padx=3, pady=3)

        self.p4.columnconfigure(0, weight=1)
        self.p4.rowconfigure(0, weight=3)
        self.p4.rowconfigure(1, weight=1)
        # el boton que nos da el acceso al sistema 
        self.boton_accesosistema = tk.Button(self.p4, text="Ingresar al sistema", command= lambda: self.crear_ventana_principal(self.window))
        self.boton_accesosistema.grid(column=0, row=1, sticky="nsew", padx=2, pady=2)
        #el label que va a contener las imagenes asociadas al sistema
        self.etiqueta = tk.Label(self.p4)
        self.etiqueta.grid(column=0, row=0, sticky="nsew")
        self.label_bio = tk.Label(self.p5, padx=10, pady=10)
        self.label_bio.pack(fill="both", expand=True)
        self.label_bio.bind("<Button-1>", self.cambiar_hoja_de_vida)
        self.etiquetas_imagenes = [
            tk.Label(self.p6, borderwidth=10, relief="groove", bg="white"),
            tk.Label(self.p6, borderwidth=10, relief="groove", bg="white"),
            tk.Label(self.p6, borderwidth=10, relief="groove", bg="white"),
            tk.Label(self.p6, borderwidth=10, relief="groove", bg="white"),
        ]


        # Posicionar con grid()
        for i, etiqueta in enumerate(self.etiquetas_imagenes):
            etiqueta.grid(row=i // 2, column=i % 2, padx=10, pady=10)

    def salir(self): #este metodo nos saca del sistema
        self.window.destroy()
    def nada(self):
        pass
    def descripcion(self): #este metodoe es el asociado a la opcion "descripcion"
        messagebox.showinfo("Descripcion de la tienda","Este es el sistema de gestion de una tienda , aqui puedes segun tu cargo con la tienda , administrarla o ser un comprador, con acceso a todo lo que se puede hacer en cualquier tienda, con algunos beneficios")
    def menu(self): #metodo que crea la barra de menu donde estara descripcion y salir
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)

        # Crear los submenús
        menu1 = tk.Menu(menubar, tearoff=0)

        # Agregar opciones a los submenús
        menu1.add_command(label="Descripción", command=self.descripcion)
        menu1.add_separator()
        menu1.add_command(label="Salir", command=self.salir)

        # Agregar los submenús a la barra de menú
        menubar.add_cascade(label="Inicio", menu=menu1)
    
    def cambiar_hoja_de_vida(self, event):
        #cambia al siguiente desarrollador al hacer clic en la hoja de vida
        self.indice_imagenes = (self.indice_imagenes + 1) % len(self.desarrolladores)
        self.mostrar_hoja_de_vida_y_fotos()

    def mostrar_hoja_de_vida_y_fotos(self):
        #actualiza la hoja de vida y las imgenes del desarrollador actual
        desarrollador = self.desarrolladores[self.indice_imagenes]

        # Actualizar la hoja de vida
        self.label_bio.config(text=f"{desarrollador['nombre']}\n\n{desarrollador['bio']}")

        # Obtener dimensiones del frame P6
        ancho_imagen = self.p6.winfo_width() // 2
        alto_imagen = self.p6.winfo_height() // 2

        self.imagenes_tk = [] 

        for i, img_path in enumerate(desarrollador["imagenes"]):
            imagen = Image.open(img_path)
            imagen_redimensionada = imagen.resize((ancho_imagen, alto_imagen), Image.Resampling.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
            self.imagenes_tk.append(imagen_tk)

            # Asignar la imagen a su etiqueta correspondiente
            self.etiquetas_imagenes[i].config(image=imagen_tk)


    #este metodo lo cree para que cuando el sistema se abra, se cargue una primera imagen 
    def cargar_imagen_inicial(self):
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        directorio_padre = os.path.dirname(directorio_actual)
        ruta = os.path.join(directorio_padre, "imagenes", "imagen5.jpg")
        imagen = Image.open(ruta)

        ancho = 500
        alto = 200
        imagen = imagen.resize((ancho, alto))
        self.imagen_tk = ImageTk.PhotoImage(imagen)
        self.etiqueta.config(image=self.imagen_tk)
        self.etiqueta.imagen = self.imagen_tk

    #este es el metodo que va cambiando las imagenes conforme el usuario pasa el mouse
    def imagenes(self, evento):

        self.window.update_idletasks()#este metodo actualiza las medidad del frame
        ancho = self.p4.winfo_width()
        alto = self.p4.winfo_height()

        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        directorio_padre = os.path.dirname(directorio_actual)
        rutas = ["imagen1.jpg", "imagen2.jpg", "imagen3.jpg", "imagen4.jpg", "imagen5.jpg"] #este contiene las direcciones de las imagenes
        ruta = os.path.join(directorio_padre, "imagenes", rutas[self.contador])
        
        imagen = Image.open(ruta)
        imagen = imagen.resize((ancho, alto))
        self.imagen_tk = ImageTk.PhotoImage(imagen)
        self.etiqueta.config(image=self.imagen_tk)
        self.etiqueta.imagen = self.imagen_tk

        self.contador = (self.contador + 1) %5
    
        
       
    def limpiar_ventana(self,ventana_principal,menu_bar):
      # Obtener todos los widgets de la ventana
        for widget in ventana_principal.winfo_children():
        # Destruir el widget solo si no es el menu_bar
         if widget != menu_bar:
            widget.destroy()


    # MÉTODOS PRESENTES EN EL MENÚ DEL CARRITO
    #    |    |    |    |    |    |    |    |
    #    V    V    V    V    V    V    V    V

    #RECOMENDACIONES EN PROGRESO(ATT. SIMÓN)

    def mostrarCatalogo(self, menu_bar, historialCompras):
        #El método recibe el menu_bar creado en la ventana principal para poder limpiar la ventana principal
        #sin eliminarlo

        catalogo = None
        frameCatalogo = tk.Frame(ventana_principal,  width= 600, height= 400)
        frameCatalogo.pack(expand= True)

        #FUNICIONES AUXILIARES PARA EL BUEN FUNCIONAMIENTO DE LOS BOTONES

        def actualizarCatalogo(historialCompras = None):
            nonlocal catalogo

            if historialCompras != None:
                catalogo = self.instanciar().crearCatalogoRecomendaciones(historialCompras)
            else:
                catalogo = self.instanciar().crearCatalogo()
              
        #Funcion creada para cuando se deba volver a crear el frame,
        # ya que se elimina al actualizar el catálogo

        def crearFrameCatalogo():
            nonlocal frameCatalogo
            frameCatalogo = tk.Frame(ventana_principal,  width= 600, height= 400)
            frameCatalogo.pack(expand= True)

        def rechazarRecomendaciones():
            actualizarCatalogo()
            self.limpiar_ventana(ventana_principal, menu_bar)
            crearFrameCatalogo()
            crearBotonesProductos()
        
        def confirmarRecomendaciones():
            actualizarCatalogo(historialCompras)
            self.limpiar_ventana(ventana_principal, menu_bar)
            crearFrameCatalogo()
            crearBotonesProductos()
        
        def crearBotonesProductos():
            #iteracion = 1 #BORRAR
            for fila in range(0, 5):
                for columna in range(0,6):
                    productoActual = catalogo[fila][columna] #Asegura que la referencia sea correcta
                    producto = tk.Button(frameCatalogo, text= catalogo[fila][columna].getNombre(),
                                      command= lambda producto=productoActual: [self.limpiar_ventana(ventana_principal, menu_bar),self.seleccionarProducto(producto)])
                  #  prueba = (catalogo[fila][columna] != None) #BORRAR
                   # print(prueba) #BORRAR
                    producto.grid(row= fila, column= columna, padx= 10, pady= 10)
                   # iteracion += 1 #BORRAR
        
        actualizarCatalogo()

        
        if len(historialCompras.getFacturas()) != 0:
            
            preguntaRecomendaciones = tk.Label(frameCatalogo, text= "¿Desea actualizar las recomendaciones?", font= ("Arial", 10))
            preguntaRecomendaciones.pack()

            botonConfirmarRecomendaciones = tk.Button(frameCatalogo, text= "Sí", command= lambda: confirmarRecomendaciones())
            botonConfirmarRecomendaciones.pack(expand= True)

            botonRechazarRecomendaciones = tk.Button(frameCatalogo, text= "No", command= lambda: rechazarRecomendaciones())
            botonRechazarRecomendaciones.pack()
            actualizarCatalogo()
        else:
            actualizarCatalogo()
            crearBotonesProductos()
        
        
        
    

    def seleccionarProducto(self, producto):

        #Muestra la info del producto para añadir al carrito o regresar al menú
        
        frameProducto = tk.Frame(ventana_principal, bg= "lightblue")
        frameProducto.pack(expand= True, fill= "both")

        infoProducto = tk.Label(frameProducto, text= producto, font= ("Arial", 20, "bold"), justify="left")
        infoProducto.pack(pady= 10,ipadx=20,ipady=20)

        frameBotones = tk.Frame(frameProducto, bg= "lightblue", width= 500, height= 200)
        frameBotones.pack(side= "top")

        botonAgregar = tk.Button(frameBotones, text= "Agregar al carrito", command= lambda: [self.limpiar_ventana(ventana_principal, menu_bar), self.agregarAlCarrito(producto, menu_bar)])
        botonAgregar.grid(row= 0, column= 0, padx= 10, pady= 10)

        botonRegresar = tk.Button(frameBotones, text= "Regresar", command= lambda: [self.limpiar_ventana(ventana_principal, menu_bar), self.menuCarrito(menu_bar)])
        botonRegresar.grid(row= 0, column= 1, padx= 10, pady= 10)


    def agregarAlCarrito(self, producto, menu_bar):
    # Crear un marco con bordes
        f1 = tk.Frame(ventana_principal, bd=5, relief="groove")
        
        # Crear y empacar el título
        titulo = tk.Label(
            f1, 
            text="AGREGAR AL CARRITO \n por favor indique la cantidad a añadir",
            font=("Arial", 15, "bold"),
            justify="center"
        )
        titulo.pack(expand=True, padx=20, pady=20)
        
        # Definir criterios, valores y habilitación
        criterios = ["Producto", "Cantidad"]
        valores = [producto.getNombre(), "1"]  # Valor inicial para "Cantidad" es 1
        habilitado = [False, True]  # El campo "Cantidad" es editable
        
        global tuc
        tuc = producto
        
        # Crear y empacar el FieldFrame
        field_frame = FieldFrame(f1, "Criterio", criterios, "Valor", valores, habilitado, funcion_llamado=self.añadir)
        field_frame.pack(padx=20, pady=20, expand=True, ipadx=50, ipady=50)
        
        # Empacar el marco principal
        f1.pack(padx=10, pady=10, expand=True)
    def añadir(self,valores):
        cantidad=int(valores["Cantidad"])
        
        o=self.main_menu.añada(tuc,cantidad,self.main_menu.getComprador())
        messagebox.showinfo("Añadir",o)
        self.ejecutar_ambas2()

    
    def eliminarProductosDelCarrito(self, ventana_principal):
    
        alto = ventana_principal.winfo_height()
        contenedorcarrito = tk.Frame(ventana_principal, height=alto*0.90)
        contenedorcarrito.pack(side="top", fill="x", padx=10, pady=20)
        contenedorcarrito.columnconfigure(0, weight=1)
        contenedorcarrito.rowconfigure(0, weight=1)

        # Título "Eliminar del Carrito"
        titulo = tk.Label(
            contenedorcarrito, 
            text="Eliminar del Carrito",
            font=("Arial", 24, "bold"),
            justify="center"
        )
        titulo.grid(column=0, row=0, sticky="ew", columnspan=2, pady=(0, 10))  # Añadimos un espaciado vertical

        # Crear Treeview para mostrar el contenido del carrito
        global tree
        tree = ttk.Treeview(contenedorcarrito, columns=("Producto", "Cantidad"), show="headings")
        tree.heading("Producto", text="Producto")
        tree.heading("Cantidad", text="Cantidad")
        tree.grid(column=0, row=1, sticky="nsew", columnspan=2)
        carrito.calcularTotal()
        total_label = tk.Label(
            contenedorcarrito, 
            text=f"Total: {carrito.getPrecioTotal()}", 
            font=("Arial", 15, "bold"),
            justify="right"
        )
        total_label.grid(column=0, row=2, sticky="e", columnspan=2, pady=(10, 0))
        # Añadir los productos al Treeview
        for producto, cantidad in zip(carrito.getListaItems(), carrito.getCantidadPorProducto()):
            tree.insert("", "end", values=(producto.getNombre(), cantidad))

        # Ajustar las columnas del Treeview
        for col in tree["columns"]:
            tree.column(col, anchor="center")
        
        criterios = ["Producto a eliminar", "Cantidad"]
        valores = [None, "1"]  # Valor inicial para "Cantidad" es 1
        habilitado = [True, True]  # Ambos campos son editables
       
        # Crear el FieldFrame
        field_frame = FieldFrame(ventana_principal, "Criterio", criterios, "Valor", valores, habilitado, funcion_llamado=self.elimina)
        field_frame.pack(padx=20, pady=20, expand=True, ipadx=10, ipady=10)

    def elimina(self,valores):
        Producto=valores["Producto a eliminar"]
        cantidad=int(valores["Cantidad"])
    
        mensaje=self.main_menu.eliminacion(Producto,cantidad,comprador)
        messagebox.showinfo("Eliminacion",mensaje)
        self.ejecutar_ambas()
    def ejecutar_ambas2(self):
        self.limpiar_ventana(ventana_principal, menu_bar)
        
        self.verElCarrito(ventana_principal)
    def ejecutar_ambas(self):
        self.actualizar_treeview()
        self.limpiar_ventana(ventana_principal, menu_bar)
        
        self.eliminarProductosDelCarrito(ventana_principal)

    def actualizar_treeview(self):
        # Limpiar el Treeview antes de actualizar
        for item in tree.get_children():
            tree.delete(item)
        # Repoblar el Treeview con los productos actualizados
        for producto, cantidad in zip(carrito.getListaItems(), carrito.getCantidadPorProducto()):
            tree.insert("", "end", values=(producto.getNombre(), cantidad))
 
    def verElCarrito(self,ventana_principal):
        tabla = ttk.Treeview(ventana_principal, columns=("Producto", "Cantidad"), show="headings")
        tabla.heading("Producto", text="Producto")
        tabla.heading("Cantidad", text="Cantidad")
        tabla.pack(expand=True,side="top",fill="both")
        self.main_menu.getComprador().getCarritoCompras().calcularTotal()
        total_label = tk.Label(
            ventana_principal, 
            text=f"Total: {self.main_menu.getComprador().getCarritoCompras().getPrecioTotal()}", 
            font=("Arial", 15, "bold"),
            justify="right"
        )
        total_label.pack(expand=True,side="right")
        # Añadir los productos al Treeview
        for producto, cantidad in zip(self.main_menu.getComprador().getCarritoCompras().getListaItems(), self.main_menu.getComprador().getCarritoCompras().getCantidadPorProducto()):
            tabla.insert("", "end", values=(producto.getNombre(), cantidad))

        # Ajustar las columnas del Treeview
        for col in tabla["columns"]:
            tabla.column(col, anchor="center")

    def regresar(self):
        pass #Agregar lógica para esta opción


    def menuCarrito(self, menu_bar):
        #El método recibe el menu_bar creado en la ventana principal para poder limpiar la ventana principal
        #Sin eliminarlo

        #Se le da un color al frame solo para verificar su tamaño, luego se borra
        frameCarrito = tk.Frame(ventana_principal,  width= 600, height= 400)
        frameCarrito.pack(expand= True)

        titulo = tk.Label(frameCarrito, text= "Menú Carrito", font= ("Arial", 10))
        titulo.grid(row= 0, column= 1, columnspan=2, padx= 10, pady= 10)

        opcion1 = tk.Button(frameCarrito, text= "Agregar productos/Ver catálogo", command= lambda: [self.limpiar_ventana(ventana_principal, menu_bar), self.mostrarCatalogo(menu_bar, self.main_menu.getComprador().getHistorialCompras())])
        opcion1.grid(row= 1, column= 1, padx= 10, pady= 10)

        opcion2 = tk.Button(frameCarrito, text= "Eliminar productos del carrito", command= lambda: [self.limpiar_ventana(ventana_principal, menu_bar), self.eliminarProductosDelCarrito(ventana_principal)])
        opcion2.grid(row= 2, column= 1, padx= 10, pady= 10)

        opcion3 = tk.Button(frameCarrito, text= "Ver el carrito", command= lambda: [self.limpiar_ventana(ventana_principal, menu_bar), self.verElCarrito(ventana_principal)])
        opcion3.grid(row= 3, column= 1, padx= 10, pady= 10)

    #    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ
    #    |    |    |    |    |    |    |    |
    # MÉTODOS PRESENTES EN EL MENÚ DEL CARRITO


    # MÉTODOS PRESENTES EN EL MENÚ DE DEVOLUCIONES
    #    |    |    |    |    |    |    |    |    |
    #    V    V    V    V    V    V    V    V    V
        
    # Parte grafica del proceso de reembolso
    def menuDevolucion(self, menu_bar):
    
        respuesta = messagebox.askyesno("Devolver producto", "¿Conoce el ID de la factura y del producto a devolver?")
        if not respuesta:
            messagebox.showinfo("Ayuda", "Por favor, consiga la información necesaria en el numeral 6 del MENÚ COMPRADOR")
            self.regresar()

        else:
            frameDevolucion = tk.Frame(ventana_principal, bg="white", width= 1000, height= 800)
            frameDevolucion.pack(expand=True)

            titulo = tk.Label(frameDevolucion, text="Devolución de Producto", font=("Arial", 16, "bold"), bg="white")
            titulo.pack(pady=(20, 5))  # Título en la parte superior con un margen superior

            # Descripción del detalle del proceso
            descripcion = tk.Label(frameDevolucion, text="A continuación, ingrese los detalles del producto a devolver.", font=("Arial", 12), bg="white")
            descripcion.pack(pady=(0, 20))  # Descripción debajo del título con un margen inferior


            criterios = ["ID Factura", "ID Producto", "Cantidad a devolver"]
            valores_iniciales = [None, None, None]
            habilitados = [True, True, True]

            field_frame = FieldFrame(frameDevolucion, "Criterios", criterios, "Valores", valores_iniciales, funcion_llamado=self.realizarDevolucion)
            field_frame.pack(padx=10, pady=10)
    
    # Llamada a la logica para realizar el reembolso
    def realizarDevolucion(self, valores):
        try:
            id_factura = int(valores["ID Factura"])
            id_producto = int(valores["ID Producto"])
            cantidad_retornar = int(valores["Cantidad a devolver"])

            if id_factura < 0 or id_producto < 0 or cantidad_retornar < 0:
                raise CantidadInvalidaError("Los valores deben ser números positivos.")

            mensaje = self.main_menu.returnMenuDisplay(id_factura, id_producto, cantidad_retornar)

            messagebox.showinfo("Devolución de Producto", mensaje)

        except CantidadInvalidaError as e:
            messagebox.showerror("Cantidad Invalida", str(e))

        except DatoNoExistenteError as e:
            messagebox.showerror("Dato No Existente", str(e))


    #    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ
    #    |    |    |    |    |    |    |    |    |
    # MÉTODOS PRESENTES EN EL MENÚ DE DEVOLUCIONES


    # MÉTODOS PRESENTES PARA HISTORIAL DE COMPRAS
    #    |    |    |    |    |    |    |    |    
    #    V    V    V    V    V    V    V    V    

    # Parte grafica del proceso para ver el historial de compras
    def verHistorialCompras(self):
        # Crear un frame para la tabla
        frameHistorial = tk.Frame(ventana_principal, bg="brown", padx=20, pady=20)
        frameHistorial.pack(expand=True, fill="both")

        titulo = tk.Label(frameHistorial, text="Historial de Compras", font=("Arial", 16, "bold"), bg="white")
        titulo.pack(pady=10)

        # Crear tabla con ttk.Treeview
        columnas = ("ID Compra", "Producto", "ID Producto", "Cantidad", "Retornable", "Total")
        self.tabla = ttk.Treeview(frameHistorial, columns=columnas, show="headings")

        #Encabezados
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100, anchor="center")

        self.tabla.pack(expand=True, fill="both")

        historial = self.obtenerHistorialCompras()
        
        self.cargar_historial(historial, self.tabla)

    # Se encarga de hacer visible graficamente el historial en la tabla
    def cargar_historial(self, historial, tabla):
        for compra in historial:
            id_compra, productos, total = compra

            primer_producto, primer_id, primera_cantidad, primer_retornabilidad = productos[0]
            parent_id = self.tabla.insert("", "end", values=(id_compra, primer_producto, primer_id, primera_cantidad, primer_retornabilidad, ""), open=True)

            for producto, ID, cantidad, retornabilidad in productos[1:]:
                tabla.insert(parent_id, "end", values=("", producto, ID, cantidad, retornabilidad))
            tabla.insert("", "end", values=("", "", "", "", "Total de la compra:", total))
            
            self.tabla.insert("", "end", values=("", "", "", "", "", ""), tags=("separador",))

            self.tabla.tag_configure("separador", background="beige")

    # Llamada a la logica para obtener el historial de compras
    def obtenerHistorialCompras(self):
        
        historial = self.main_menu.ver_historial_compras()

        if isinstance(historial, str):
            messagebox.showinfo("Lo sentimos", historial)
            return []

        else: 
            return historial

    #    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    
    #    |    |    |    |    |    |    |    |    
    # MÉTODOS PRESENTES PARA HISTORIAL DE COMPRAS


    # MÉTODOS PRESENTES PARA NOTIFICACIONES
    #    |    |    |    |    |    |    | 
    #    V    V    V    V    V    V    V 

    # Parte grafica del proceso para ver las notificaciones de cada usuario
    def verNotificaciones(self, usuario):
        frameNotificaciones = tk.Frame(ventana_principal, bg="brown", padx=20, pady=20)
        frameNotificaciones.pack(expand=True, fill="both")
    
        titulo = tk.Label(frameNotificaciones, text="Notificaciones", font=("Arial", 16, "bold"), bg="white")
        titulo.pack(pady=10)

        columnas = ("Fecha", "Destinatario", "Asunto")
        self.tabla = ttk.Treeview(frameNotificaciones, columns=columnas, show="headings")

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100, anchor="center")

        self.tabla.pack(side="left", expand=True, fill="both")

        #campo de texto para mostrar el mensaje
        self.texto_mensaje = tk.Text(frameNotificaciones, wrap="word", height=10, width=50)
        self.texto_mensaje.pack(side="right", expand=True, fill="both", padx=10)

        self.notificaciones = self.obtenerNotificaciones(usuario)

        self.cargarNotificaciones(self.notificaciones, self.tabla, self.texto_mensaje)

        self.tabla.bind("<<TreeviewSelect>>", self.mostrarMensaje)

    # Se encarga de hacer visible graficamente las notificaciones en la tabla 
    def cargarNotificaciones(self, notificaciones, tabla, texto_mensaje):
        for notificacion in notificaciones:
            fecha, destinatario, asunto, mensaje = notificacion
            tabla.insert("", "end", values=(fecha, destinatario, asunto))

    # Se encarga de hacer visible graficamente el mensaje de la notificacion 
    def mostrarMensaje(self, evento):
        item_seleccionado = self.tabla.selection()
        if item_seleccionado:
            item = self.tabla.item(item_seleccionado[0])["values"]
            if item:
                fecha, destinatario, asunto = item
                mensaje = next(noti[3] for noti in self.notificaciones if noti[:3] == tuple(item))

                self.texto_mensaje.config(state="normal")

                self.texto_mensaje.delete("1.0", tk.END)
                self.texto_mensaje.insert(tk.END, f"Fecha: {fecha}\n")
                self.texto_mensaje.insert(tk.END, f"Destinatario: {destinatario}\n")
                self.texto_mensaje.insert(tk.END, f"Asunto: {asunto}\n\n")
                self.texto_mensaje.insert(tk.END, f"Mensaje:\n{mensaje}")

                self.texto_mensaje.config(state="disabled")
                     
    # Llamada a la logica para obtener las notificaciones de cada usuario
    def obtenerNotificaciones(self, usuario):
        notificaciones = self.main_menu.ver_notificaciones(usuario)

        if isinstance(notificaciones, str):
            messagebox.showinfo("Lo sentimos", notificaciones)
            return []
        else: 
            return notificaciones

    #    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ        
    #    |    |    |    |    |    |    |    
    # MÉTODOS PRESENTES PARA NOTIFICACIONES

    # MÉTODOS PRESENTES EN EL MENÚ DE CUENTA BANCARIA
    #    |    |    |    |    |    |    |    |    |
    #    V    V    V    V    V    V    V    V    V

    # Parte grafica del proceso relacionado a la cuenta bancaria
    def menuCuentaBancaria(self, ventana, tipoUsuario):
        if tipoUsuario == "comprador":
            respuesta = messagebox.askyesno("Recargar saldo", "¿Desea recargar saldo en su cuenta bancaria?")
            if not respuesta:
                mensaje = self.main_menu.getComprador().consultarCuentaBancaria()
                label = tk.Label(ventana, text= mensaje, bg= "white", font=("Arial", 16, "bold"))
                label.pack(pady = 150)
            else:
                criterios = ["Valor a recargar"]
                valores_iniciales = [None]
                titulo = tk.Label(ventana, text= "Consultar Cuenta Bancaria", font=("Arial", 16, "bold"))
                titulo.pack(pady=(100, 5))
                descripcion = tk.Label(ventana, text= "Por favor ingrese el valor correspondiente que usted desea recargar para su cuenta", font=("Arial", 12, "bold"))
                descripcion.pack(pady= (5, 0))
                ff = FieldFrame(ventana, "Criterios", criterios, "Valores", valores_iniciales, funcion_llamado = self.actualizar_saldos)
                ff.pack(pady= 10)
        else:
            mensaje = self.main_menu.getVendedor().consultarCuentaBancaria()
            label = tk.Label(ventana, text= mensaje, bg= "white", font=("Arial", 16, "bold"))
            label.pack(pady = 150)
    
    # Llamada a la logica para recargar la cuenta
    def actualizar_saldos(self, valores):
        try:
            monto = float(valores["Valor a recargar"])
            if monto < 500:
                messagebox.showwarning("Monto menor al aceptado", "Lo sentimos. Por favor introduzca un monto mayor a 500.")
            elif monto > 10000:
                messagebox.showwarning("Monto mayor al aceptado", "Lo sentimos. El monto máximo a recargar es de 10000, por favor intente nuevamente.")
            else:
                mensaje = self.main_menu.cuentaBancariaDisplay(monto)
                messagebox.showinfo("Recarga exitosa", mensaje)
        except ValueError:
            messagebox.showerror("ERROR", "Por favor ingrese un valor unicamente numerico.")

    #    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ
    #    |    |    |    |    |    |    |    |    |
    # MÉTODOS PRESENTES EN EL MENÚ DE CUENTA BANCARIA


    # MÉTODOS PRESENTES EN EL MENÚ DE COMPRA
    #    |    |    |    |    |    |    |    |
    #    V    V    V    V    V    V    V    V   

    def menuCompra(self, ventana, menu_bar):
        try:
            self.comprobarCarrito(self.main_menu.getComprador().getCarritoCompras().getListaItems())
            self.comprobarSaldo(self.main_menu)
            self.main_menu.getComprador().getCarritoCompras().calcularTotal()
            respuesta = messagebox.askyesno("Aplicar Cupón", "¿Desea aplicar un cupón de descuento durante la compra?")
            if respuesta == True:
                if len(self.main_menu.getComprador().getValorCupones()) == 0:
                    messagebox.showerror("Cupones insuficientes", "ERROR. No cuentas con cupones suficientes.")
                else:
                    cuadro_texto = tk.Text(ventana, height= 10, width= 40, wrap= "word")
                    cuadro_texto.insert(tk.END, f"Actualmente usted cuenta con {len(self.main_menu.getComprador().getValorCupones())} cupones de descuento. Estos cupones son los siguientes:\n{self.main_menu.getComprador().mostrarCupones()}")
                    cuadro_texto.config(state= tk.DISABLED)
                    cuadro_texto.pack(pady= (70, 10))

                    label = tk.Label(ventana, text= "Por favor escribe en el recuadro de abajo tu selección", font=("Arial", 14, "bold"))
                    label.pack(pady=(0, 10))

                    entry = tk.Entry(ventana, width= 40)
                    entry.pack(pady=(0, 10))

                    frame_botones = tk.Frame(ventana)
                    frame_botones.pack()

                    boton_aceptar = tk.Button(frame_botones, text="Aceptar", command=lambda: obtener_cupon(entry))
                    boton_aceptar.grid(row=0, column=0, padx=10)

                    boton_borrar = tk.Button(frame_botones, text="Borrar", command=lambda: eliminar_texto(entry))
                    boton_borrar.grid(row=0, column=1, padx=10)

                    def obtener_cupon(entrada_evaluar):
                        entrada = entrada_evaluar.get()
                        try:
                            cupon = int(entrada)
                            if cupon > len(self.main_menu.getComprador().getValorCupones()) or cupon < 1:
                                messagebox.showerror("Cupón no valido", "ERROR. El cupón que seleccionaste no existe, intenta nuevamente (solo debes de poner el número del cupón que quieres usar, por ejemplo si quieres usar el primero pon 1)")
                            else:
                                self.realizarCompra(ventana, menu_bar, True, cupon)
                        except ValueError:
                            messagebox.showerror("Opción no válida", "ERROR. Por favor introduzca un valor númerico.")
                    def eliminar_texto(entrada_evaluar):
                        entrada_evaluar.delete(0, tk.END)
            elif respuesta == False:
                self.realizarCompra(ventana, menu_bar, False, None)
        except SaldoInsuficienteError as error_saldo:
            messagebox.showerror("Saldo Insuficiente", error_saldo)
        except CarritoComprasVacio as error_carrito:
            messagebox.showerror("Carrito de Compras Vacío", error_carrito)
    
    def realizarCompra(self, ventana, menu_bar, aplica_o_no = None, cupon = None):
        self.limpiar_ventana(ventana, menu_bar)
        label = tk.Label(ventana, text= "Resumen de la compra", font=("Arial", 16, "bold"))
        label.pack()
        cuadro_texto = tk.Text(ventana, height= 20, width= 50, wrap= "word")
        cuadro_texto.insert(tk.END, self.main_menu.buyProcessDisplay(aplica_o_no, cupon))
        cuadro_texto.config(state= tk.DISABLED)
        cuadro_texto.pack()
        label2 = tk.Label(ventana, text= "¡Muchas gracias por su compra!", font=("Arial", 16, "bold"))
        label2.pack()
        
    def comprobarCarrito(self, listaItems):
        if len(listaItems) == 0:
            raise CarritoComprasVacio("ERROR. Por favor verifique que su carrito de compras no este vacío.")
    def comprobarSaldo(self, main_menu):
        estado = main_menu.verificacionCompra()
        if estado == False:
            raise SaldoInsuficienteError("ERROR. No cuentas con saldo suficiente para realizar la compra.")
    #    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    
    #    |    |    |    |    |    |    |    |  
    # MÉTODOS PRESENTES EN EL MENÚ DE COMPRA


    # MÉTODOS PRESENTES EN EL MENÚ DE CUPONES
    #    |    |    |    |    |    |    |    |   
    #    V    V    V    V    V    V    V    V 
       
    def menuCupones(self, ventana, menu_bar, mainMenu):
        main_menu = mainMenu
        def eliminar_cupones(valores):
            try:
                cupon_eliminar = int(valores["Cupón"])
                if cupon_eliminar < 1 or cupon_eliminar > len(main_menu.getComprador().getValorCupones()):
                    messagebox.showerror("Opción no válida", "ERROR. Por favor seleccionar solo una de las opciones disponibles.")
                else:
                    mensaje = main_menu.voucherMenuDisplay(cupon_eliminar)
                    messagebox.showinfo("Cupón eliminado", mensaje)
                    self.limpiar_ventana(ventana, menu_bar)
            except ValueError:
                messagebox.showerror("Input incorrecto", "ERROR. Por favor introduzca un valor númerico.")

        if len(self.main_menu.getComprador().getValorCupones()) == 0:
            messagebox.showwarning("No hay cupones", "Lo sentimos. Actualmente no dispones de cupones, si tienes suerte ganarás alguno durante una compra.")
        else:
            respuesta = messagebox.askyesno("Eliminar cupón", "¿Deseas eliminar algún cupón?")
            if respuesta == True:
                titulo = tk.Label(ventana, text= "Eliminar cupones", font=("Arial", 16, "bold"))
                titulo.pack(pady=(40, 5))
                descripcion = tk.Label(ventana, text= "Por favor ingrese el valor correspondiente al cupón que usted desea eliminar", font=("Arial", 12, "bold"))
                descripcion.pack(pady= (5, 10))
                cuadro_texto = tk.Text(ventana, height= 10, width= 50, wrap= "word")
                cuadro_texto.insert(tk.END, f"Cupones disponibles:\n{self.main_menu.getComprador().mostrarCupones()}")
                cuadro_texto.config(state= tk.DISABLED)
                cuadro_texto.pack(pady=(0, 5))

                criterios = ["Cupón"]
                valores_iniciales = [None]
                ff = FieldFrame(ventana, "Criterios", criterios, "Valores", valores_iniciales, funcion_llamado = eliminar_cupones)
                ff.pack()
            else:
                titulo = tk.Label(ventana, text= "Cupones", font=("Arial", 16, "bold"))
                titulo.pack(pady=(40, 5))
                cuadro_texto = tk.Text(ventana, height= 10, width= 50, wrap= "word")
                cuadro_texto.insert(tk.END, f"Cupones disponibles:\n{self.main_menu.getComprador().mostrarCupones()}")
                cuadro_texto.config(state= tk.DISABLED)
                cuadro_texto.pack(pady=(0, 5))

    #    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    
    #    |    |    |    |    |    |    |    |    
    # MÉTODOS PRESENTES EN EL MENÚ DE CUPONES 


    # MÉTODOS PRESENTES EN EL MENÚ DE VENDEDOR
    #    |    |    |    |    |    |    |    |    
    #    V    V    V    V    V    V    V    V    

    def generarReporteVentas(self, menu_bar):

        inventario = self.main_menu.getInventario() 
        reporte = inventario.generar_reporte()

        frameReporte = tk.Frame(ventana_principal, bg="lightblue", width=600, height=400)
        frameReporte.pack(expand=True)

        texto_reporte = tk.Text(frameReporte, wrap="word", width=70, height=20)
        texto_reporte.insert("1.0", reporte)
        texto_reporte.config(state="disabled")  # Para que el usuario no pueda modificarlo
        texto_reporte.pack(padx=10, pady=10)

        boton_volver = tk.Button(frameReporte, text="Volver", command=lambda: self.limpiar_ventana(ventana_principal, menu_bar))
        boton_volver.pack(pady=10)
    
    #    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    
    #    |    |    |    |    |    |    |    |    
    # MÉTODOS PRESENTES EN EL MENÚ DE VENDEDOR 

    # Método para crear la ventana principal de la aplicación
    def crear_ventana_principal(self, ventana_inicio = None):
        if ventana_inicio != None:
            ventana_inicio.destroy() # Se destruye la ventana de inicio
        global ventana_principal
        ventana_principal = tk.Tk()
        global menu_bar
        ventana_principal.geometry("800x600")
        ventana_principal.title("Kartera") #Se crea una nueva ventana
        menu_bar = tk.Menu(ventana_principal) # Se crea el menú para esta ventana principal
        ventana_principal.config(menu= menu_bar)
        menu_archivo = tk.Menu(menu_bar, tearoff= 0) # Se crea el menú llamado archivo
        menu_proceso_consultas = tk.Menu(menu_bar, tearoff= 0) # Se crea el menú llamado procesos y consultas
        submenu_comprador = tk.Menu(menu_proceso_consultas, tearoff= 0) # Se crea el submenu para procesos y consultas del comprador
        submenu_vendedor = tk.Menu(menu_proceso_consultas, tearoff= 0)# Se crea el submenu para procesos y consultas del vendedor
        menu_proceso_consultas.add_cascade(label= "1. Menú Comprador", menu= submenu_comprador)
        menu_proceso_consultas.add_separator()
        menu_proceso_consultas.add_cascade(label= "2. Menú Vendedor", menu= submenu_vendedor)
        submenu_comprador.add_command(label= "1. Gestionar Carrito/Ver Catálogo", command=lambda: [self.limpiar_ventana(ventana_principal,menu_bar), self.menuCarrito(menu_bar)])
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "2. Consultar cuenta bancaria", command=lambda: [self.limpiar_ventana(ventana_principal, menu_bar), self.menuCuentaBancaria(ventana_principal, "comprador")])
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "3. Realizar Devolución", command=lambda: [self.limpiar_ventana(ventana_principal,menu_bar), self.menuDevolucion(menu_bar)])
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "4. Realizar Compra", command=lambda: [self.limpiar_ventana(ventana_principal,menu_bar), self.menuCompra(ventana_principal, menu_bar)])
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "5. Gestionar cupones", command=lambda: [self.limpiar_ventana(ventana_principal,menu_bar), self.menuCupones(ventana_principal, menu_bar, self.main_menu)])
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "6. Ver historial de compras", command=lambda: [self.limpiar_ventana(ventana_principal,menu_bar), self.verHistorialCompras()])
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "7. Ver Notificaciones", command=lambda: [self.limpiar_ventana(ventana_principal,menu_bar), self.verNotificaciones(self.main_menu.comprador)])
        submenu_comprador.add_separator()
        submenu_vendedor.add_command(label= "1. Generar reporte de ventas", command=lambda: [self.limpiar_ventana(ventana_principal,menu_bar), self.generarReporteVentas(menu_bar)])
        submenu_vendedor.add_separator()
        submenu_vendedor.add_command(label= "2. Consultar cuenta bancaria", command=lambda: [self.limpiar_ventana(ventana_principal, menu_bar), self.menuCuentaBancaria(ventana_principal, "vendedor")])
        submenu_vendedor.add_separator()
        submenu_vendedor.add_command(label= "3. Ver notificaciones", command=lambda: [self.limpiar_ventana(ventana_principal,menu_bar), self.verNotificaciones(self.main_menu.vendedor)])
        menu_ayuda = tk.Menu(menu_bar, tearoff= 0) # se crea un menú llamado ayuda
        menu_bar.add_cascade(label= "Archivo", menu= menu_archivo)
        menu_archivo.add_command(label= "Aplicación", command= self.informacion_basica) # Se muestra la información básica del programa
        menu_archivo.add_separator()
        menu_archivo.add_command(label= "Salir", command= lambda: [self.serializar_main_menu(), App(ventana_principal, self.main_menu)]) # Se crea una nueva ventana de inicio y se destruye esta ventana principal
        menu_bar.add_cascade(label= "Procesos y consultas", menu= menu_proceso_consultas)
        menu_bar.add_cascade(label= "Ayuda", menu= menu_ayuda)
        menu_ayuda.add_command(label= "Desarrolladores", command= self.ayuda)

        frame0 = tk.Frame(ventana_principal)
        frame0.pack(expand= True, fill = "both")
        label0 = tk.Label(frame0, text= "Kartera")
        label0.pack(padx= 10, anchor= "nw")

        frame1 = tk.Frame(frame0)
        frame1.pack(expand= True, fill= "both", pady= 15)
        ventana_principal.mainloop()

    def informacion_basica(self):
        messagebox.showinfo("Descripción de la aplicación", "En la aplicación podrás cumplir el rol de un vendedor o un comprador de una tienda. Como comprador vas a poder gestionar tu carrito, ver el catálogo, comprar, realizar devoluciones, etc. Mientras que como vendedor pordrás actualizar productos, generar reportes de ventas, etc.")

    def ayuda(self):
        messagebox.showinfo("Ayuda", "Desarrolladores:\nTomás Aristizábal Gómez\nSantiago Barrientos Medina\nJosé Alejandro Castro Rey\nJuan Nicolás Chaparro Rodríguez\nSimón David Díaz Rojas")
    def instanciar(self):
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
    
    def serializar_main_menu(self):
        serializar(self.main_menu)


if __name__ == "__main__":
    ########################################################
    #Esto es de prueba, no borrar hasta que Nicolás diga
    # producto1 = Producto(10, 2, 0, 0, Producto.Categoria.TECNOLOGIA, 1, "Iphone", 1000, True)
    # producto2 = Producto(20, 5, 0, 0, Producto.Categoria.COMIDA, 2, "Manzana", 20, False)
    # producto3 = Producto(40, 3, 0, 0, Producto.Categoria.ASEO, 3, "Escoba", 50, True)
    ########################################################
    inventario = instanciar()
    # inventario.añadirProducto(producto1)
    # inventario.añadirProducto(producto2)
    # inventario.añadirProducto(producto3)
    comprador = Comprador("Juan", None, None)
    cuenta = CuentaBancaria(comprador)
    cuenta.recargarCuenta(2000)
    comprador.setCuentaBancaria(cuenta)
    carrito = CarritoCompras(comprador, inventario)
    ######################################
    #Esto es de prueba, no borrar hasta que Nicolás diga
    # carrito.añadirProducto(producto1)
    # carrito.añadirProducto(producto2, 5)
    # carrito.añadirProducto(producto3, 2)
    ######################################
    comprador.setCarritoCompras(carrito)
    vendedor = Vendedor("pedro", None, inventario, None)
    cuenta2 = CuentaBancaria(vendedor)
    vendedor.setCuentaBancaria(cuenta2)
    test = MainMenu(comprador, vendedor, inventario)
    App(None, test)
    #Menu serializado (Para serializar se hace exactamente igual que en el proyecto de Java), es decir comentan ela variable que dice test de arriba 
    # y la creación de App de arriba y descomentan lo de abajo. Para que funcione la serialización deben de salirse desde la misma interfaz y no cerrarla con el botón de la x.
    #Si tienen dudas de este nuevo proceso no duden en preguntarle a Nicolás.
    # test = MainMenu()
    # App(None, test)
