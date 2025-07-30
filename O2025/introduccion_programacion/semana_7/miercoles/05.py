# main.py

clientes = {}
pedidos = {}

def cargar_clientes(nombre_archivo):
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
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            primera_linea = archivo.readline()
            if not primera_linea:
                print(f"⚠️ El archivo '{nombre_archivo}' está vacío.")
                return
            
            for linea in archivo:
                partes = linea.strip().split(',')
                if len(partes) == 3:
                    try:
                        id_pedido = int(partes[0])
                        id_cli = int(partes[1])
                        monto = int(partes[2])
                        pedidos[id_pedido] = {"id_cli": id_cli, "monto": monto}
                    except ValueError:
                        print(f"❌ Error de datos en línea: {linea.strip()}")
                        continue
    except FileNotFoundError:
        print(f"🚫 Archivo '{nombre_archivo}' no encontrado.")

def mostrar_clientes():
    print("\n📋 Clientes:")
    for id_cliente, nombre in clientes.items():
        print(f"ID: {id_cliente}, Nombre: {nombre}")

def mostrar_pedidos():
    print("\n📦 Pedidos:")
    for id_pedido, datos in pedidos.items():
        cliente = clientes.get(datos['id_cli'], 'Desconocido')
        print(f"ID Pedido: {id_pedido}, Cliente: {cliente}, Monto: ${datos['monto']}")

def buscar_pedidos_por_cliente():
    id_cliente = input("\n🔍 Ingrese el ID del cliente para ver sus pedidos: ")
    try:
        id_cliente = int(id_cliente)
    except ValueError:
        print("ID inválido. Debe ser un número.")
        return

    print(f"\nPedidos del cliente {clientes.get(id_cliente, 'Desconocido')}:")
    encontrados = False
    for id_pedido, datos in pedidos.items():
        if datos["id_cli"] == id_cliente:
            print(f"  Pedido ID: {id_pedido}, Monto: ${datos['monto']}")
            encontrados = True
    if not encontrados:
        print("  No hay pedidos registrados para este cliente.")

def mostrar_estadisticas():
    print("\n📊 Estadísticas de pedidos:")
    if not pedidos:
        print("No hay datos de pedidos disponibles.")
        return

    montos = [datos["monto"] for datos in pedidos.values()]
    total = sum(montos)
    promedio = total / len(montos)
    maximo = max(montos)
    minimo = min(montos)

    print(f"🔸 Total de ventas: ${total}")
    print(f"🔸 Promedio de pedidos: ${promedio:.2f}")
    print(f"🔸 Pedido más alto: ${maximo}")
    print(f"🔸 Pedido más bajo: ${minimo}")

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
