# Ejemplos de if, if-else, if-elif-else
empanada = "empanada"
bebida = "bebida"
dulce = "dulce"

stock_empanada = int(input(f"Ingrese el stock de producto {empanada}: "))
stock_bebida = int(input(f"Ingrese el stock de producto {bebida}: "))
stock_dulce = int(input(f"Ingrese el stock de producto {dulce}: "))

# Uso de if
if stock_empanada > 0:
    print(f"El producto {empanada} está disponible.")

if stock_bebida > 0:
    print(f"El producto {bebida} está disponible.")

if stock_dulce > 0:
    print(f"El producto {dulce} está disponible.")
    
# Uso de if-else
if stock_empanada > 0:
    print(f"Puede comprar {stock_empanada} {empanada}.")
else:
    print(f"Lo sentimos, no hay stock de {empanada}.")
    
if stock_bebida > 0:
    print(f"Puede comprar {stock_bebida} {bebida}.")
else:
    print(f"Lo sentimos, no hay stock de {bebida}.")

if stock_dulce > 0:
    print(f"Puede comprar {stock_dulce} {dulce}.")
else:
    print(f"Lo sentimos, no hay stock de {dulce}.")