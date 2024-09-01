import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("Producto ya existe.")
        else:
            self.productos[producto.id] = producto
            print("Producto añadido.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos.")

    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            json.dump({id: vars(p) for id, p in self.productos.items()}, archivo)
        print(f"Inventario guardado en {nombre_archivo}.")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                datos = json.load(archivo)
                self.productos = {id: Producto(**info) for id, info in datos.items()}
            print(f"Inventario cargado desde {nombre_archivo}.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

def mostrar_menu():
    print("\n--- Menú del Inventario ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar productos")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")

def main():
    inventario = Inventario()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(Producto(id, nombre, cantidad, precio))
        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = input("ID del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == '4':
            nombre = input("Nombre del producto: ")
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == '5':
            inventario.mostrar_todos_los_productos()
        elif opcion == '6':
            nombre_archivo = input("Nombre del archivo: ")
            inventario.guardar_en_archivo(nombre_archivo)
        elif opcion == '7':
            nombre_archivo = input("Nombre del archivo: ")
            inventario.cargar_desde_archivo(nombre_archivo)
        elif opcion == '8':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
