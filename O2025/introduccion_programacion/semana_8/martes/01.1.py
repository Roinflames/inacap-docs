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

try:
    import pandas as pd
except ImportError:
    print("⚠️ El módulo 'pandas' no está instalado.")
    print("Puedes instalarlo ejecutando: pip install pandas")
    exit(1)

try:
    # Lectura segura: deshabilita conversión automática de datos
    df = pd.read_csv("datos_usuarios_errores.csv", dtype=str)

    # Validación de columnas esperadas
    columnas_esperadas = {"id", "nombre", "email"}
    if not columnas_esperadas.issubset(df.columns):
        raise ValueError("❌ El archivo no contiene todas las columnas necesarias: id, nombre, email")

    # Limpieza de datos
    df["email"] = df["email"].str.strip().str.lower()

    print("✅ Datos cargados y limpiados correctamente")
    print(df)

except FileNotFoundError:
    print("❌ El archivo 'datos_usuarios.csv' no se encuentra en el directorio actual.")
except pd.errors.EmptyDataError:
    print("❌ El archivo está vacío o tiene un formato inválido.")
except ValueError as ve:
    print(f"❌ Error de validación: {ve}")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
