# Descripción:
#   Módulo para la conversión entre diferentes unidades de medicion de temperatura.
#   Proporciona métodos estáticos para convertir entre grados centigrados (°C), grados Kelvin (K) y Fahrenheit (°F).

class Temperatura:

    def c_to_f(value: float = 0) -> float:
        return (value * 9/5) + 32

    def f_to_c(value: float = 32) -> float:
        return (value - 32) * 5/9

    def c_to_k(value: float = 0) -> float:
        return value + 273.15

    def k_to_c(value: float = 273.15) -> float:
        return value - 273.15

    def f_to_k(value: float = 32) -> float:
        return Temperatura.c_to_k(Temperatura.f_to_c(value))

    def k_to_f(value: float = 273.15) -> float:
        return Temperatura.c_to_f(Temperatura.k_to_c(value))