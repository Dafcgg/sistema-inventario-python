inventario = []
siguiente_id = 1


def solicitar_numero_valido(mensaje, tipo=float):
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo. Intente de nuevo.\n")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un valor numérico válido.\n")


def buscar_por_id(id_producto):
    return next((p for p in inventario if p["id"] == id_producto), None)


def solicitar_id_existente(mensaje):
    try:
        id_ingresado = int(input(mensaje))
    except ValueError:
        print("El ID debe ser un número.\n")
        return None

    producto = buscar_por_id(id_ingresado)
    if producto is None:
        print(f"No se encontró ningún producto con ID {id_ingresado}.\n")
    return producto


def agregar_producto():
    global siguiente_id

    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.\n")
        return

    cantidad = solicitar_numero_valido("Cantidad: ", tipo=int)
    precio = solicitar_numero_valido("Precio: ", tipo=float)

    inventario.append({
        "id": siguiente_id,
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    })

    print(f"Producto '{nombre}' agregado con ID {siguiente_id}.\n")
    siguiente_id += 1


def listar_productos():
    if not inventario:
        print("El inventario está vacío.\n")
        return

    encabezado = "{:<5} {:<20} {:<10} {:<10}".format("ID", "Nombre", "Cantidad", "Precio")
    print(f"\n{encabezado}")
    print("-" * len(encabezado))
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


def actualizar_campo_numerico(producto, campo, mensaje, tipo):
    entrada = input(mensaje).strip()
    if not entrada:
        return

    try:
        valor = tipo(entrada)
    except ValueError:
        print(f"Valor inválido para {campo}. No se actualizó.\n")
        return

    if valor < 0:
        print(f"{campo.capitalize()} no puede ser negativo. No se actualizó.\n")
        return

    producto[campo] = valor


def actualizar_producto():
    if not inventario:
        print("El inventario está vacío.\n")
        return

    producto = solicitar_id_existente("ID del producto a actualizar: ")
    if producto is None:
        return

    print(f"Editando '{producto['nombre']}' "
          f"(cantidad actual: {producto['cantidad']}, precio actual: {producto['precio']:.2f})")
    print("Deje el campo vacío si no desea modificarlo.")

    actualizar_campo_numerico(producto, "cantidad", "Nueva cantidad: ", int)
    actualizar_campo_numerico(producto, "precio", "Nuevo precio: ", float)

    print(f"Producto '{producto['nombre']}' actualizado.\n")


MENU_OPCIONES = {
    "1": ("Agregar producto", agregar_producto),
    "2": ("Listar productos", listar_productos),
    "3": ("Buscar producto", buscar_producto),
    "4": ("Actualizar producto", actualizar_producto),
}


def mostrar_menu():
    print("=" * 40)
    print("  SISTEMA DE GESTIÓN DE INVENTARIO")
    print("=" * 40)
    for clave, (etiqueta, _) in MENU_OPCIONES.items():
        print(f"{clave}. {etiqueta}")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "5":
            print("Saliendo del sistema. Hasta pronto.")
            break

        accion = MENU_OPCIONES.get(opcion)
        if accion is None:
            print("Opción no válida. Intente de nuevo.\n")
            continue

        _, funcion = accion
        funcion()


if __name__ == "__main__":
    main()
