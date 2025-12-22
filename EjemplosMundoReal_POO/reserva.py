class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def confirmar_reserva(self):
        if self.habitacion.disponible:
            self.habitacion.ocupar()
            return "Reserva confirmada."
        return "La habitación no está disponible."

    def calcular_total(self):
        return self.dias * self.habitacion.precio

    def mostrar_resumen(self):
        return (
            f"{self.cliente.mostrar_datos()}\n"
            f"{self.habitacion.mostrar_info()}\n"
            f"Días: {self.dias}\n"
            f"Total a pagar: ${self.calcular_total()}"
        )
