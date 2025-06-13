# Descripción:
#   Módulo para la conversión entre diferentes unidades de velocidad.
#   Proporciona métodos estáticos para convertir entre Kilometros/h, Metros/s y Millas/h.

class Velocidad:

    def kmh_to_mps(value: float = 1) -> float:
        return value / 3.6

    def mps_to_kmh(value: float = 1) -> float:
        return value * 3.6

    def mph_to_mps(value: float = 1) -> float:
        return value * 0.44704

    def mps_to_mph(value: float = 1) -> float:
        return value / 0.44704

    def kmh_to_mph(value: float = 1) -> float:
        return Velocidad.mps_to_mph(Velocidad.kmh_to_mps(value))

    def mph_to_kmh(value: float = 1) -> float:
        return Velocidad.mps_to_kmh(Velocidad.mph_to_mps(value))