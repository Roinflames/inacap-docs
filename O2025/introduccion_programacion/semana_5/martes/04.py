# 1.4. Aplicación de operadores lógicos

# and
estudia_introduccion = True
realiza_quiz = True

if estudia_introduccion and realiza_quiz:
    print("El estudiante aprobará la evaluación sumativa.") 
    
# or
licencia_vencida = True
nueva_version_disponible = True

if licencia_vencida or nueva_version_disponible:
    print("Se actualizará el paquete de software.")

# not
usuario_bloqueado = False

if not usuario_bloqueado:
    print("El usuario puede acceder al sistema.")
    
# combinacion de operadores lógicos
es_miembro = True
monto_compra = 120000

if es_miembro and monto_compra > 50000:
    print("El cliente es elegible para un descuento.")

# EXPRESIONES ANIDADAS
es_electrico = False
rendimiento_kpl = 15

if es_electrico or rendimiento_kpl > 14: # kpl: Kilometros por litro
    print("El vehiculo es considerado eficiente.")
