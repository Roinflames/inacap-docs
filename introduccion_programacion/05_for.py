frutas = ["manzana", "banana", "cereza", 1, 2, 3]
print("Esto es lo que escribe el for:")
for fruta in frutas:
    print(fruta)

print("Esto es lo que escribe el arreglo por cada índice:")
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
print(frutas[4])
print(frutas[5])

frutas[3] = "platanos"
print("Esto es el arreglo luego de modificar sus valores:")
print(frutas)