# 3.1 Declarando el Diccionario
# Declaramos un Diccionario
datos = {
    'nombre': 'Marcos',
    'apellido': 'Rojas',
    'edad': 26,
    'direccion': 'Balmaceda #1520',
    'ciudad': 'La Serena'
}

# Acceder a los elementos del Diccionario
print("Acceder al elemento 'nombre' del Diccionario: ", datos['nombre'])
print("Acceder al elemento 'apellido' del Diccionario: ", datos['apellido'])
print("Acceder al elemento 'edad' del Diccionario: ", datos['edad'])
print("Acceder al elemento 'direccion' del Diccionario: ", datos['direccion'])
print("Acceder al elemento 'ciudad' del Diccionario: ", datos['ciudad'])

# Modificar los elementos del Diccionario
datos['nombre'] = 'Teresa'
datos['apellido'] = 'Novoa'
print("Modificar los elementos del Diccionario: ", datos)

# Agregar un elemento al Diccionario
datos['telefono'] = '123456789'
print("Agregar un elemento al Diccionario: ", datos)

# Eliminar un elemento del Diccionario
del datos['direccion']
print("Eliminar elemento 'direccion' del Diccionario: ", datos)   