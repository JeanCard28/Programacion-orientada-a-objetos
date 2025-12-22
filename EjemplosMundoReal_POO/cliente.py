class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_datos(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}"
