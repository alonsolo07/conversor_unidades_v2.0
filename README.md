# 🔄 Conversor de Unidades

**Conversor de Unidades** es una librería **Python** que facilita la conversión precisa entre distintas magnitudes físicas (distancia, masa, temperatura y velocidad), siguiendo buenas prácticas de programación y diseño modular.

---

## ✨ Características

| Categoría      | Ejemplos de unidades                                   |
|----------------|--------------------------------------------------------|
| Longitud       | m,  km,  mi                                              |
| Masa           | g,  kg,  lb                                              |
| Temperatura    | °C,  °F,  K                                              |
| Velocidad      | m/s,  km/h,  mph                                         |

- API clara (`convertir()` y funciones específicas por magnitud)
- Precisión basada en el paquete **pint**
- Conversión encadenada y formato de resultados configurable
- Manejo de errores (unidades incompatibles, divisiones por cero, etc.)
- Tipado estático con **type hints** y cobertura completa de tests

---

## 🗂️ Estructura del Proyecto

```
conversor-unidades/
├── src/
│   ├── __init__.py
│   ├── conversor.py
│   ├── longitud.py
│   ├── masa.py
│   ├── temperatura.py
│   ├── volumen.py
├── test/
│   └── test.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## 📦 Instalación

```bash
pip install conversor-unidades
```

> Requiere **Python 3.8+** y **pint 0.23+** para el motor de unidades.

---

## 🛠️ Puesta a punto

1. Clona este repositorio en la ruta que desees
   ```bash
   git clone https://github.com/alonsolo07/conversor_unidades_v2.0
   ```
2. Crea un entorno virtual y activalo
   ```bash
   python -m venv conversor_unidades_venv
   .\conversor_unidades_venv\Scripts\activate  # En Windows
   ```
3. Instala el paquete en modo editable  
   ```bash
   pip install -e .
   ```

---


## 🧰 Uso Básico

```python
from conversor_unidades import convertir

# Conversión genérica
km = convertir(12500, "m", "km")        # 12.5
```

---



## 🧪 Ejecutar Pruebas

```bash
pytest
```

---


## ✅ Buenas Prácticas Implementadas

1. **Programación Orientada a Objetos** con clases por categoría de unidades  
2. **Modularidad** y separación de responsabilidades  
3. **Documentación** completa con *docstrings* y ejemplos  
4. **Tipado Estático** con *mypy* y *type hints*  
5. **Cobertura de Pruebas** > 90 % con *pytest*  
6. **Manejo de Errores** para unidades no soportadas  

---

## 🚀 Roadmap

- Conversión con incertidumbre y propagación de error  
- Soporte para más magnitudes físicas (presión, potencia, etc.)  
- CLI interactiva (`conversor-cli`)  
- Compatibilidad con notebooks (*Jupyter-friendly*)  

---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. 

---

## 👤 Autor

Desarrollado por Alonso Lara Ordóñez. ¡Se agradecen *issues* y *pull requests*!