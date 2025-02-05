import random
from abc import ABC

class Cupon(ABC):
    VALOR_DESCUENTO = 11

    @staticmethod
    def generarValorCupon():
        valor_descuento_aleatorio = random.randint(0, Cupon.VALOR_DESCUENTO - 1) + 5
        return valor_descuento_aleatorio

    def crearCupon(self):
        generar_cupon = random.choice([True, False])
        return generar_cupon