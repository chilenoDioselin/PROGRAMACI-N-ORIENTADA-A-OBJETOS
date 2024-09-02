# Clase Libro: representa un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.info = (titulo, autor)  # Tupla para almacenar título y autor

    def __str__(self):
        return f"{self.titulo} por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario: representa un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

    def listar_libros_prestados(self):
        if not self.libros_prestados:
            return "No hay libros prestados actualmente."
        return "\n".join(str(libro) for libro in self.libros_prestados)


# Clase Biblioteca: gestiona la colección de libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y Usuario como valor
        self.usuarios_ids = set()  # Conjunto para IDs de usuario únicos

    def anadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado de la biblioteca.")
        else:
            print("El libro no se encontró en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_ids:
            print("El usuario ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.usuarios_ids.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_ids:
            del self.usuarios[id_usuario]
            self.usuarios_ids.remove(id_usuario)
            print("Usuario dado de baja con éxito.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_ids:
            print("Usuario no registrado.")
            return

        if isbn not in self.libros:
            print("Libro no disponible en la biblioteca.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_ids:
            print("Usuario no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                return

        print("El usuario no tiene ese libro prestado.")

    def buscar_libro(self, **criterios):
        resultados = []
        for libro in self.libros.values():
            if all(getattr(libro, k) == v for k, v in criterios.items()):
                resultados.append(libro)

        if resultados:
            return "\n".join(str(libro) for libro in resultados)
        else:
            return "No se encontraron libros que coincidan con los criterios de búsqueda."

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            return self.usuarios[id_usuario].listar_libros_prestados()
        else:
            return "Usuario no encontrado."


# Ejemplos de uso
biblioteca = Biblioteca()

# Añadir libros a la biblioteca
libro1 = Libro("1984", "George Orwell", "Distopía", "9780451524935")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Realismo Mágico", "9780307474728")
biblioteca.anadir_libro(libro1)
biblioteca.anadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Dioselin", "U001")
usuario2 = Usuario("María", "U002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("U001", "9780451524935")

# Listar libros prestados por un usuario
print(usuario1.listar_libros_prestados())

# Buscar libros por autor
print(biblioteca.buscar_libro(autor="Gabriel García Márquez"))

# Devolver libro
biblioteca.devolver_libro("U001", "9780451524935")

# Listar libros prestados después de la devolución
print(usuario1.listar_libros_prestados())
