# 3.2 Métodos de Tuplas
datos = {
    'nombre': 'Marcos',
    'apellido': 'Rojas',
    'edad': 26,
    'direccion': 'Balmaceda #1520',
    'ciudad': 'La Serena'
}
print("ITEMS: ")
# Método ITEMS ()
for elemento in datos.items():
    print(elemento)

print("\nKEYS: ")
# Método keys ( )
for elemento in datos.keys():
    print(elemento)

print("\nValues: ")
# Método values ( )
for elemento in datos.values():
    print(elemento)
    
print("\nCopy: ")
# Método copy ( )
copia = datos.copy()
print("Copia del Diccionario: ", copia)

print("\nClear: ")
# Método clear ( )
datos.clear()
print("Diccionario después de limpiar: ", datos)

print("\nGET: ")
# Método get ( )
valor1 = copia.get('nombre')
print("Valor de 'nombre' usando get: ", valor1) 
valor2 = copia.get('telefono')
print("Valor de 'telefono' usando get: ", valor2)

print("\nPOP: ")
# Método pop ( )
print(datos)
eliminado = copia.pop('nombre')
print("Elemento eliminado usando pop: ", eliminado)
print("Diccionario después de eliminar 'nombre': ", datos)

print("\nsetdefault: ")
# Método setdefault ( )
# Primera forma de uso: Funciona igual que el método get().
encontrado1 = copia.setdefault('direccion')
encontrado2 = copia.setdefault('telefono')
print("Elemento encontrado usando setdefault: ", encontrado1)
print("Elemento encontrado usando setdefault: ", encontrado2)

print("\nsetdefault: ")
# Método setdefault ( )
# Segunda forma de uso: Agrega un nuevo elemento al Diccionario si le pasamos la clave y el valor
copia.setdefault('telefono', '123456789')
print("Diccionario después de agregar 'telefono': ", copia)

print("\Dict: ")
# Recorriendo un Diccionario
for clave, valor in copia.items():
    print(clave, " ==> ", valor)