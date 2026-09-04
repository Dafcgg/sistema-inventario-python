
inventario = []


siguiente_id = 1


def agregar_producto():
    """Solicita datos al usuario y agrega un nuevo producto al inventario."""
    global siguiente_id

    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("⚠ El nombre no puede estar vacío.\n")
        return

    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
    except ValueError:
        print("⚠ Cantidad y precio deben ser numéricos.\n")
        return

    producto = {
        "id": siguiente_id,
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    inventario.append(producto)
    siguiente_id += 1

    print(f"Producto '{nombre}' agregado con ID {producto['id']}.\n")


def listar_productos():
    """Muestra todos los productos registrados en el inventario."""
    if not inventario:
        print("El inventario está vacío.\n")
        return

    print("\n{:<5} {:<20} {:<10} {:<10}".format("ID", "Nombre", "Cantidad", "Precio"))
    print("-" * 45)
    for producto in inventario:
        print("{:<5} {:<20} {:<10} {:<10.2f}".format(
            producto["id"], producto["nombre"], producto["cantidad"], producto["precio"]
        ))
    print()


def buscar_producto():
    """Busca productos por nombre (coincidencia parcial, sin distinguir mayúsculas)."""
    termino = input("Nombre a buscar: ").strip().lower()

    resultados = [p for p in inventario if termino in p["nombre"].lower()]

    if not resultados:
        print(f"🔍 No se encontraron productos que coincidan con '{termino}'.\n")
        return

    print(f"\nResultados para '{termino}':")
    for producto in resultados:
        print(f"  - ID {producto['id']}: {producto['nombre']} "
            f"(Cantidad: {producto['cantidad']}, Precio: {producto['precio']:.2f})")
    print()


def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("=" * 40)
    print("  SISTEMA DE GESTIÓN DE INVENTARIO")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Salir")


def main():
    """Función principal: controla el ciclo del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            print("👋 Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("⚠ Opción no válida. Intente de nuevo.\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
