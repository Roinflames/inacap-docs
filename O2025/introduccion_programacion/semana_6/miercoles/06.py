# registro_seguro.py
import bcrypt

username = input("Usuario: ")
password = input("Contraseña: ").encode('utf-8')

# Hasheando contraseña
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

with open("usuarios.txt", "a") as file:
    file.write(f"{username},{hashed.decode()}\n")

print("Usuario registrado con seguridad.")
