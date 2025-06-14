# Descripción:
#   Módulo para la conversión entre diferentes unidades de distancia.
#   Proporciona métodos estáticos para convertir entre kilómetros, metros y millas.

from .conversor import Conversor

class Distancia(Conversor):
    # Todas las unidades se convierten a "metro" como base
    conversiones = {
        "km": 1000,
        "m": 1,
        "mi": 1609.344
    }