# Programa para calcular el promedio semanal de temperaturas
# utilizando Programación Orientada a Objetos (POO)

# Clase base que representa información climática general
class Clima:
    def __init__(self):
        self.temperaturas = []

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


# Clase derivada que hereda de Clima
class ClimaSemanal(Clima):
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperatura es: {promedio:.2f}")


# Uso de las clases
print("Registro de temperaturas semanales (POO)")
clima = ClimaSemanal()
clima.ingresar_temperaturas()
clima.mostrar_promedio()
