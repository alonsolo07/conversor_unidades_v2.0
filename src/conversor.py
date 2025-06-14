class Conversor:
    conversiones = {}  # Se define en las subclases

    def convertir(cls, valor, unidad_origen, unidad_destino):
        unidad_origen = unidad_origen.lower()
        unidad_destino = unidad_destino.lower()

        if unidad_origen == unidad_destino:
            return valor

        try:
            a_base = cls.conversiones[unidad_origen]
            de_base = cls.conversiones[unidad_destino]
        except KeyError:
            raise ValueError(f"Conversión no soportada: {unidad_origen} → {unidad_destino}")

        return valor * a_base / de_base