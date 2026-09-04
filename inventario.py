"""Sistema de Gestión de Inventario Básico por Consola"""

inventario = []
siguiente_id = 1


def solicitar_numero_valido(mensaje, tipo=float):
    """Solicita un número al usuario y valida que sea positivo."""
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo. Intente de nuevo.\n")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un valor numérico válido.\n")


def agregar_producto():
    global siguiente_id

    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.\n")
        return

    cantidad = solicitar_numero_valido("Cantidad: ", tipo=int)
    precio = solicitar_numero_valido("Precio: ", tipo=float)

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
    termino = input("Nombre a buscar: ").strip().lower()

    resultados = [p for p in inventario if termino in p["nombre"].lower()]

    if not resultados:
        print(f"No se encontraron productos que coincidan con '{termino}'.\n")
        return

    print(f"\nResultados para '{termino}':")
    for producto in resultados:
        print(f"  - ID {producto['id']}: {producto['nombre']} "
              f"(Cantidad: {producto['cantidad']}, Precio: {producto['precio']:.2f})")
    print()


def actualizar_producto():
    if not inventario:
        print("El inventario está vacío.\n")
        return

    try:
        id_buscado = int(input("ID del producto a actualizar: "))
    except ValueError:
        print("El ID debe ser un número.\n")
        return

    producto = next((p for p in inventario if p["id"] == id_buscado), None)

    if producto is None:
        print(f"No se encontró ningún producto con ID {id_buscado}.\n")
        return

    print(f"Editando '{producto['nombre']}' "
          f"(cantidad actual: {producto['cantidad']}, precio actual: {producto['precio']:.2f})")
    print("Deje el campo vacío si no desea modificarlo.")

    nueva_cantidad = input("Nueva cantidad: ").strip()
    if nueva_cantidad:
        try:
            valor = int(nueva_cantidad)
            if valor < 0:
                print("La cantidad no puede ser negativa. No se actualizó.\n")
            else:
                producto["cantidad"] = valor
        except ValueError:
            print("Cantidad inválida. No se actualizó.\n")

    nuevo_precio = input("Nuevo precio: ").strip()
    if nuevo_precio:
        try:
            valor = float(nuevo_precio)
            if valor < 0:
                print("El precio no puede ser negativo. No se actualizó.\n")
            else:
                producto["precio"] = valor
        except ValueError:
            print("Precio inválido. No se actualizó.\n")

    print(f"Producto '{producto['nombre']}' actualizado.\n")


def mostrar_menu():
    print("=" * 40)
    print("  SISTEMA DE GESTIÓN DE INVENTARIO")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Salir")


def main():
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
            actualizar_producto()
        elif opcion == "5":
            print("Saliendo del sistema. Hasta pronto.")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")


if __name__ == "__main__":
    main()
