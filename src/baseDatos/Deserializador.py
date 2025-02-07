import os
import pickle

ruta_temp = "src/baseDatos/temp"

def deserializar(menu):
    docs = [os.path.join(ruta_temp, f) for f in os.listdir(ruta_temp)]
    
    # Bucle para deserializar todos nuestros objetos
    for file in docs:
        if "comprador" in file:
            try:
                with open(file, 'rb') as fis:
                    menu.setComprador(pickle.load(fis))
            except (FileNotFoundError, IOError, pickle.PickleError) as e:
                print(e)
        elif "inventario" in file:
            try:
                with open(file, 'rb') as fis:
                    menu.setInventario(pickle.load(fis))
            except (FileNotFoundError, IOError, pickle.PickleError) as e:
                print(e)
        elif "vendedor" in file:
            try:
                with open(file, 'rb') as fis:
                    menu.setVendedor(pickle.load(fis))
            except (FileNotFoundError, IOError, pickle.PickleError) as e:
                print(e)
