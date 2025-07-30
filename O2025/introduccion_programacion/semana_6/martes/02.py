"""
Actividades prácticas

1. Manipulación de Listas
Los estudiantes resuelven ejercicios prácticos que implican:

Crear, modificar y recorrer listas.

Aplicar operaciones seguras como validación de índices.

Usar funciones propias para evitar duplicación de código.

Aplicar principios de programación segura como control de excepciones.
"""
# ✅ Ejemplo 1: Manipulación básica de listas con validación

# Crear una lista con validación de entrada
numeros = []

try:
    cantidad = int(input("¿Cuántos números quieres ingresar? "))
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a cero.")

    for i in range(cantidad):
        while True:
            try:
                num = float(input(f"Ingrese el número {i+1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("⚠️ Entrada no válida. Por favor ingresa un número.")

    print("\n✅ Lista ingresada con éxito:", numeros)

except ValueError as ve:
    print("❌ Error:", ve)
