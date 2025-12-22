class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def ocupar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} | Tipo: {self.tipo} | Precio: ${self.precio} | Estado: {estado}"
