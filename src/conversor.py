class Conversor:
    conversiones = {}  # Se define en las subclases

    """
        Convierte un valor de una unidad de distancia a otra.

        Args:
            valor (float): El valor numérico a convertir.
            unidad_origen (str): Unidad de origen (ej: 'km', 'm', 'mi').
            unidad_destino (str): Unidad destino.

        Returns:
            float: Valor convertido en la unidad destino.

        Raises:
            ValueError: Si la conversión entre unidades no está soportada.
    """
    @classmethod
    def convertir(cls, valor: float, unidad_origen: str, unidad_destino: str) -> float:
        unidad_origen = unidad_origen.lower()
        unidad_destino = unidad_destino.lower()

        if unidad_origen == unidad_destino:
            return valor

        try:
            factor_origen = cls.conversiones[unidad_origen]
            factor_destino = cls.conversiones[unidad_destino]
        except KeyError:
            raise ValueError(f"Conversión no soportada: {unidad_origen} → {unidad_destino}")


        # Convierte el valor a la unidad base y luego a la unidad destino
        valor_en_base = valor * factor_origen
        valor_convertido = valor_en_base / factor_destino
        return valor_convertido