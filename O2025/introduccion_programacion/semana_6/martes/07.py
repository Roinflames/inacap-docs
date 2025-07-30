# 🔹 Ejemplo 1 (individual): Acceso y recorrido de tupla
# Tupla con datos personales
persona = ("Rodrigo", "Reyes", 35)

print(f"Nombre: {persona[0]}")
print(f"Apellido: {persona[1]}")
print(f"Edad: {persona[2]}")

# Recorrido
print("\n🔁 Recorriendo la tupla:")
for dato in persona:
    print(f"- {dato}")
