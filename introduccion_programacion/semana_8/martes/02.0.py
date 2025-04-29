# 1.2. NumPy
"""
NumPy es una biblioteca fundamental para la computación científica en Python. 
Proporciona un objeto de matriz multidimensional de alto rendimiento y herramientas para trabajar con estas matrices. 
NumPy es esencial para operaciones numéricas eficientes en Python y es comúnmente utilizado junto con Pandas.
"""
"""
✅ Ejemplo seguro usando NumPy junto a Pandas
Este ejemplo:

Lee un archivo CSV con edades.

Usa NumPy para convertir a números.

Filtra valores inválidos o peligrosos (como negativos o NaN).

Calcula estadísticas con validación.
"""

import sys

try:
    import pandas as pd
    import numpy as np
except ImportError:
    print("⚠️ Necesitas instalar pandas y numpy.")
    print("Ejecuta: pip install pandas numpy")
    exit(1)

# Validar argumento
if len(sys.argv) < 2:
    print("❌ Uso: python 02.py <archivo.csv>")
    exit(1)

archivo = sys.argv[1]

try:
    df = pd.read_csv(archivo, dtype=str)

    if not {"id", "nombre", "edad"}.issubset(df.columns):
        raise ValueError("El archivo debe contener las columnas: id, nombre, edad")

    # Convertir edad a números usando NumPy
    edades = pd.to_numeric(df["edad"], errors="coerce").values
    edades = np.array(edades)

    # Filtrar edades inválidas: NaN, negativas o cero
    edades_validas = edades[~np.isnan(edades) & (edades > 0)]

    if len(edades_validas) == 0:
        print("❌ No hay datos de edad válidos.")
    else:
        print("✅ Estadísticas seguras de edad:")
        print(f"- Mínimo: {np.min(edades_validas)}")
        print(f"- Máximo: {np.max(edades_validas)}")
        print(f"- Promedio: {np.mean(edades_validas):.2f}")
        print(f"- Desviación estándar: {np.std(edades_validas):.2f}")

except FileNotFoundError:
    print(f"❌ El archivo '{archivo}' no se encuentra.")
except Exception as e:
    print(f"❌ Error inesperado: {e}")

