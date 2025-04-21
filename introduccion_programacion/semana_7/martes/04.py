# 2.1 Declaramos una Tupla
tupla_1_int = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla_2_float = (1.5, 2.5, 3.5, 4.5, 5.5)
tupla_3_str = ("Juan", "Pedro", "Maria", "Jose")
tupla_4_bool = (True, False, True, False, False, True, False)
tupla_5_mixta = ("Juan", 2.5, True, 3.4, "Maria", 5.6, False, 7.8)

# ACCEDER A LA TUPLA
print("\nAcceder a la Tupla: ", tupla_1_int[2])
print("Acceder a la Tupla: ", tupla_2_float[2])
print("Acceder a la Tupla: ", tupla_3_str[2])
print("Acceder a la Tupla: ", tupla_4_bool[2])
print("Acceder a la Tupla: ", tupla_5_mixta[2], "\n")

# Acceder a una rebanada de la Tupla
print("Acceder a una rebanada de la Tupla: (del segundo ìndice al quinto elemento)", tupla_1_int[2:5])
print("Acceder a una rebanada de la Tupla: (del primer índice al quinto elemento)", tupla_2_float[1:4])
print("Acceder a una rebanada de la Tupla: (del índice 0 al segundo elemento) ", tupla_3_str[0:2])
print("Acceder a una rebanada de la Tupla: (desde el tercer índice) ", tupla_4_bool[3:], "\n")

# Obtener la longitud de una Tupla
print("Obtener la longitud de una Tupla: ", len(tupla_1_int))
print("Obtener la longitud de una Tupla: ", len(tupla_2_float))
print("Obtener la longitud de una Tupla: ", len(tupla_3_str))
print("Obtener la longitud de una Tupla: ", len(tupla_4_bool))
print("Obtener la longitud de una Tupla: ", len(tupla_5_mixta), "\n")

# Verificar un elemento dentro de la tupla
print("Verificar un elemento dentro de la tupla: ", 2 in tupla_1_int)
print("Verificar un elemento dentro de la tupla: ", 2 in tupla_2_float)
print("Verificar un elemento dentro de la tupla: ", "Juan" in tupla_3_str)
print("Verificar un elemento dentro de la tupla: ", "Juan" in tupla_4_bool)
print("Verificar un elemento dentro de la tupla: ", "Juan" in tupla_5_mixta, "\n")

# Verificar un elemento fuera de la tupla
print("Verificar un elemento fuera de la tupla: ", 20 not in tupla_1_int)
print("Verificar un elemento fuera de la tupla: ", 20 not in tupla_2_float)
print("Verificar un elemento fuera de la tupla: ", "Juan" not in tupla_3_str)
print("Verificar un elemento fuera de la tupla: ", "Juan" not in tupla_4_bool)
print("Verificar un elemento fuera de la tupla: ", "Juan" not in tupla_5_mixta, "\n")

# Concatenar tuplas
print("Concatenar tuplas: ", tupla_1_int + tupla_2_float)

# Obtener el valor mínimo de la tupla
print("Obtener el valor mínimo de la tupla 1: ", min(tupla_1_int))
print("Obtener el valor mínimo de la tupla 2: ", min(tupla_2_float))

# Obtener el valor máximo de la tupla
print("Obtener el valor máximo de la tupla 1: ", max(tupla_1_int))
print("Obtener el valor máximo de la tupla 2: ", max(tupla_2_float))

# Obtener la cantidad de ocurrencias
print("Obtener la cantidad de ocurrencias de un elemento en la tupla 1: ", tupla_1_int.count(2))
print("Obtener la cantidad de ocurrencias de un elemento en la tupla 2: ", tupla_2_float.count(2.5))

# Borrar una tupla
del tupla_1_int
del tupla_2_float