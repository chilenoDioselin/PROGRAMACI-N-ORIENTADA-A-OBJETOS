# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingresa la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio_semanal(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal para ejecutar el programa
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
