# ✅ Ejemplo 1: Validación de entrada
# Riesgo: Inyección de comandos

# ¡Peligroso!
import os

usuario = input("Ingresa tu nombre de usuario: ")
os.system(f"echo Bienvenido {usuario}")

import os
import shlex

usuario = input("Ingresa tu nombre de usuario: ")
usuario_seguro = shlex.quote(usuario)
os.system(f"echo Bienvenido {usuario_seguro}")
