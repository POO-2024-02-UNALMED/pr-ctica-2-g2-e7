import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import messagebox

class App:
    def __init__(self, ventana_principal = None):  
        if ventana_principal != None:
            ventana_principal.destroy() # Esto es para destruir la nueva ventana principal
        
        self.contador = 0
        self.imagen_tk = None


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
        
        self.p3.columnconfigure(0, weight=1)
        self.p3.rowconfigure(1, weight=1)
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
    def salir(self): #este metodo nos saca del sistema
        self.window.destroy()
    def nada(self):
        pass
    def descripcion(self): #este metodoe es el asociado a la opcion "descripcion"
        messagebox.showinfo("Descripcion de la tienda","Este es el sistema de gestion de una tienda , aqui puedes segun tu cargo con la tienda , administrarla o ser un comprador, con acceso a todo lo que se puede hacer en cualquier tienda, con algunos beneficios")
    def menu(self): #metodo que crea la barra de menu donde estara descripcion y salir
        menubar=tk.Menu(self.window)
        self.window.config(menu=menubar)
        menu1=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Inicio",menu=menu1,command=self.nada)
        menu1.add_command(label="Descripcion",command=self.descripcion)
        menu1.add_separator()
        menu1.add_command(label="Salir",command=self.salir)

    #este metodo lo cree para que cuando el sistema se abra, se cargue una primera imagen 
    def cargar_imagen_inicial(self):
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(directorio_actual, "imagenes", "imagen1.jpg")
        imagen = Image.open(ruta)

        ancho = self.p4.winfo_width()
        alto = self.p4.winfo_height()
        imagen = imagen.resize((ancho, alto))
        self.imagen_tk = ImageTk.PhotoImage(imagen)
        self.etiqueta.config(image=self.imagen_tk)
        self.etiqueta.imagen = self.imagen_tk
    #esre es el metodo que va cambiando las imagenes conforme el usuario pasa el mouse
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

    # Método para crear la ventana principal de la aplicación
    def crear_ventana_principal(self, ventana_inicio = None):
        if ventana_inicio != None:
            ventana_inicio.destroy() # Se destruye la ventana de inicio
        ventana_principal = tk.Tk()
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
        submenu_comprador.add_command(label= "1. Gestionar Carrito/Ver Catálogo")
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "2. Consultar cuenta bancaria")
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "3. Realizar Devolución")
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "4. Realizar Compra")
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "5. Gestionar cupones")
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "6. Ver historial de compras")
        submenu_comprador.add_separator()
        submenu_comprador.add_command(label= "7. Ver Notificaciones")
        submenu_comprador.add_separator()
        submenu_vendedor.add_command(label= "1. Generar reporte de ventas")
        submenu_vendedor.add_separator()
        submenu_vendedor.add_command(label= "2. Consultar cuenta bancaria")
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


if __name__ == "__main__":
    App()
