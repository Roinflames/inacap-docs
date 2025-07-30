"""
Actividades prácticas

2. Desarrollo de Scripts
A través de ejemplos expositivos y guiados, los estudiantes crean scripts que:

Utilizan listas para almacenar y procesar datos.

Incluyen entradas del usuario validadas (validación de tipo y rango).

Entregan salidas limpias y organizadas.

Demuestran el uso de funciones seguras como try-except, validación de inputs y límites de acceso.
"""
# ✅ Ejemplo 2: Script que calcula promedio de una lista (seguro)

def calcular_promedio(lista):
    if not lista:
        return None
    return sum(lista) / len(lista)

# Lista segura (validada anteriormente)
datos = [10, 20, 30, 40]

promedio = calcular_promedio(datos)
if promedio is not None:
    print(f"✅ El promedio es: {promedio}")
else:
    print("⚠️ La lista está vacía. No se puede calcular el promedio.")
