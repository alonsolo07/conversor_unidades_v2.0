# 🔄 Conversor de Unidades

**Conversor de Unidades** es una librería **Python** que facilita la conversión precisa entre distintas magnitudes físicas (longitud, masa, temperatura, tiempo, volumen y más), siguiendo buenas prácticas de programación y diseño modular.

---

## 📦 Instalación

```bash
pip install conversor-unidades
```

> Requiere **Python 3.8+** y **pint 0.23+** para el motor de unidades.

---

## ✨ Características

| Categoría      | Ejemplos de unidades                                   |
|----------------|--------------------------------------------------------|
| Longitud       | m,  km,  mi                                              |
| Masa           | g,  kg,  lb                                              |
| Temperatura    | °C,  °F,  K                                              |
| Velocidad      | m/s,  km/h,  mph                                         |

- API clara (`convertir()` y funciones específicas por magnitud)
- Precisión basada en el paquete **pint**
- Conversión encadenada y formato de resultados configurable
- Manejo de errores (unidades incompatibles, divisiones por cero, etc.)
- Tipado estático con **type hints** y cobertura completa de tests

---

## 🧰 Uso Básico

```python
from conversor_unidades import convertir, Longitud, Temperatura

# Conversión genérica
km = convertir(12_500, origen="m", destino="km")        # 12.5

# Conversión con clases helper
metros = Longitud.to_metros(3, unidad_origen="ft")      # 0.9144
celsius = Temperatura.to_celsius(68, unidad_origen="F") # 20.0
```

### Conversión Encadenada

```python
from conversor_unidades import convertir

# 5 millas → metros → kilómetros
resultado = convertir(5, "mi", "m").pipe(
    lambda m: convertir(m, "m", "km")
)
# 8.04672
```

---

## 🗂️ Estructura del Proyecto

```
conversor-unidades/
├── src/
│   └── conversor_unidades/
│       ├── __init__.py
│       ├── core.py
│       ├── excepciones.py
│       ├── categorias/
│       │   ├── base.py
│       │   ├── longitud.py
│       │   ├── masa.py
│       │   ├── temperatura.py
│       │   └── volumen.py
├── tests/
│   └── test_conversor.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🧪 Ejecutar Pruebas

```bash
pytest
```

---

## 🛠️ Desarrollo

1. Clona este repositorio  
2. Crea un entorno virtual  
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. Instala dependencias de desarrollo  
   ```bash
   pip install -r requirements.txt
   ```
4. Instala el paquete en modo editable  
   ```bash
   pip install -e .
   ```

---

## ✅ Buenas Prácticas Implementadas

1. **Programación Orientada a Objetos** con clases por categoría de unidades  
2. **Modularidad** y separación de responsabilidades  
3. **Documentación** completa con *docstrings* y ejemplos  
4. **Tipado Estático** con *mypy* y *type hints*  
5. **Cobertura de Pruebas** > 90 % con *pytest*  
6. **Manejo de Errores** específico mediante excepciones personalizadas  
7. **CI/CD** con GitHub Actions (lint, tests, build)  
8. **Código Limpio** y estilo consistente con *black* y *isort*  

---

## 🚀 Roadmap

- Conversión con incertidumbre y propagación de error  
- Soporte para más magnitudes físicas (presión, potencia, etc.)  
- CLI interactiva (`conversor-cli`)  
- Compatibilidad con notebooks (*Jupyter-friendly*)  

---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

---

## 👤 Autor

Desarrollado por **[Tu Nombre]**. ¡Se agradecen *issues* y *pull requests*!