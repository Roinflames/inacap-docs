# 1.5. CSV
"""
Es una herramienta incorporada que permite leer y escribir archivos CSV (Comma-Separated Values), 
que son un formato popular para almacenar datos tabulares. 
Los archivos CSV están formateados en texto plano, 
donde cada línea representa una fila de datos y los valores están separados por comas u otros delimitadores.

La librería CSV ofrece un conjunto de funciones y opciones para manejar archivos CSV de manera eficiente, 
como la lectura/escritura de diccionarios en lugar de listas, el manejo de archivos con diferentes formatos de línea, etc. 
"""
"""
El módulo csv es parte de la biblioteca estándar de Python, por lo que no necesitas instalar nada extra.
Ejemplo básico de lectura de un archivo CSV:
"""
import csv

with open('usuarios.csv', newline='', encoding='utf-8') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(fila)
