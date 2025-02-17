import tkinter as tk
from tkinter import messagebox
class FieldFrame(tk.Frame):
    def __init__(self, parent, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None, funcion_llamado=None):
        super().__init__(parent)
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores if valores else [None] * len(criterios)
        self.habilitado = habilitado if habilitado else [True] * len(criterios)
        self.funcion_llamado = funcion_llamado #Función a llamar al presionar el botón aceptar
        
        self.entries = []  # Almacenar entradas para obtener sus valores después
        
        self.crear_ventanas()

    def crear_ventanas(self):
        # Crear el título de los criterios
        label_criterio = tk.Label(self, text=self.tituloCriterios)
        label_criterio.grid(row=0, column=0, padx=5, pady=5)
        
        label_valor = tk.Label(self, text=self.tituloValores)
        label_valor.grid(row=0, column=1, padx=5, pady=5)
        
        # Crear los campos de entrada según los criterios
        for i, criterio in enumerate(self.criterios):
            label = tk.Label(self, text=criterio)
            label.grid(row=i+1, column=0, padx=5, pady=5, sticky='w')
            
            entry = tk.Entry(self)
            if self.valores[i]:
                entry.insert(0, self.valores[i])  #Insertar valor inicial si está presente
            
            #Si el campo está deshabilitado, lo hacemos no-editable
            if not self.habilitado[i]:
                entry.config(state='disabled')
                
            entry.grid(row=i+1, column=1, padx=5, pady=5)
            self.entries.append(entry)
        
        # Agregar botón para aceptar
        boton_aceptar = tk.Button(self, text="Aceptar", command=self.validate_and_save)
        boton_aceptar.grid(row=len(self.criterios)+1, column=0, padx=5, pady=5)
        
        # Agregar botón para borrar
        boton_borrar = tk.Button(self, text="Borrar", command=self.limpiar_campos)
        boton_borrar.grid(row=len(self.criterios)+1, column=1, padx=5, pady=5)

    def getValue(self, criterio):
        #Devuelve el valor del criterio solicitado
        if criterio not in self.criterios:
            raise ValueError(f"El criterio '{criterio}' no existe.")
        indice = self.criterios.index(criterio)
        return self.entries[indice].get()

    def limpiar_campos(self):
        #Borra todos los campos de texto
        for entry in self.entries:
            entry.delete(0, tk.END)
    
    def validate_and_save(self):
        #Verifica que todos los campos de texto tengan valores
        campos_faltantes = []
        for i, entry in enumerate(self.entries):
            if not entry.get().strip():
                campos_faltantes.append(self.criterios[i])
        
        if campos_faltantes:
            messagebox.showwarning("Campos Vacíos", f"Por favor, complete los siguientes campos: {', '.join(campos_faltantes)}")
            return
        valores = {criterio: self.getValue(criterio) for criterio in self.criterios}
        self.funcion_llamado(valores)
