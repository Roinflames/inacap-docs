# Ejemplos de if, if-else, if-elif-else
producto = "empanada"
stock = int(input(f"Ingrese el stock del producto {producto}: "))

# Uso de if
if stock > 0:
    print(f"El producto {producto} está disponible.")

# Uso de if-else
if stock > 0:
    print(f"Puede comprar {producto}.")
else:
    print(f"Lo sentimos, no hay stock de {producto}.")