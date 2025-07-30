# 🔹 Ejemplo 4 (grupal): Mini script para registro de coordenadas GPS
# Cada coordenada es una tupla (latitud, longitud)
coordenadas = []

print("🌎 Registro de coordenadas GPS:")
for i in range(3):
    try:
        lat = float(input(f"Ingrese latitud {i+1}: "))
        lon = float(input(f"Ingrese longitud {i+1}: "))
        punto = (lat, lon)
        coordenadas.append(punto)
    except ValueError:
        print("⚠️ Entrada inválida. Usa números decimales.")

print("\n📍 Coordenadas registradas:")
for c in coordenadas:
    print(f"→ Latitud: {c[0]}, Longitud: {c[1]}")
