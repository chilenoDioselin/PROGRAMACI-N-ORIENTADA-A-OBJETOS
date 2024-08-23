class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar los productos

    def guardar_en_archivo(self):
        with open('inventario.txt', 'w') as archivo:
            for codigo, datos in self.productos.items():
                archivo.write(f'{codigo},{datos["nombre"]},{datos["cantidad"]},{datos["precio"]}\n')

    def añadir_producto(self, codigo, nombre, cantidad, precio):
        if codigo in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[codigo] = {'nombre': nombre, 'cantidad': cantidad, 'precio': precio}
            self.guardar_en_archivo()

    def actualizar_producto(self, codigo, nombre=None, cantidad=None, precio=None):
        if codigo in self.productos:
            if nombre is not None:
                self.productos[codigo]['nombre'] = nombre
            if cantidad is not None:
                self.productos[codigo]['cantidad'] = cantidad
            if precio is not None:
                self.productos[codigo]['precio'] = precio
            self.guardar_en_archivo()
        else:
            print("El producto no existe.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_en_archivo()
        else:
            print("El producto no existe.")

    def mostrar_inventario(self):
        for codigo, datos in self.productos.items():
            print(f'{codigo}: {datos["nombre"]}, Cantidad: {datos["cantidad"]}, Precio: {datos["precio"]}')


# Ejemplo de uso:
inventario = Inventario()

# Añadir productos
inventario.añadir_producto('001', 'Laptop', 10, 1500)
inventario.añadir_producto('002', 'Mouse', 50, 25)

# Actualizar un producto
inventario.actualizar_producto('002', cantidad=45)

# Mostrar inventario
inventario.mostrar_inventario()

# Eliminar un producto
inventario.eliminar_producto('001')

# Mostrar inventario actualizado
inventario.mostrar_inventario()
