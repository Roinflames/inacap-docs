# 🔹 Ejemplo 2 (individual): Conversión de lista a tupla
# Lista de compras editable
compras = ["pan", "leche", "huevos"]

# Convertimos a tupla para asegurar que no se modifique
compras_seguras = tuple(compras)

print("🛒 Tupla de compras (protegida):", compras_seguras)

# Intentar modificar la tupla (generará error)
try:
    compras_seguras[0] = "café"
except TypeError:
    print("❌ No se puede modificar una tupla. ¡Es inmutable!")
