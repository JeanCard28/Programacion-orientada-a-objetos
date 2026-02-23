# servicios/inventario.py

from modelos.producto import Producto
import os


class Inventario:
    """
    Gestiona productos y persistencia en archivo.
    """

    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # ===============================
    # CARGAR INVENTARIO DESDE ARCHIVO
    # ===============================
    def cargar_desde_archivo(self):
        """
        Lee el archivo inventario.txt y reconstruye
        la lista de productos.
        """

        try:
            # Si no existe, crear archivo vacío
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                return

            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split(",")

                    # Validar líneas corruptas
                    if len(datos) != 4:
                        continue

                    id_p, nombre, cantidad, precio = datos
                    producto = Producto(
                        id_p,
                        nombre,
                        int(cantidad),
                        float(precio)
                    )
                    self.productos.append(producto)

            print("✅ Inventario cargado desde archivo.")

        except PermissionError:
            print("❌ Error: No hay permisos para leer el archivo.")

        except Exception as e:
            print(f"❌ Error inesperado al cargar archivo: {e}")

    # ===============================
    # GUARDAR INVENTARIO
    # ===============================
    def guardar_en_archivo(self):
        """
        Sobrescribe el archivo con el inventario actual.
        """

        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    f.write(linea)

            return True

        except PermissionError:
            print("❌ Error: permiso denegado al escribir archivo.")
            return False

        except Exception as e:
            print(f"❌ Error inesperado al guardar: {e}")
            return False

    # ===============================
    # CRUD
    # ===============================
    def agregar_producto(self, producto):

        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ ID duplicado.")
                return False

        self.productos.append(producto)

        if self.guardar_en_archivo():
            print("✅ Producto agregado y guardado en archivo.")
        else:
            print("⚠ Producto agregado pero NO guardado.")

        return True

    def eliminar_producto(self, id_producto):

        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)

                if self.guardar_en_archivo():
                    print("✅ Producto eliminado del sistema y archivo.")
                else:
                    print("⚠ Eliminado en memoria pero falló el archivo.")

                return True

        print("❌ Producto no encontrado.")
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):

        for p in self.productos:
            if p.get_id() == id_producto:

                if cantidad is not None:
                    p.set_cantidad(cantidad)

                if precio is not None:
                    p.set_precio(precio)

                if self.guardar_en_archivo():
                    print("✅ Producto actualizado y guardado.")
                else:
                    print("⚠ Actualizado pero no guardado.")

                return True

        print("❌ Producto no encontrado.")
        return False

    def buscar_producto(self, nombre):
        return [
            p for p in self.productos
            if nombre.lower() in p.get_nombre().lower()
        ]

    def mostrar_inventario(self):

        if not self.productos:
            print("📦 Inventario vacío.")
            return

        print("\n===== INVENTARIO =====")
        for p in self.productos:
            print(p)