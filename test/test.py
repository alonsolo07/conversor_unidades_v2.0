from src import Distancia, Masa, Velocidad, Temperatura

print(Distancia.convertir(5, "km", "mi"))         # ≈ 3.1069
print(Masa.convertir(1000, "g", "lb"))            # ≈ 2.2046
print(Velocidad.convertir(90, "kmh", "mph"))      # ≈ 55.9234
print(Temperatura.convertir(100, "c", "k"))       # 373.15