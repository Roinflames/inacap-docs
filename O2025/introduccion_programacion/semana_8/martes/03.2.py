# 1.3. SQLite
"""
SQLite es una biblioteca de software que proporciona un motor de base de datos SQL ligero y autónomo. 
SQLite3 es un módulo de Python que te permite interactuar con bases de datos SQLite desde Python. 
Es ideal para proyectos que requieren una base de datos simple y fácil de usar sin la necesidad de un servidor de base de datos separado.
"""
"""
🎯 Objetivos:
Leer datos desde CSV con pandas.

Insertarlos en una base SQLite usando sqlite3.

Evitar inyección SQL usando parámetros seguros (?).

Mostrar cómo validar antes de insertar.
"""
import sys
import sqlite3
import pandas as pd

# Validar argumento
if len(sys.argv) < 2:
    print("❌ Uso: python 03.py <archivo.csv>")
    exit(1)

archivo_csv = sys.argv[1]

try:
    df = pd.read_csv(archivo_csv, dtype=str)
    columnas_requeridas = {"id", "nombre", "email"}
    if not columnas_requeridas.issubset(df.columns):
        raise ValueError("❌ El archivo debe tener columnas: id, nombre, email")

    # Conectar a SQLite (se crea si no existe)
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    # Crear tabla de forma segura
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)

    # Limpiar y preparar los datos
    for _, row in df.iterrows():
        try:
            id_val = int(row["id"])
            nombre = row["nombre"].strip()
            email = row["email"].strip().lower()

            # Código VULNERABLE a inyección SQL
            query_vulnerable = f"INSERT OR IGNORE INTO usuarios (id, nombre, email) VALUES ('{id_val}', '{nombre}', '{email}')"
            print(f"\nEjecutando (VULNERABLE): {query_vulnerable}")
            try:
                cursor.execute(query_vulnerable)
                conn.commit()
                print("✅ Inserción (VULNERABLE) exitosa (¡esto NO debería pasar en un sistema seguro!).")
            except sqlite3.Error as e:
                print(f"❌ Error al ejecutar (VULNERABLE): {e}")

        except ValueError as ve:
            print(f"⚠️ Error de valor en fila: {row.to_dict()} → {ve}")
        except Exception as row_error:
            print(f"⚠️ Otro error en fila: {row.to_dict()} → {row_error}")

    conn.commit()
    print("✅ Datos insertados correctamente.")
    print("👁️‍🗨️ Usuarios en la base de datos:")
    for fila in cursor.execute("SELECT * FROM usuarios"):
        print(fila)

    conn.close()

except FileNotFoundError:
    print(f"❌ El archivo '{archivo_csv}' no fue encontrado.")
except pd.errors.EmptyDataError:
    print("❌ El archivo está vacío o malformado.")
except sqlite3.Error as db_error:
    print(f"❌ Error en la base de datos: {db_error}")
except Exception as e:
    print(f"❌ Error inesperado: {e}")