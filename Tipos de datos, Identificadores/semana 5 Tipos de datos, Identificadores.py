"""
Este programa calcula el área de un círculo basado en el radio proporcionado por el usuario.
Utiliza diferentes tipos de datos y sigue las convenciones de codificación.
"""

import math


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    # Verifica que el radio sea positivo
    if radio > 0:
        area = math.pi * (radio ** 2)
        return area
    else:
        return None


def main():
    # Solicita al usuario que ingrese el radio del círculo
    radio_str = input("Introduce el radio del círculo: ")

    try:
        # Convierte la entrada del usuario a un número de punto flotante
        radio = float(radio_str)

        # Llama a la función para calcular el área
        area = calcular_area_circulo(radio)

        # Verifica si el área es válida (no None)
        if area is not None:
            print(f"El área del círculo con radio {radio} es: {area:.2f}")
        else:
            print("El radio debe ser un número positivo.")

    except ValueError:
        print("Por favor, introduce un número válido.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
