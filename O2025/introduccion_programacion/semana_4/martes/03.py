precio_original = 49.99
descuento_porcentaje = 15
precio_final = precio_original * (1 - descuento_porcentaje / 100)
print("El precio final del producto es:", precio_final)

# Mostrar el precio final con distintas cifras significativas
print("El precio final con 0 cifras significativas es:", round(precio_final, 0))
print("El precio final con 1 cifras significativas es:", round(precio_final, 1))
print("El precio final con 2 cifras significativas es:", round(precio_final, 2))
print("El precio final con 3 cifras significativas es:", round(precio_final, 3))
print("El precio final con 4 cifras significativas es:", round(precio_final, 4))
print("El precio final con 5 cifras significativas es:", round(precio_final, 5))