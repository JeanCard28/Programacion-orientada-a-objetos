"""
Servicio GestorArchivos
Contiene la lógica para trabajar con la clase Archivo.
No mezcla lógica con la definición del modelo.
"""

from modelos.archivo import Archivo


class GestorArchivos:
    def crear_y_escribir_archivo(self, nombre_archivo: str, mensaje: str):
        """
        Crea un objeto Archivo y escribe contenido dentro de él.
        """
        archivo = Archivo(nombre_archivo)
        archivo.escribir(mensaje)

        # Eliminamos la referencia para forzar la destrucción del objeto
        del archivo
