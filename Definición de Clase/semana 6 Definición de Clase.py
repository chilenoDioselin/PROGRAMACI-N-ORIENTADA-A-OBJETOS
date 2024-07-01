# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca  # Atributo encapsulado
        self._modelo = modelo  # Atributo encapsulado

    def mostrar_info(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}"

    def arrancar(self):
        return "El vehículo ha arrancado."


# Definición de la clase derivada Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self._num_puertas = num_puertas  # Atributo encapsulado

    # Polimorfismo: Sobrescribir el método arrancar
    def arrancar(self):
        return "El coche ha arrancado."

    # Método adicional para mostrar información específica del coche
    def mostrar_info(self):
        info_base = super().mostrar_info()  # Llamada al método de la clase base
        return f"{info_base}, Número de puertas: {self._num_puertas}"


# Creación de instancias y demostración de funcionalidad
vehiculo1 = Vehiculo("Toyota", "Corolla")
coche1 = Coche("Ford", "Mustang", 2)

# Uso de los métodos y demostración de polimorfismo
print(vehiculo1.mostrar_info())  # Marca: Toyota, Modelo: Corolla
print(vehiculo1.arrancar())  # El vehículo ha arrancado.

print(coche1.mostrar_info())  # Marca: Ford, Modelo: Mustang, Número de puertas: 2
print(coche1.arrancar())  # El coche ha arrancado.
