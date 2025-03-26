# Ejemplo de bucle while sin estructuras de datos
print("--- Contando clientes en la fila ---")
clientes = int(input(f"Ingrese número de clientes: "))
contador = 0

while contador < clientes:
    print(f"-- índice {contador} --")
    contador += 1
    print(f"Cliente número {contador} atendido.")