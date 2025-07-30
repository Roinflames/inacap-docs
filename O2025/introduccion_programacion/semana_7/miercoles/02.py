# ✅ Ejemplo 2: Contraseñas en texto plano
# Riesgo: Fugas de contraseñas
usuarios = {"admin": "1234"}  # ¡Nunca guardar contraseñas así!
print(usuarios)

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

usuarios = {"admin": hash_password("1234")}  # Contraseña en hash
print(usuarios)
