# 1.2 Métodos de las listas
nombres = ["Juan", "Pedro", "Maria", "Jose"]

# Modificar los elementos de la lista
print("Nombres: ", nombres)
nombres[1] = "Karen"
print("Cambio el nombre del ìndice 1", nombres)

# Agregar los elementos de la lista
nombres.append("Luis")
nombres.insert(0, "Ana")
print("Agrego Luis al final y Ana al principio del arreglo: ", nombres)

# Eliminar los elementos de la lista
del nombres[0]
print("Elimino el primer elemento del arreglo/lista: ", nombres)
del nombres[len(nombres) - 1]
print("Elimino el último elemento del arreglo/lista: ", nombres)