"""
Clase Estudiante
Hereda de Persona y redefine su comportamiento.
"""

from modelos.persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, promedio: float):
        super().__init__(nombre, edad)
        self.promedio = promedio

    # Método sobrescrito (polimorfismo)
    def descripcion(self) -> str:
        return "Estudiante registrado en el sistema académico"
