# Descripción:
#   Módulo para la conversión entre diferentes unidades de velocidad.
#   Proporciona métodos estáticos para convertir entre Kilometros/h, Metros/s y Millas/h.

from .conversor import Conversor

class Velocidad(Conversor):
    # Unidad base: metros por segundo (m/s)
    conversiones = {
        "kmh": 1000 / 3600,     # 1 km/h = 0.277777...
        "mps": 1,
        "mph": 1609.344 / 3600  # 1 mph = 0.44704
    }