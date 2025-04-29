# 1.1. Pandas
"""
Pandas es una biblioteca de código abierto que proporciona estructuras de datos y herramientas de análisis de datos de alto rendimiento 
y fáciles de usar para el lenguaje de programación Python. 
Es especialmente útil para manipular y analizar datos tabulares y series temporales.
"""

import pandas as pd

# Lectura segura: deshabilitar conversión automática de datos peligrosos
df = pd.read_csv("datos_usuarios.csv", dtype=str)

# Validación de columnas esperadas
columnas_esperadas = {"id", "nombre", "email"}
if not columnas_esperadas.issubset(df.columns):
    raise ValueError("Archivo no contiene las columnas necesarias")

# Limpieza de datos
df["email"] = df["email"].str.strip().str.lower()
