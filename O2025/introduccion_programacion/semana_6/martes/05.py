# ✅ Ejemplo 4: Script grupal mini-proyecto (Inventario simple)
def mostrar_menu():
    print("\n📦 Menú del Inventario:")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Eliminar producto")
    print("4. Salir")

inventario = []

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        producto = input("Ingrese nombre del producto: ").strip()
        if producto:
            inventario.append(producto)
            print("✅ Producto agregado.")
        else:
            print("⚠️ El nombre no puede estar vacío.")

    elif opcion == "2":
        if inventario:
            print("🧾 Productos en inventario:")
            for i, prod in enumerate(inventario, start=1):
                print(f"{i}. {prod}")
        else:
            print("📭 Inventario vacío.")

    elif opcion == "3":
        try:
            eliminar = int(input("Ingrese número del producto a eliminar: "))
            if 1 <= eliminar <= len(inventario):
                eliminado = inventario.pop(eliminar - 1)
                print(f"🗑️ Producto '{eliminado}' eliminado.")
            else:
                print("⚠️ Número fuera de rango.")
        except ValueError:
            print("❌ Entrada no válida.")

    elif opcion == "4":
        print("👋 Saliendo del sistema...")
        break
    else:
        print("❌ Opción inválida.")
