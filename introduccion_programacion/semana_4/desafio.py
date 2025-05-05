# Su equipo de trabajo ha sido seleccionado para analizar desde el punto de vista de sistemas la biblioteca de INACAP Ñuñoa.
# Debe definir al menos un proceso a automatizar mediante un código escrito en Python.
# Se recomienda que este proceso sea el de "Préstamo de Libro", dónde debe considerar las variables o atributos que abstraigan:

# - Título del libro
# - Disponibilidad
# - Nombre de alumno/docente/funcionario
# - Fecha de préstamo
# - Fecha de devolución  
from datetime import datetime, timedelta
titulos = ["Libro1","Libro2","Libro3"]
disponibilidad = [True,True,True]
nombre = ["","",""]
fecha_prestamo = [datetime.now(),datetime.now(),datetime.now()]
fecha_devolucion = [datetime.now(),datetime.now(),datetime.now()]

def get_titulos():
    return titulos

def get_disponibilidad():
    return disponibilidad

def set_nombre(indice):
    nombre[indice] = input("Ingrese nombre de quien solicitó el libro:\n")

def set_fecha_devolucion(indice):
    for fecha in fecha_prestamo:
        fecha_devolucion[indice] += timedelta(days=7)

def show_resultado(indice):
    print(
        "Solicitante: ", nombre[indice], ".\n" ,
        "Libro solicitado: ", titulos[indice], ".\n" ,
        "Fecha de prestamo: ", fecha_prestamo[indice], ".\n" ,
        "Fecha de devolucion: ", fecha_devolucion[indice], ".\n" ,
        )

def solicitar_libro(libro_solicitado):
    i=0
    indice=None

    for libro in titulos:
        if libro_solicitado == titulos[i]:
            indice = i
        print(libro, disponibilidad[i], indice)
        i+=1

    if indice != None:
        set_nombre(indice)
        set_fecha_devolucion(indice)
        show_resultado(indice)

libro_solicitado = input("Ingrese nombre de libro a solicitar:\n")
solicitar_libro(libro_solicitado)
