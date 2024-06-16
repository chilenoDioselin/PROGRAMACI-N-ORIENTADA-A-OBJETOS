class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Clase principal para manejar la entrada y el cálculo
class GestorClima:
    def __init__(self):
        self.clima_diario = ClimaDiario()

    def ingresar_datos(self):
        for i in range(7):
            temp = float(input(f"Ingresa la temperatura del día {i+1}: "))
            self.clima_diario.ingresar_temperatura(temp)

    def mostrar_promedio(self):
        promedio = self.clima_diario.calcular_promedio_semanal()
        print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    gestor_clima = GestorClima()
    gestor_clima.ingresar_datos()
    gestor_clima.mostrar_promedio()
