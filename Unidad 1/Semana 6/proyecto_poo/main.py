"""
Programa principal
Demuestra el uso de POO: herencia, encapsulación y polimorfismo.
"""

from modelos.persona import Persona
from modelos.estudiante import Estudiante
from servicios.gestion_estudiantes import GestionEstudiantes

# Creación de objetos
persona1 = Persona("Carlos", 30)
estudiante1 = Estudiante("Ana", 20, 8.9)

# Uso del servicio
gestion = GestionEstudiantes()

gestion.mostrar_informacion(persona1)
gestion.mostrar_informacion(estudiante1)
