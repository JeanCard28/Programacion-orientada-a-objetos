"""
Clase base Persona
Representa a una persona dentro del sistema.
Aplica encapsulación y define un comportamiento general.
"""

class Persona:
    def __init__(self, nombre: str, edad: int):
        # Atributos privados (encapsulación)
        self.__nombre = nombre
        self.__edad = edad

    # Métodos de acceso (getters)
    def get_nombre(self) -> str:
        return self.__nombre

    def get_edad(self) -> int:
        return self.__edad

    # Método que será sobrescrito (polimorfismo)
    def descripcion(self) -> str:
        return "Persona del sistema"
