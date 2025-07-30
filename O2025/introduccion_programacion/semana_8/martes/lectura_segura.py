import sys

try:
    import pandas as pd
except ImportError:
    print("⚠️ El módulo 'pandas' no está instalado.")
    print("Puedes instalarlo ejecutando: pip install pandas")
    exit(1)

# Validación del argumento de línea de comandos
if len(sys.argv) < 2:
    print("❌ Uso: python lectura_segura.py <archivo.csv>")
    exit(1)

archivo = sys.argv[1]

try:
    # Lectura segura: no permite conversiones automáticas
    df = pd.read_csv(archivo, dtype=str)

    # Validación de columnas esperadas
    columnas_esperadas = {"id", "nombre", "email"}
    if not columnas_esperadas.issubset(df.columns):
        raise ValueError("El archivo no contiene todas las columnas necesarias: id, nombre, email")

    # Limpieza de datos
    df["email"] = df["email"].str.strip().str.lower()

    print("✅ Datos cargados y limpiados correctamente")
    print(df)

except FileNotFoundError:
    print(f"❌ El archivo '{archivo}' no se encuentra.")
except pd.errors.EmptyDataError:
    print("❌ El archivo está vacío o tiene un formato inválido.")
except ValueError as ve:
    print(f"❌ Error de validación: {ve}")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
