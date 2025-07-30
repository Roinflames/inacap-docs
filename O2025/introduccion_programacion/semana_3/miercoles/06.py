# Uso de break, continue y else en bucles
print("--- Control de stock ---")
cantidad_productos = int(input(f"Ingrese número de productos a analizar: "))

for i in range(0, cantidad_productos):
    stock = int(input(f"Ingrese stock del producto {i + 1}: "))
    
    if stock == 0:
        print("Se detectó un problema en el stock, deteniendo revisión.")
        break  # Sale del bucle
    print(f"Revisión {i + 1} completada.")
else:
    print("Todas las revisiones completadas sin problemas.")

print("--- Control de calidad de productos ---")
for i in range(0, cantidad_productos):
    # Opción 1: Comparar explícitamente la entrada
    estado = input(f"Ingrese estado del producto {i + 1} (True/False - 1/0): ")
    estado = estado.lower() in ["true", "1"]  # Convierte a booleano correctamente    
    print(estado)
    print(type(estado))
    
    # Opción 2: Convertir directamente a int
    estado = bool(int(input(f"Ingrese estado del producto {i + 1} (1 para True, 0 para False): ")))

    if estado == False:
        print("Producto defectuoso detectado, saltando revisión.")
        continue  # Salta la iteración actual
    print(f"Producto {i} aprobado.")