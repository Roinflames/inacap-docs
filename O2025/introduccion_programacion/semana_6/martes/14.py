# ✅ Ejemplo 4: Verificación segura de claves
usuario = {
    "nombre": "Rodrigo",
    "apellido": "Reyes",
    "edad": 35
}

print("🧍 Nombre:", usuario["nombre"])
print("📅 Edad:", usuario.get("edad"))

clave = "telefono"

if clave in usuario:
    print(f"📱 Teléfono: {usuario[clave]}")
else:
    print(f"❌ La clave '{clave}' no existe en el diccionario.")
