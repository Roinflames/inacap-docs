# prompt: solicitar notas a un usuario ingresandolas por teclado, una vez ingresadas, dar el mensaje de que no se pueden modificar despues de 48 horas. No utilizar try except

notas = []
cantidad_notas = int(input("Ingrese la cantidad de notas que desea ingresar: "))

for i in range(cantidad_notas):
  nota = float(input(f"Ingrese la nota {i+1}: "))
  notas.append(nota)

print("Las notas ingresadas son:", notas)
print("Recuerde que las notas no podrán ser modificadas después de 48 horas.")