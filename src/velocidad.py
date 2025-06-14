"""
Clase para la conversión entre diferentes unidades de velocidad.
Proporciona métodos estáticos para convertir entre Kilometros/h, Metros/s y Millas/h.

Atributos:
conversiones (dict): Diccionario con factores de conversión a Metros/s (unidad base).

Métodos:
convertir(valor, unidad_origen, unidad_destino): Convierte un valor de una unidad a otra.
"""
from .conversor import Conversor

class Velocidad(Conversor):
    # Unidad base: metros por segundo (m/s)
    conversiones = {
        "kmh": 1000 / 3600,     # 1 km/h = 0.277777...
        "mps": 1,
        "mph": 1609.344 / 3600  # 1 mph = 0.44704
    }