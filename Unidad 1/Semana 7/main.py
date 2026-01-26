"""
Programa principal
Punto de entrada del sistema.
Demuestra el uso de constructores y destructores.
"""

from servicios.gestor_archivos import GestorArchivos


def main():
    gestor = GestorArchivos()
    gestor.crear_y_escribir_archivo(
        "ejemplo.txt",
        "Este archivo fue creado usando constructores y destructores en Python."
    )

    print("Fin del programa principal.")


if __name__ == "__main__":
    main()
