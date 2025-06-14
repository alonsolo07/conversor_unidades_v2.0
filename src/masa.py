"""
Clase para la conversión entre diferentes unidades de masa.
Proporciona métodos estáticos para convertir entre kilógramos, gramos y libras.

Atributos:
conversiones (dict): Diccionario con factores de conversión a kilógramos (unidad base).

Métodos:
convertir(valor, unidad_origen, unidad_destino): Convierte un valor de una unidad a otra.
"""

from .conversor import Conversor

class Masa(Conversor):
    # Unidad base: kilogramo
    conversiones = {
        "kg": 1,
        "g": 0.001,
        "lb": 0.453592
    }