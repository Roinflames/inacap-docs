# ✅ Ejemplo 3: Búsqueda segura en una lista (con control de errores)
frutas = ["manzana", "banana", "pera", "kiwi"]

buscar = input("🔍 ¿Qué fruta quieres buscar? ").strip().lower()

if buscar in frutas:
    print(f"✅ La fruta '{buscar}' está en la lista.")
else:
    print(f"❌ La fruta '{buscar}' no fue encontrada.")
