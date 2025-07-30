# Su equipo de trabajo ha sido seleccionado para analizar desde el punto de vista de sistemas la biblioteca de INACAP Ñuñoa.
# Debe definir al menos un proceso a automatizar mediante un código escrito en Python.
# Se recomienda que este proceso sea el de "Préstamo de Libro", dónde debe considerar las variables o atributos que abstraigan:

# - Título del libro
# - Disponibilidad
# - Nombre de alumno/docente/funcionario
# - Fecha de préstamo
# - Fecha de devolución  
titulos = ["Libro1","Libro2","Libro3"]
disponibilidad = [True,False,True]
nombre = ["","",""]

def get_titulos():
    return titulos

def get_disponibilidad():
    return disponibilidad

def set_nombre():
    pass

def set_fecha_prestamo():
    pass

def set_fecha_devolucion():
    pass

def solicitar_libro(libro_solicitado):
    # consultar disponibilidad
    print(get_titulos())
    print(get_disponibilidad())
    # Si el libro está disponible, realizar préstamo
    if True: # libro_solicitado
        print(set_nombre())
        print(set_fecha_prestamo())
        print(set_fecha_devolucion())

i=0
for libro in titulos:
    print(libro, disponibilidad[i])
    i+=1

libro_solicitado = input("Ingrese nombre de libro a solicitar")
solicitar_libro(libro_solicitado)