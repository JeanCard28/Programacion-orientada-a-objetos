"""
Clase Archivo
Representa un archivo de texto que puede abrirse y cerrarse.
Demuestra el uso de __init__ y __del__.
"""


class Archivo:
    def __init__(self, nombre_archivo: str):
        """
        Constructor:
        Se ejecuta automáticamente al crear el objeto.
        Inicializa el nombre del archivo y abre el recurso.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, "w", encoding="utf-8")
        print(f"Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir(self, contenido: str):
        """
        Escribe contenido dentro del archivo.
        """
        self.archivo.write(contenido + "\n")

    def __del__(self):
        """
        Destructor:
        Se ejecuta cuando el objeto es eliminado por el recolector de basura.
        Intenta cerrar el archivo si aún está abierto.

        Puede ejecutarse cuando:
        - El programa finaliza
        - El objeto deja de tener referencias
        """
        if not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")