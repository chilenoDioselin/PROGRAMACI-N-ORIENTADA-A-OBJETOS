# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    # Añadir nuevo producto
    def agregar_producto(self, producto):
        if not any(p.get_id() == producto.get_id() for p in self.productos):
            self.productos.append(producto)
            print("Producto añadido exitosamente.")
        else:
            print("Error: El ID del producto ya existe.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        print("Producto eliminado exitosamente.")

    # Actualizar cantidad o precio por ID
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    # Buscar productos por nombre
    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(
                    f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")

    # Mostrar todos los productos
    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(
                    f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
        else:
            print("El inventario está vacío.")


# Interfaz de Usuario en la Consola
def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad (deje en blanco si no quiere cambiarla): ")
            nuevo_precio = input("Ingrese el nuevo precio (deje en blanco si no quiere cambiarlo): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()
