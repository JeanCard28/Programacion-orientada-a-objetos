# ==========================================
# IMPORTACIÓN DE LIBRERÍAS
# ==========================================

# json permite convertir datos Python a texto
# para guardarlos en archivos y volverlos a cargar.
import json

# os permite verificar si un archivo existe
# antes de intentar abrirlo.
import os


# ==========================================
# CLASE PRODUCTO
# Representa un solo item del inventario
# ==========================================
class Producto:

    # Constructor: se ejecuta al crear un producto
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos privados (__)
        # Se usan para aplicar encapsulamiento (POO)
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # ---------- GETTERS ----------
    # Permiten obtener valores sin acceder directamente
    # a los atributos privados

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # ---------- SETTERS ----------
    # Permiten modificar valores de forma controlada

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Convierte el objeto en diccionario
    # Esto es necesario para poder guardarlo en JSON
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }


# ==========================================
# CLASE INVENTARIO
# Administra todos los productos
# ==========================================
class Inventario:

    # Constructor
    def __init__(self):
        # Diccionario principal del inventario
        # clave = ID producto
        # valor = objeto Producto
        self.productos = {}

    # --------------------------------------
    # AGREGAR PRODUCTO
    # --------------------------------------
    def agregar_producto(self, producto):

        # Verifica si el ID ya existe
        if producto.get_id() in self.productos:
            print("⚠ Producto ya existe.")
        else:
            # Se guarda usando el ID como clave
            self.productos[producto.get_id()] = producto
            print("✅ Producto agregado.")

    # --------------------------------------
    # ELIMINAR PRODUCTO POR ID
    # --------------------------------------
    def eliminar_producto(self, id_producto):

        # Comprueba si el producto existe
        if id_producto in self.productos:
            # del elimina la clave del diccionario
            del self.productos[id_producto]
            print("🗑 Producto eliminado.")
        else:
            print("Producto no encontrado.")

    # --------------------------------------
    # ACTUALIZAR DATOS DEL PRODUCTO
    # --------------------------------------
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):

        # get() evita error si no existe
        producto = self.productos.get(id_producto)

        if producto:
            # Solo actualiza si el usuario ingresó valor
            if cantidad is not None:
                producto.set_cantidad(cantidad)

            if precio is not None:
                producto.set_precio(precio)

            print("✅ Producto actualizado.")
        else:
            print("Producto no encontrado.")

    # --------------------------------------
    # BUSCAR PRODUCTOS POR NOMBRE
    # --------------------------------------
    def buscar_por_nombre(self, nombre):

        # Lista por comprensión:
        # recorre todos los productos
        resultados = [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

        # Mostrar resultados encontrados
        if resultados:
            for p in resultados:
                self.mostrar_producto(p)
        else:
            print("No se encontraron coincidencias.")

    # --------------------------------------
    # MOSTRAR UN PRODUCTO
    # --------------------------------------
    def mostrar_producto(self, producto):

        print(f"ID: {producto.get_id()} | "
              f"Nombre: {producto.get_nombre()} | "
              f"Cantidad: {producto.get_cantidad()} | "
              f"Precio: ${producto.get_precio():.2f}")

    # --------------------------------------
    # MOSTRAR TODO EL INVENTARIO
    # --------------------------------------
    def mostrar_todos(self):

        # Verifica si el inventario está vacío
        if not self.productos:
            print("Inventario vacío.")
        else:
            # Recorre todos los productos
            for producto in self.productos.values():
                self.mostrar_producto(producto)

    # ======================================
    # FUNCIONES DE ARCHIVO (PERSISTENCIA)
    # ======================================

    # Guarda inventario en archivo JSON
    def guardar_archivo(self, archivo="inventario.json"):

        # Convierte cada producto a diccionario
        datos = [p.to_dict() for p in self.productos.values()]

        # Abre archivo en modo escritura
        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)

        print("💾 Inventario guardado.")

    # Carga inventario desde archivo
    def cargar_archivo(self, archivo="inventario.json"):

        # Si no existe archivo, no hace nada
        if not os.path.exists(archivo):
            return

        # Abre archivo en modo lectura
        with open(archivo, "r") as f:
            datos = json.load(f)

        # Reconstruye objetos Producto
        for item in datos:
            producto = Producto(
                item["id"],
                item["nombre"],
                item["cantidad"],
                item["precio"]
            )

            self.productos[item["id"]] = producto


# ==========================================
# MENÚ INTERACTIVO (INTERFAZ DE USUARIO)
# ==========================================
def menu():

    # Se crea inventario
    inventario = Inventario()

    # Carga datos guardados previamente
    inventario.cargar_archivo()

    # Bucle infinito del menú
    while True:

        print("\n===== SISTEMA INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Guardar")
        print("7. Salir")

        opcion = input("Seleccione opción: ")

        # -------- OPCIÓN 1 --------
        if opcion == "1":
            idp = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(idp, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        # -------- OPCIÓN 2 --------
        elif opcion == "2":
            inventario.eliminar_producto(input("ID: "))

        # -------- OPCIÓN 3 --------
        elif opcion == "3":
            idp = input("ID: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            inventario.actualizar_producto(
                idp,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        # -------- OPCIÓN 4 --------
        elif opcion == "4":
            inventario.buscar_por_nombre(input("Nombre: "))

        # -------- OPCIÓN 5 --------
        elif opcion == "5":
            inventario.mostrar_todos()

        # -------- OPCIÓN 6 --------
        elif opcion == "6":
            inventario.guardar_archivo()

        # -------- SALIR --------
        elif opcion == "7":
            inventario.guardar_archivo()
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


# Punto de entrada del programa
# Solo ejecuta el menú si el archivo se ejecuta directamente
if __name__ == "__main__":
    menu()