"""

Escribe un programa en Python que determine si un participante puede ingresar a una actividad. 
El ingreso está permitido sólo si el participante tiene entre 18 y 25 años, inclusive. 

"""

# Solicitar la edad del participante
edad = int(input("Por favor, ingrese su edad: "))

# Verificar si la edad está en el rango permitido usando operadores lógicos
if 18 <= edad <= 25:
    print("¡Puede ingresar a la actividad!")
else:
    print("Lo sentimos, no cumple con los requisitos de edad.")


# Verificar si la edad está en el rango permitido sin operadores lógicos
if edad >= 18:
    if edad <= 25:
        print("¡Puede ingresar a la actividad! (sin operadores lógicos)")
    else:
        print("Lo sentimos, no cumple con los requisitos de edad. (sin operadores lógicos)")
else:
    print("Lo sentimos, no cumple con los requisitos de edad. (sin operadores lógicos)")