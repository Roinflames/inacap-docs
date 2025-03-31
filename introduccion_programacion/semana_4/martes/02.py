edad_estudiante1 = 18
edad_estudiante2 = 21
promedio_edades = (edad_estudiante1 + edad_estudiante2) / 2
print("El promedio de edad de los estudiantes es:", promedio_edades)
print(f"El promedio de edad de los estudiantes es: { promedio_edades }")
print("---------------------------------------------------------------------")
variables = [var for var in locals() if var.startswith("edad_estudiante")]
print(variables)
cantidad_variables = len(variables)
print("Cantidad de variables:", cantidad_variables)
print("---------------------------------------------------------------------")
promedio_edades = (edad_estudiante1 + edad_estudiante2) / cantidad_variables
print("El promedio de edad de los estudiantes es:", promedio_edades)
print(f"El promedio de edad de los estudiantes es: { promedio_edades }")
print("---------------------------------------------------------------------")
print(locals())
print("---------------------------------------------------------------------")
print(globals())
print("---------------------------------------------------------------------")
print(dir())