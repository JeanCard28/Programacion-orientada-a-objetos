# servicios/inventario.py

import modelos.producto


class Inventario:
    """
    Clase encargada de gestionar los productos.
    """

    def __init__(self):
        self.productos = []

    # Añadir producto
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: ID ya existe.")
                return False

        self.productos.append(producto)
        print("✅ Producto agregado correctamente.")
        return True

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("✅ Producto eliminado.")
                return True

        print("❌ Producto no encontrado.")
        return False

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)

                print("✅ Producto actualizado.")
                return True

        print("❌ Producto no encontrado.")
        return False

    # Buscar por nombre (coincidencia parcial)
    def buscar_producto(self, nombre):
        resultados = [
            p for p in self.productos
            if nombre.lower() in p.get_nombre().lower()
        ]

        return resultados

    # Mostrar inventario
    def mostrar_inventario(self):
        if not self.productos:
            print("📦 Inventario vacío.")
            return

        print("\n=== INVENTARIO ===")
        for producto in self.productos:
            print(producto)
