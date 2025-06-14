# Descripción:
#   Módulo para la conversión entre diferentes unidades de masa.
#   Proporciona métodos estáticos para convertir entre kilógramos, gramos y libras.

from .conversor import Conversor

class Masa(Conversor):
    # Unidad base: kilogramo
    conversiones = {
        "kg": 1,
        "g": 0.001,
        "lb": 0.453592
    }