# Descripción:
#   Módulo para la conversión entre diferentes unidades de masa.
#   Proporciona métodos estáticos para convertir entre kilógramos, gramos y libras.

class Masa:

    def kg_to_lb(value: float = 1) -> float:
        return value * 2.20462

    def lb_to_kg(value: float = 1) -> float:
        return value / 2.20462

    def kg_to_g(value: float = 1) -> float:
        return value * 1000

    def g_to_kg(value: float = 1) -> float:
        return value / 1000

    def lb_to_g(value: float = 1) -> float:
        return Masa.kg_to_g(Masa.lb_to_kg(value))

    def g_to_lb(value: float = 1) -> float:
        return Masa.kg_to_lb(Masa.g_to_kg(value))