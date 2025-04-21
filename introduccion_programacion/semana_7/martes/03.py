# 1.3 Operaciones con las listas
nombres = ["Juan", "Pedro", "Maria", "Jose"]
ciudades = ["Santiago", "Valparaíso", "Concepción", "La Serena"]

# Concatenar lista
concatenadas = nombres + ciudades
print("\nConcatenación de listas: ", concatenadas, "\n")

# Obtener el largo de la lista
print("Largo de la lista nombres: ", len(nombres))
print("Largo de la lista ciudades: ", len(ciudades))
print("Largo de la lista concatenadas: ", len(concatenadas), "\n")

# Verificación de elemento de la lista
if "Juan" in nombres:
    print("Juan está en la lista de nombres", "\n")   
else:
    print("Elemento no encontrado")
    
# Repetir una lista en pantalla
print("Repetición de la lista nombres: ", nombres * 3, "\n")

# Recorrer una lista
contador = 1

for elemento in nombres:
    print("Elemento ", contador, ": ", elemento)
    contador += 1
    
# Limpiar una lista
nombres.clear()
print("Lista nombres después de limpiar: ", nombres, "\n")

# Inserción de un elemento a la lista en una posición específica 
nombres.insert(5, "Ana")
print("Lista nombres después de insertar Ana: ", nombres)
print("Lista nombres después de insertar Ana: ", nombres[0])
# print("Lista nombres después de insertar Ana: ", nombres[4])
print("Lista nombres después de insertar Ana: ", nombres[-1])
print("Lista nombres después de insertar Ana: ", nombres[-0], "\n")

nombres.insert(0, "Luis")
nombres.insert(0, "Pedro")
print("Lista nombres después de insertar: ", nombres, "\n")

# Eliminar y retornar el último elemento de la lista
print("Eliminar y retornar el último elemento de la lista: ", nombres.pop())
print("Lista nombres después de eliminar el último elemento: ", nombres, "\n")

# Eliminar y retornar un elemento de la lista indicando su índice
print("Eliminar y retornar el primer elemento de la lista: ", nombres.pop(0))
print("Lista nombres después de eliminar el primer elemento: ", nombres)