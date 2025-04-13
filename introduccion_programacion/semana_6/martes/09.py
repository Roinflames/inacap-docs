# 🔹 Ejemplo 3 (expositivo): Devolver múltiples valores usando una tupla
# Función que retorna una tupla con operaciones matemáticas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    return (suma, resta)

resultado = operaciones_basicas(10, 5)

print("📦 Resultados:")
print("Suma:", resultado[0])
print("Resta:", resultado[1])
