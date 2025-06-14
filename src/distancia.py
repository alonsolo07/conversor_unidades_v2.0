"""
Clase para la conversión entre diferentes unidades de distancia.
Proporciona métodos estáticos para convertir entre kilómetros, metros y millas.

Atributos:
conversiones (dict): Diccionario con factores de conversión a metros (unidad base).

Métodos:
convertir(valor, unidad_origen, unidad_destino): Convierte un valor de una unidad a otra.
"""
    
from .conversor import Conversor

class Distancia(Conversor):
    conversiones = {
        "km": 1000,
        "m": 1,
        "mi": 1609.344
    }