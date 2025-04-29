# 1.1. Pandas
"""
Pandas es una biblioteca de código abierto que proporciona estructuras de datos y herramientas de análisis de datos de alto rendimiento 
y fáciles de usar para el lenguaje de programación Python. 
Es especialmente útil para manipular y analizar datos tabulares y series temporales.
"""
"""
🧪 Ejemplo 1: Validación de entradas al cargar datos CSV
Riesgo: archivos manipulados maliciosamente (por ejemplo, CSV con fórmulas maliciosas como =cmd|'/C calc.exe'!A0 en Excel).
"""
"""
🐛 Ejemplo 3: Prevención de errores por datos corruptos
Riesgo: fallos o comportamientos impredecibles por datos mal estructurados.
"""
import pandas as pd

# Validación estricta de tipos de datos
df = pd.read_csv("datos_usuarios_errores.csv")

# Asegurar que la columna edad solo contenga números enteros positivos
df = df[pd.to_numeric(df["edad"], errors="coerce").notnull()]
df["edad"] = df["edad"].astype(int)
df = df[df["edad"] > 0]
print(df)
