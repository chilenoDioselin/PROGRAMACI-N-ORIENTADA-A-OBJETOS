class Pelicula:
    def __init__(self, titulo, duracion, genero):
        """
        Constructor de la clase Pelicula.
        Args:
            titulo (str): Título de la película.
            duracion (int): Duración de la película en minutos.
            genero (str): Género de la película.
        """
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        """
        Método para obtener una representación en cadena de la película.
        Returns:
            str: Descripción de la película.
        """
        return f'Pelicula: {self.titulo}, Duración: {self.duracion} minutos, Género: {self.genero}'


class Cine:
    def __init__(self, nombre):
        """
        Constructor de la clase Cine.
        Args:
            nombre (str): Nombre del cine.
        """
        self.nombre = nombre
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        """
        Método para agregar una película a la cartelera del cine.
        Args:
            pelicula (Pelicula): Instancia de la clase Pelicula.
        """
        self.peliculas.append(pelicula)

    def mostrar_cartelera(self):
        """
        Método para mostrar la cartelera de películas del cine.
        """
        if not self.peliculas:
            print("No hay películas en cartelera.")
        else:
            print(f'Cartelera del cine {self.nombre}:')
            for pelicula in self.peliculas:
                print(pelicula)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear el cine
    cine = Cine("Cine Python")

    # Crear algunas películas
    pelicula1 = Pelicula("legion de angeles", 144, "Ciencia ficción")
    pelicula2 = Pelicula("La laguna azul", 144, "drama")
    pelicula3 = Pelicula("indestructible", 143, "accion")

    # Agregar las películas al cine
    cine.agregar_pelicula(pelicula1)
    cine.agregar_pelicula(pelicula2)
    cine.agregar_pelicula(pelicula3)

    # Mostrar la cartelera del cine
    cine.mostrar_cartelera()
