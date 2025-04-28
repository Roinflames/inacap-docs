# Archivo base: main.py

clientes = {}
pedidos = {}

def cargar_clientes(nombre_archivo):
    """Lee el archivo de clientes y carga los datos en el diccionario 'clientes'"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            primera_linea = archivo.readline()
            if not primera_linea:
                print(f"⚠️ El archivo '{nombre_archivo}' está vacío.")
                return
            
            for linea in archivo:
                partes = linea.strip().split(',')
                if len(partes) == 2:
                    try:
                        id_cliente = int(partes[0])
                        nombre = partes[1]
                        clientes[id_cliente] = nombre
                    except ValueError:
                        print(f"❌ Error de datos en línea: {linea.strip()}")
                        continue
    except FileNotFoundError:
        print(f"🚫 Archivo '{nombre_archivo}' no encontrado.")

def cargar_pedidos(nombre_archivo):
    """Lee el archivo de pedidos y carga los datos en el diccionario 'pedidos'"""
    pass

def mostrar_clientes():
    """Muestra todos los clientes cargados"""
    pass

def mostrar_pedidos():
    """Muestra todos los pedidos cargados"""
    pass

def buscar_pedidos_por_cliente(id_cliente):
    """Muestra los pedidos correspondientes a un cliente dado"""
    pass

def mostrar_estadisticas():
    """Muestra estadísticas de los pedidos: Total de ventas, Promedio de pedidos, Pedido más alto, Pedido más bajo"""
    pass

def menu():
    while True:
        print("\n📚 Menú:")
        print("1. Ver clientes")
        print("2. Ver pedidos")
        print("3. Ver estadísticas")
        print("4. Buscar pedidos por cliente")
        print("5. Salir")

        opcion = input("Elija una opción (1-5): ")

        if opcion == '1':
            mostrar_clientes()
        elif opcion == '2':
            mostrar_pedidos()
        elif opcion == '3':
            mostrar_estadisticas()
        elif opcion == '4':
            buscar_pedidos_por_cliente()
        elif opcion == '5':
            print("👋 Saliendo del programa...")
            break
        else:
            print("⚠️ Opción inválida. Intente nuevamente.")

def main():
    cargar_clientes("clientes.txt")
    cargar_pedidos("pedidos.txt")
    menu()

if __name__ == "__main__":
    main()
