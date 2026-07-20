from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n" + "=" * 40)
    print("         SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 40)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 40)
    print("6. Salir")

def ejecutar_registrar_producto(restaurante: Restaurante):
    print("\n--- Registrar Producto ---")
    try:
        codigo = input("Código del producto: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        
        producto = Producto(codigo, nombre, categoria, precio)
        if restaurante.agregar_producto(producto):
            print("\nProducto registrado correctamente.")
        else:
            print(f"\nError: Ya existe un producto con el código '{codigo}'.")
    except ValueError as e:
        print(f"\nError de validación: {e}")

def ejecutar_registrar_bebida(restaurante: Restaurante):
    print("\n--- Registrar Bebida ---")
    try:
        codigo = input("Código de la bebida: ")
        nombre = input("Nombre de la bebida: ")
        categoria = input("Categoría (ej. Jugos, Gaseosas): ")
        precio = float(input("Precio: "))
        tamano = input("Tamaño / Presentación (ej. 500ml, Familiar): ")
        
        bebida = Bebida(codigo, nombre, categoria, precio, tamano)
        if restaurante.agregar_producto(bebida):
            print("\nBebida registrada correctamente.")
        else:
            print(f"\nError: Ya existe un producto/bebida con el código '{codigo}'.")
    except ValueError as e:
        print(f"\nError de validación: {e}")

def ejecutar_registrar_cliente(restaurante: Restaurante):
    print("\n--- Registrar Cliente ---")
    try:
        id_cliente = int(input("ID del cliente (Número entero): "))
        nombre = input("Nombre completo: ")
        correo = input("Correo electrónico: ")
        
        cliente = Cliente(id_cliente, nombre, correo)
        if restaurante.agregar_cliente(cliente):
            print("\nCliente registrado correctamente.")
        else:
            print(f"\nError: Ya existe un cliente con el ID {id_cliente}.")
    except ValueError as e:
        print(f"\nError: Entrada inválida. {e}")

def ejecutar_listar_productos(restaurante: Restaurante):
    print("\n--- Lista de Productos y Bebidas ---")
    productos = restaurante.listar_productos()
    if productos:
        for p in productos:
            p.mostrar_informacion()
    else:
        print("No existen productos ni bebidas registrados.")

def ejecutar_listar_clientes(restaurante: Restaurante):
    print("\n--- Lista de Clientes ---")
    clientes = restaurante.listar_clientes()
    if clientes:
        for c in clientes:
            c.mostrar_informacion()
    else:
        print("No existen clientes registrados.")

def main():
    restaurante = Restaurante()
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            ejecutar_registrar_producto(restaurante)
        elif opcion == "2":
            ejecutar_registrar_bebida(restaurante)
        elif opcion == "3":
            ejecutar_registrar_cliente(restaurante)
        elif opcion == "4":
            ejecutar_listar_productos(restaurante)
        elif opcion == "5":
            ejecutar_listar_clientes(restaurante)
        elif opcion == "6":
            print("\nGracias por utilizar el sistema Restaurante. ¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()