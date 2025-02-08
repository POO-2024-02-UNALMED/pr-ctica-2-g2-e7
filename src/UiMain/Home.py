import tkinter as tk




window = tk.Tk()
window.geometry("800x600")
window.title("Inicio")


margin_x = 10 # con esto nos aseguramos de las margenes en los bordes, por este lado, de las margenes en los bordes de x
margin_y = 10 #por este lado en las de y 
spacing = 20  # espacio entre los frames

# Configurar el grid para que crezca 
#vamos a configurar las columnas , 5 columnas, dos donde van los frames, y tres espaciadoras, entre margenes y entre los frames

window.columnconfigure(0, weight=1, minsize=margin_x)
window.columnconfigure(1, weight=10)  # Columna para el primer frame # el weight es diferente ya que es mejor tener mas espacio para los frames y poder tenerlos con buena visibilidad
window.columnconfigure(2, weight=1, minsize=spacing)  # el weigth es el que se asegura del crecimiento de la ventana, hice mas grandes los de los frames para que crezcan como con mejor vista y pues proporcionales
window.columnconfigure(3, weight=20)  # Columna para el segundo frame
window.columnconfigure(4, weight=1, minsize=margin_x)

window.rowconfigure(0, weight=1, minsize=margin_y)
window.rowconfigure(1, weight=30)  # Fila para los frames
window.rowconfigure(2, weight=1, minsize=margin_y)

# Crear los frames
p1 = tk.Frame(window, bg="yellow")
p2 = tk.Frame(window, bg="red")

p1.grid(row=1, column=1, sticky="nsew") #el nsew se asegura de que crezca en todas las direcciones 
p2.grid(row=1, column=3, sticky="nsew")

p1.columnconfigure(0, weight=1, minsize=margin_x)


p1.rowconfigure(1, weight=1)
p1.rowconfigure(2,weight=1)
p3= tk.Frame(p1,bg="blue")
p3.grid(row=1, column=0,sticky="nsew",padx=10,pady=10)


#aqui vamos a crear el frame que deberia llevar el boton que nos lleva a la ventana principal
p4=tk.Frame(p1,bg="green")
p4.grid(row=2,column=0,sticky="nsew",padx=10,pady=10 ) #padx y pady hacen referencia a las margenes 
#vamos a crear los frame p5 y p6
p5=tk.Frame(p2, bg="purple")
p2.rowconfigure(1,weight=1)
p2.rowconfigure(2,weight=1)
p2.columnconfigure(0,weight=1,minsize=margin_x)
p5.grid(row=1,column=0,sticky="nsew",padx=10,pady=10)
p6=tk.Frame(p2,bg="orange")
p6.grid(column=0,row=2,padx=10,pady=10,sticky="nsew")

#ahora vamos a proseguir con el marco de bienvenida
p3.columnconfigure(0,weight=1,minsize=1)
p3.rowconfigure(1,weight=1)

texto_bienvenida = tk.Label(
    p3, 
    text="Bienvenido a nuestra tienda virtual, esperamos que nuestro proyecto de programación orientada a objetos satisfaga todas tus necesidades.",
    wraplength=150
)

texto_bienvenida.grid(column=0, row=1, sticky="nsew",padx=3,pady=3)
window.mainloop()