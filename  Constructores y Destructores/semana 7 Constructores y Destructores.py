class Recurso:
    def __init__(self, nombre):
        """
        Constructor: se llama cuando se crea una instancia de la clase.
        Inicializa el objeto con el nombre proporcionado y abre un archivo para escribir.
        """
        self.nombre = nombre
        self.archivo = open(f'{self.nombre}.txt', 'w')
        print(f"Recurso '{self.nombre}' creado y archivo abierto.")

    def escribir_en_archivo(self, mensaje):
        """
        Método para escribir un mensaje en el archivo asociado con el objeto.
        """
        if self.archivo:
            self.archivo.write(mensaje + '\n')
            print(f"Mensaje '{mensaje}' escrito en {self.nombre}.txt")
        else:
            print("El archivo no está abierto.")

    def __del__(self):
        """
        Destructor: se llama cuando el objeto está a punto de ser destruido.
        Cierra el archivo si está abierto y realiza la limpieza necesaria.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre}.txt' cerrado.")
        print(f"Recurso '{self.nombre}' destruido.")


# Ejemplo de uso
def main():
    recurso1 = Recurso("ejemplo")
    recurso1.escribir_en_archivo("¡Hola, Mundo!")
    recurso1.escribir_en_archivo("Esto es una prueba.")

    # Al final del programa, el destructor __del__ se llamará automáticamente
    # cuando recurso1 salga del alcance y se elimine.
    del recurso1  # Se puede llamar explícitamente para ver la destrucción inmediata


if __name__ == "__main__":
    main()
