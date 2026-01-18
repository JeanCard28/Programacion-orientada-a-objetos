# Clase base Empleado
class Empleado:
    def __init__(self, nombre, salario):
        # Atributos encapsulados (privados)
        self.__nombre = nombre
        self.__salario = salario

    # Métodos getter (encapsulación)
    def get_nombre(self):
        return self.__nombre

    def get_salario(self):
        return self.__salario

    # Método que será sobrescrito (polimorfismo)
    def calcular_pago(self):
        return self.__salario