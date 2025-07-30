# registro_inseguro.py

username = input("Usuario: ")
password = input("Contraseña: ")

# Guardando en archivo plano (inseguro)
with open("usuarios.txt", "a") as file:
    file.write(f"{username},{password}\n")

print("Usuario registrado.")
