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
from UiMain.Field import FieldFrame

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
        self.imagen_tk = None
        self.imagen1 = None
        self.imagen2 = None
        self.imagen3 = None
        self.imagen4 = None


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
        self.p6.after(100,self.cargar_imagen_nosotros)
        self.p5.bind("<Button-1>",self.actualizar_imagenes)
        self.p4.after(100, self.cargar_imagen_inicial)
        self.p4.bind("<Enter>", self.imagenes)
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
        self.p2 = tk.Frame(self.window, bg="red")

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
        
        self.p6 = tk.Frame(self.p2, bg="orange")
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
        self.etiqueta1=tk.Label(self.p6)
        self.etiqueta1.grid(column=0,row=0,sticky="nsew")
        self.etiqueta2 = tk.Label(self.p6,background="red")
        self.etiqueta2.grid(column=1,row=0,sticky="nsew")
        self.etiqueta3 = tk.Label(self.p6,background="green")
        self.etiqueta3.grid(column=0,row=1,sticky="nsew")
        self.etiqueta4 = tk.Label(self.p6,background="black")
        self.etiqueta4.grid(column=1,row=1,sticky="nsew")
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
    ''
    def cargar_imagen_nosotros(self):
       
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta1 = os.path.join(directorio_actual, "imagenes", "imagen1.jpg")
        imagen1 = Image.open(ruta1)
        
        
        ruta2 = os.path.join(directorio_actual, "imagenes", "imagen2.jpg")
        imagen2= Image.open(ruta2)
        ruta3 = os.path.join(directorio_actual, "imagenes", "imagen3.jpg")
        imagen3 = Image.open(ruta3)
        ruta4 = os.path.join(directorio_actual, "imagenes", "imagen4.jpg")
        imagen4= Image.open(ruta4)
        self.window.update_idletasks()#este metodo actualiza las medidad del frame
        ancho = self.p6.winfo_width()
        alto = self.p6.winfo_height()
        imagen1 = imagen1.resize((ancho//2, alto//2))
        self.imagen_tk1= ImageTk.PhotoImage(imagen1)
        self.etiqueta1.config(image=self.imagen_tk1)
        self.etiqueta1.imagen = self.imagen_tk1
        imagen2 = imagen2.resize((ancho//2, alto//2))
        self.imagen_tk2= ImageTk.PhotoImage(imagen2)
        self.etiqueta2.config(image=self.imagen_tk2)
        self.etiqueta2.imagen = self.imagen_tk2
        imagen3 = imagen3.resize((ancho//2, alto//2))
        self.imagen_tk3= ImageTk.PhotoImage(imagen3)
        self.etiqueta3.config(image=self.imagen_tk3)
        self.etiqueta3.imagen = self.imagen_tk3
        imagen4 = imagen4.resize((ancho//2, alto//2))
        self.imagen_tk4= ImageTk.PhotoImage(imagen4)
        self.etiqueta4.config(image=self.imagen_tk4)
        self.etiqueta4.imagen = self.imagen_tk4
        self.imagen1=imagen1
        self.imagen2=imagen2
        self.imagen3=imagen3
        self.imagen4=imagen4


    
    def actualizar_imagenes(self, evento):
        """Intercambia las imágenes entre las etiquetas"""
        
        # Obtener las dimensiones del frame (p6)
        ancho_imagen = self.p6.winfo_width()
        alto_imagen = self.p6.winfo_height()

        # Redimensionar las imágenes antes de rotarlas
        imagen1_redimensionada = self.imagen1.resize((ancho_imagen//2, alto_imagen), Image.Resampling.LANCZOS)
        imagen2_redimensionada = self.imagen2.resize((ancho_imagen, alto_imagen), Image.Resampling.LANCZOS)
        imagen3_redimensionada = self.imagen3.resize((ancho_imagen, alto_imagen), Image.Resampling.LANCZOS)
        imagen4_redimensionada = self.imagen4.resize((ancho_imagen, alto_imagen), Image.Resampling.LANCZOS)

        # Convertir las imágenes redimensionadas a formato PhotoImage de Tkinter
        self.imagen_tk1 = ImageTk.PhotoImage(imagen1_redimensionada)
        self.imagen_tk2 = ImageTk.PhotoImage(imagen2_redimensionada)
        self.imagen_tk3 = ImageTk.PhotoImage(imagen3_redimensionada)
        self.imagen_tk4 = ImageTk.PhotoImage(imagen4_redimensionada)

        # Rotar las imágenes
        self.imagen_tk1, self.imagen_tk2, self.imagen_tk3, self.imagen_tk4 = (
            self.imagen_tk2, self.imagen_tk3, self.imagen_tk4, self.imagen_tk1
        )

        # Asignar las imágenes rotadas a las etiquetas
        self.etiqueta1.config(image=self.imagen_tk1)
        self.etiqueta2.config(image=self.imagen_tk2)
        self.etiqueta3.config(image=self.imagen_tk3)
        self.etiqueta4.config(image=self.imagen_tk4)

        # Actualizar el frame de la ventana
        self.window.update_idletasks()

    #este metodo lo cree para que cuando el sistema se abra, se cargue una primera imagen 
    def cargar_imagen_inicial(self):
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(directorio_actual, "imagenes", "imagen2.jpg")
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
        rutas = ["imagen1.jpg", "imagen2.jpg", "imagen3.jpg", "imagen4.jpg", "imagen5.jpg"] #este contiene las direcciones de las imagenes
        ruta = os.path.join(directorio_actual, "imagenes", rutas[self.contador])
        
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

    def mostrarCatalogo(self):
        

        frameCatalogo = tk.Frame(ventana_principal, bg="lightblue", width= 600, height= 400)
        frameCatalogo.pack(expand= True)

        titulo = tk.Label(frameCatalogo, text= "tuki", font= ("Arial", 10))
        titulo.pack(expand = True)

      #  for fila in range(0, 4):
       #     for columna in range(0,5):
        #        producto = tk.Button(frameCatalogo, text= catalogo[fila][columna].getNombre(), command= self.seleccionarProducto())
         #       producto.grid(row= fila, column= columna, padx= 10, pady= 10)

    def seleccionarProducto(self):
        pass
    
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
            tree.insert("", "end", values=(producto, cantidad))

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
            tree.insert("", "end", values=(producto, cantidad))


        
    def verElCarrito(self,ventana_principal):
        tabla = ttk.Treeview(ventana_principal, columns=("Producto", "Cantidad"), show="headings")
        tabla.heading("Producto", text="Producto")
        tabla.heading("Cantidad", text="Cantidad")
        tabla.pack(expand=True,side="top",fill="both")
        carrito.calcularTotal()
        total_label = tk.Label(
            ventana_principal, 
            text=f"Total: {carrito.getPrecioTotal()}", 
            font=("Arial", 15, "bold"),
            justify="right"
        )
        total_label.pack(expand=True,side="right")
        # Añadir los productos al Treeview
        for producto, cantidad in zip(carrito.getListaItems(), carrito.getCantidadPorProducto()):
            tabla.insert("", "end", values=(producto, cantidad))

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

        opcion1 = tk.Button(frameCarrito, text= "Agregar productos/Ver catálogo", command= lambda: [self.limpiar_ventana(ventana_principal, menu_bar), self.mostrarCatalogo()])
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
    
    def realizarDevolucion(self, valores):
        id_factura = valores["ID Factura"]
        id_producto = valores["ID Producto"]
        cantidad_retornar = valores["Cantidad a devolver"]

        mensaje = self.main_menu.returnMenuDisplay(id_factura, id_producto, cantidad_retornar)
        messagebox.showinfo("Devolución de Producto", mensaje)

    #    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ
    #    |    |    |    |    |    |    |    |    |
    # MÉTODOS PRESENTES EN EL MENÚ DE DEVOLUCIONES

    # MÉTODOS PRESENTES PARA HISTORIAL DE COMPRAS
    #    |    |    |    |    |    |    |    |    
    #    V    V    V    V    V    V    V    V    

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

    

    #    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ        
    #    |    |    |    |    |    |    |    
    # MÉTODOS PRESENTES PARA NOTIFICACIONES

    # MÉTODOS PRESENTES EN EL MENÚ DE CUENTA BANCARIA
    #    |    |    |    |    |    |    |    |    |
    #    V    V    V    V    V    V    V    V    V
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
    #    |    |    |    |    |    |    |    |    |
    #    V    V    V    V    V    V    V    V    V
    def menuCompra(self, ventana, menu_bar):
        if len(self.main_menu.getComprador().getCarritoCompras().getListaItems()) == 0:
            messagebox.showerror("Carrito de compras vacío", "ERROR. Por favor verifique que su carrito de compras no este vacío.")
        elif self.main_menu.verificacionCompra() == False:
            messagebox.showerror("Saldo insuficiente", "ERROR. No cuentas con saldo suficiente para realizar la compra.")
        else:
            self.main_menu.getComprador().getCarritoCompras().calcularTotal()
            respuesta = messagebox.askyesno("Aplicar Cupón", "¿Desea aplicar un cupón de descuento durante la compra?")
            if respuesta == True:
                if len(self.main_menu.getComprador().getValorCupones()) == 0:
                    messagebox.showerror("Cupones insuficientes", "ERROR. No cuentas con cupones suficientes.")
                else:
                    cuadro_texto = tk.Text(ventana, height= 10, width= 40)
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
    
    def realizarCompra(self, ventana, menu_bar, aplica_o_no = None, cupon = None):
        self.limpiar_ventana(ventana, menu_bar)
        label = tk.Label(ventana, text= "Resumen de la compra", font=("Arial", 16, "bold"))
        label.pack()
        cuadro_texto = tk.Text(ventana, height= 20, width= 50)
        cuadro_texto.insert(tk.END, self.main_menu.buyProcessDisplay(aplica_o_no, cupon))
        cuadro_texto.config(state= tk.DISABLED)
        cuadro_texto.pack()
        label2 = tk.Label(ventana, text= "¡Muchas gracias por su compra!", font=("Arial", 16, "bold"))
        label2.pack()
    #    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ    Ʌ
    #    |    |    |    |    |    |    |    |    |
    # MÉTODOS PRESENTES EN EL MENÚ DE COMPRA



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
        submenu_comprador.add_command(label= "5. Gestionar cupones")
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "6. Ver historial de compras", command=lambda: [self.limpiar_ventana(ventana_principal,menu_bar), self.verHistorialCompras()])
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "7. Ver Notificaciones")
        submenu_comprador.add_separator()
        submenu_vendedor.add_command(label= "1. Generar reporte de ventas")
        submenu_vendedor.add_separator()
        submenu_vendedor.add_command(label= "2. Consultar cuenta bancaria", command=lambda: [self.limpiar_ventana(ventana_principal, menu_bar), self.menuCuentaBancaria(ventana_principal, "vendedor")])
        submenu_vendedor.add_separator()
        submenu_vendedor.add_command(label= "3. Ver notificaciones")
        menu_ayuda = tk.Menu(menu_bar, tearoff= 0) # se crea un menú llamado ayuda
        menu_bar.add_cascade(label= "Archivo", menu= menu_archivo)
        menu_archivo.add_command(label= "Aplicación", command= self.informacion_basica) # Se muestra la información básica del programa
        menu_archivo.add_separator()
        menu_archivo.add_command(label= "Salir", command= lambda: App(ventana_principal)) # Se crea una nueva ventana de inicio y se destruye esta ventana principal
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
        producto1 = Producto(10, 2, 0, 0, Producto.Categoria.TECNOLOGIA, 1, "Iphone", 1000, True)
        producto2 = Producto(20, 5, 0, 0, Producto.Categoria.COMIDA, 2, "Manzana", 20, False)
        producto3 = Producto(40, 3, 0, 0, Producto.Categoria.ASEO, 3, "Escoba", 50, True)
        inventario = Inventario([producto1], [producto3], [producto2], [], [], [])
        comprador = Comprador("Juan", None, None)
        cuenta = CuentaBancaria(comprador)
        comprador.setCuentaBancaria(cuenta)
        carrito = CarritoCompras(comprador, inventario)
        carrito.añadirProducto(producto1)
        carrito.añadirProducto(producto2, 5)
        carrito.añadirProducto(producto3, 2)
        comprador.setCarritoCompras(carrito)
        vendedor = Vendedor("pedro", None, inventario, None)
        cuenta2 = CuentaBancaria(vendedor)
        vendedor.setCuentaBancaria(cuenta2)
        self.comprador=comprador
        self.carrito=carrito

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

if __name__ == "__main__":
    ########################################################
    #Esto es de prueba, no borrar hasta que Nicolás diga
    producto1 = Producto(10, 2, 0, 0, Producto.Categoria.TECNOLOGIA, 1, "Iphone", 1000, True)
    producto2 = Producto(20, 5, 0, 0, Producto.Categoria.COMIDA, 2, "Manzana", 20, False)
    producto3 = Producto(40, 3, 0, 0, Producto.Categoria.ASEO, 3, "Escoba", 50, True)
    ########################################################
    inventario = instanciar()
    comprador = Comprador("Juan", None, None)
    cuenta = CuentaBancaria(comprador)
    cuenta.recargarCuenta(2000)
    comprador.setCuentaBancaria(cuenta)
    carrito = CarritoCompras(comprador, inventario)
    ######################################
    #Esto es de prueba, no borrar hasta que Nicolás diga
    carrito.añadirProducto(producto1)
    carrito.añadirProducto(producto2, 5)
    carrito.añadirProducto(producto3, 2)
    ######################################
    comprador.setCarritoCompras(carrito)
    vendedor = Vendedor("pedro", None, inventario, None)
    cuenta2 = CuentaBancaria(vendedor)
    vendedor.setCuentaBancaria(cuenta2)
    test = MainMenu(comprador, vendedor, inventario)
    App(None, test)
    #Menu serializado (Para serializar se hace exactamente igual que en el proyecto de Java):
    #test = MainMenu()
    #test.display()
