import sqlite3

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

usuario = input("Usuario: ")
password = input("Contraseña: ")

# SQL vulnerable
query = f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND password = '{password}'"
cursor.execute(query)

if cursor.fetchone():
    print("Acceso concedido")
else:
    print("Acceso denegado")
