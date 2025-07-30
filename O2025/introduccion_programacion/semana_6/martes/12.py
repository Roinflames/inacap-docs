# ✅ Ejemplo 2: Agregar y modificar datos
usuario = {
    "nombre": "Rodrigo",
    "apellido": "Reyes",
    "edad": 35
}

print("🧍 Nombre:", usuario["nombre"])
print("📅 Edad:", usuario.get("edad"))

# Agregar clave nueva
usuario["correo"] = "rodrigo@correo.cl"

# Modificar edad
usuario["edad"] = 36

print("📧 Correo actualizado:", usuario["correo"])
