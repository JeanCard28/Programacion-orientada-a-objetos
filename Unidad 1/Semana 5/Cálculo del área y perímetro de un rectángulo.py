"""
Programa: Cálculo del área y perímetro de un rectángulo
Descripción:
Este programa solicita al usuario el ancho y el alto de un rectángulo,
calcula su área y su perímetro, y muestra los resultados en pantalla.
"""

# Solicitar datos al usuario (tipo string convertido a float)
rect_width = float(input("Ingrese el ancho del rectángulo en metros: "))
rect_height = float(input("Ingrese el alto del rectángulo en metros: "))

# Cálculo del área y del perímetro (tipo float)
rect_area = rect_width * rect_height
rect_perimeter = 2 * (rect_width + rect_height)

# Variable booleana para validar si el área es mayor a 10 m²
is_large_area = rect_area > 10

# Mostrar resultados al usuario (uso de string)
print("\nResultados del cálculo:")
print(f"Área del rectángulo: {rect_area} metros cuadrados")
print(f"Perímetro del rectángulo: {rect_perimeter} metros")

# Evaluación lógica usando boolean
if is_large_area:
    print("El rectángulo tiene un área mayor a 10 m².")
else:
    print("El rectángulo tiene un área menor o igual a 10 m².")
