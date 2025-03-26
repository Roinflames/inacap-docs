# Uso de if-elif-else
hora = int(input(f"Ingrese horario actual, sin minutos: "))

if hora < 12:
    print("Estamos en horario de desayuno.")
elif 12 <= hora < 15:
    print("Estamos en horario de almuerzo.")
elif 15 <= hora < 18:
    print("Estamos en horario de once.")
else:
    print("El casino está cerrado.")