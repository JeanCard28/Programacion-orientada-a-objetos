"""
Clase encargada de la gestión de estudiantes.
Demuestra el uso de polimorfismo.
"""

class GestionEstudiantes:
    def mostrar_informacion(self, persona):
        print("Nombre:", persona.get_nombre())
        print("Edad:", persona.get_edad())
        print("Descripción:", persona.descripcion())
        print("----------------------------")
