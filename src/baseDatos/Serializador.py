import os
import pickle

# Asumiendo que las clases MainMenu, Inventario y sus métodos están definidos en algún lugar
import MainMenu

ruta_temp = "src/baseDatos/temp"

def serializar(menu):
    docs = [os.path.join(ruta_temp, f) for f in os.listdir(ruta_temp)]
    
    # Borramos el contenido de los archivos para evitar redundancia
    for file in docs:
        with open(file, 'w') as pw:
            pass  # Abrir el archivo en modo 'w' lo vacía automáticamente

    # Serializamos los objetos
    for file in docs:
        if "comprador" in file:
            with open(file, 'wb') as fos:
                pickle.dump(menu.getComprador(), fos)
        elif "vendedor" in file:
            with open(file, 'wb') as fos:
                pickle.dump(menu.getVendedor(), fos)
        elif "inventario" in file:
            with open(file, 'wb') as fos:
                pickle.dump(menu.getInventario(), fos)



