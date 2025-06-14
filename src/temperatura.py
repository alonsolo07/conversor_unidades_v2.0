# Descripción:
#   Módulo para la conversión entre diferentes unidades de medicion de temperatura.
#   Proporciona métodos estáticos para convertir entre grados centigrados (°C), grados Kelvin (K) y Fahrenheit (°F).

class Temperatura:

    @staticmethod
    def convertir(valor, unidad_origen, unidad_destino):
        unidad_origen = unidad_origen.lower()
        unidad_destino = unidad_destino.lower()

        if unidad_origen == unidad_destino:
            return valor

        if unidad_origen == "c":
            if unidad_destino == "f":
                return (valor * 9/5) + 32
            elif unidad_destino == "k":
                return valor + 273.15

        elif unidad_origen == "f":
            if unidad_destino == "c":
                return (valor - 32) * 5/9
            elif unidad_destino == "k":
                return (valor - 32) * 5/9 + 273.15

        elif unidad_origen == "k":
            if unidad_destino == "c":
                return valor - 273.15
            elif unidad_destino == "f":
                return (valor - 273.15) * 9/5 + 32

        raise ValueError(f"Conversión no soportada: {unidad_origen} → {unidad_destino}")