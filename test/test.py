# test/test.py

from src import Distancia, Masa, Temperatura, Velocidad

print("DISTANCIA")
print(Distancia.km_to_mi(5))     # 5 km ≈ 3.1069 mi
print(Distancia.mi_to_km(3.1))   # 3.1 mi ≈ 4.989 km

print("\nMASA")
print(Masa.kg_to_lb(10))         # 10 kg ≈ 22.0462 lb
print(Masa.lb_to_kg(22))         # 22 lb ≈ 9.979 kg

print("\nTEMPERATURA")
print(Temperatura.c_to_f(0))     # 0 ºC = 32 ºF
print(Temperatura.f_to_k(32))    # 32 ºF = 273.15 K

print("\nVELOCIDAD")
print(Velocidad.kmh_to_mph(100))  # 100 km/h ≈ 62.137 mph
print(Velocidad.mph_to_kmh(60))   # 60 mph ≈ 96.5606 km/h