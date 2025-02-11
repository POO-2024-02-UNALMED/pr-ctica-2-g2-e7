import tkinter as tk
from PIL import Image, ImageTk
import os

class App:
    def __init__(self):  
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
        
        self.etiqueta.config(image=self.imagen_tk)
        self.p4.after(100, self.cargar_imagen_inicial)
        self.p4.bind("<Enter>", self.imagenes)
        
        self.window.mainloop()
    
    def configurar_grid(self):
        margin_x = 10#margenes 
        margin_y = 10
        spacing = 20 # espacio entre frame p1 y p2

        self.window.columnconfigure(0, weight=1, minsize=margin_x)
        self.window.columnconfigure(1, weight=10)
        self.window.columnconfigure(2, weight=1, minsize=spacing)
        self.window.columnconfigure(3, weight=15)
        self.window.columnconfigure(4, weight=1, minsize=margin_x)
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
        self.boton_accesosistema = tk.Button(self.p4, text="Ingresar al sistema")
        self.boton_accesosistema.grid(column=0, row=1, sticky="nsew", padx=2, pady=2)
        #el label que va a contener las imagenes asociadas al sistema
        self.etiqueta = tk.Label(self.p4)
        self.etiqueta.grid(column=0, row=0, sticky="nsew")
    
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
    
    def imagenes(self, evento):
        self.window.update_idletasks()
        ancho = self.p4.winfo_width()
        alto = self.p4.winfo_height()

        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        rutas = ["imagen1.jpg", "imagen2.jpg", "imagen3.jpg", "imagen4.jpg", "imagen5.jpg"]
        ruta = os.path.join(directorio_actual, "imagenes", rutas[self.contador])
        
        imagen = Image.open(ruta)
        imagen = imagen.resize((ancho, alto))
        self.imagen_tk = ImageTk.PhotoImage(imagen)
        self.etiqueta.config(image=self.imagen_tk)
        self.etiqueta.imagen = self.imagen_tk

        self.contador = (self.contador + 1) %5

if __name__ == "__main__":
    App()
