# login_seguro.py
import sqlite3

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

usuario = input("Usuario: ")
password = input("Contraseña: ")

# Consulta segura con parámetros
cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND password = ?", (usuario, password))

if cursor.fetchone():
    print("Acceso concedido")
else:
    print("Acceso denegado")
