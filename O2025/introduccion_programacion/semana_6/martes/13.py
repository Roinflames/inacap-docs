# ✅ Ejemplo 3: Recorrer diccionario
usuario = {
    "nombre": "Rodrigo",
    "apellido": "Reyes",
    "edad": 35
}

print("🧍 Nombre:", usuario["nombre"])
print("📅 Edad:", usuario.get("edad"))

for clave, valor in usuario.items():
    print(f"{clave}: {valor}")
