from modelos.producto import Producto
from servicios.inventario import Inventario


def menu():
    print("\n===== SISTEMA INVENTARIO =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione opción: ")

        try:
            if opcion == "1":
                id_p = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_p, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            elif opcion == "2":
                inventario.eliminar_producto(input("ID: "))

            elif opcion == "3":
                id_p = input("ID: ")
                cantidad = input("Nueva cantidad: ")
                precio = input("Nuevo precio: ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_p, cantidad, precio)

            elif opcion == "4":
                nombre = input("Buscar nombre: ")
                resultados = inventario.buscar_producto(nombre)

                for p in resultados:
                    print(p)

            elif opcion == "5":
                inventario.mostrar_inventario()

            elif opcion == "6":
                print("👋 Sistema finalizado.")
                break

            else:
                print("❌ Opción inválida.")

        except ValueError:
            print("❌ Error: entrada numérica inválida.")


if __name__ == "__main__":
    main()