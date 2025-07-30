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
🔐 Ejemplo 2: Evitar exposición de datos sensibles
Riesgo: fuga de información personal (PII - Personally Identifiable Information).
"""
import pandas as pd

# Supón que este DataFrame viene de una base de datos
df = pd.DataFrame({
    "id": [1, 2],
    "nombre": ["Ana", "Luis"],
    "email": ["ana@email.com", "luis@email.com"],
    "password": ["hash1", "hash2"]
})

# Antes de exportar o mostrar, eliminar campos sensibles
df_sanitizado = df.drop(columns=["email", "password"])
print(df_sanitizado)

