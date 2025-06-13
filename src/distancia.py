# Descripción:
#   Módulo para la conversión entre diferentes unidades de distancia.
#   Proporciona métodos estáticos para convertir entre kilómetros, metros y millas.

class Distancia:

    def km_to_m(value: float = 1) -> float:
        return value * 1000

    def m_to_km(value: float = 1) -> float:
        return value / 1000

    def m_to_mi(value: float = 1) -> float:
        return value / 1609.344

    def mi_to_m(value: float = 1) -> float:
        return value * 1609.344

    def km_to_mi(value: float = 1) -> float:
        return Distancia.m_to_mi(Distancia.km_to_m(value))

    def mi_to_km(value: float = 1) -> float:
        return Distancia.m_to_km(Distancia.mi_to_m(value))