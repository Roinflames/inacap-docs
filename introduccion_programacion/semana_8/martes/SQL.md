✅ 1. Prevención de Inyección SQL
Qué se previno:
El archivo CSV incluía una entrada maliciosa:

    3,Malicioso,"'); DROP TABLE usuarios;--"

Si se usara una inserción de SQL directa con string.format() o f-strings, esta línea podría borrar la tabla completa.

Cómo se evitó:

    cursor.execute("INSERT INTO ... VALUES (?, ?, ?)", (id_val, nombre, email))

El uso de parámetros con ? evita que el contenido se interprete como parte del SQL. Todo se trata como texto literal.

✅ 2. Validación de columnas
Qué se previno:
Archivos CSV mal formados (con columnas faltantes o mal nombradas) podrían provocar errores o insertar basura.

Cómo se evitó:

    if not columnas_requeridas.issubset(df.columns):
        raise ValueError("...")

✅ 3. Filtrado y limpieza de datos antes de insertarlos
Qué se previno:
Inserción de espacios en blanco, correos en mayúsculas, IDs no válidos, etc.

Cómo se evitó:

    nombre = row["nombre"].strip()
    email = row["email"].strip().lower()
    id_val = int(row["id"])
    ✅ 4. Manejo de errores por fila
    Qué se previno:
    Que una sola fila mal escrita interrumpiera toda la carga de datos.

Cómo se evitó:

    try:
        ...
    except Exception as row_error:
        print(f"⚠️ Fila con error: {row.to_dict()} → {row_error}")

✅ 5. Reintentos seguros

El uso de INSERT OR IGNORE previene que un ID duplicado o mal ingreso detone un crash del programa.

🧠 Conclusión:

El script aplicó principios de programación segura al:

    Validar entradas externas.
    Usar parámetros en consultas.
    Manejar errores con gracia.
    Evitar confiar ciegamente en archivos de terceros.