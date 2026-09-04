# Sistema de Gestión de Inventario (Consola)

Sistema CRUD básico desarrollado en Python para gestionar un inventario de productos desde consola. Permite agregar, listar, buscar y actualizar productos, utilizando estructuras de datos nativas (listas y diccionarios) para almacenar la información en memoria durante la ejecución.

Proyecto desarrollado como parte de mi formación como desarrollador de software, con énfasis en buenas prácticas de programación y control de versiones con Git.

## Tecnologías utilizadas

- Python 3

## Requisitos previos

- Tener instalado Python 3.8 o superior.
- No se requieren librerías externas, el proyecto usa únicamente la librería estándar de Python.

## Instalación y ejecución

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```

2. Ingresa a la carpeta del proyecto:

   ```bash
   cd tu-repositorio
   ```

3. Ejecuta el script:

   ```bash
   python3 inventario.py
   ```

4. Usa el menú interactivo para gestionar el inventario:

   ```
   ========================================
     SISTEMA DE GESTIÓN DE INVENTARIO
   ========================================
   1. Agregar producto
   2. Listar productos
   3. Buscar producto
   4. Actualizar producto
   5. Salir
   ```

## Funcionalidades

- Agregar producto: registra un nuevo producto con nombre, cantidad y precio, validando que los valores numéricos no sean negativos.
- Listar productos: muestra todos los productos registrados en formato de tabla.
- Buscar producto: busca productos por nombre, aceptando coincidencias parciales.
- Actualizar producto: permite modificar la cantidad y/o el precio de un producto existente mediante su ID.

## Posibles mejoras futuras

- Persistencia de datos en archivo (JSON o CSV).
- Eliminación de productos.
- Interfaz gráfica o web.

## Autor

Dilan, estudiante de desarrollo de software.
