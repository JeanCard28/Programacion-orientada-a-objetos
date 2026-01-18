from modelos.empleado import Empleado

# Clase derivada (herencia)
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono

    # Método sobrescrito (polimorfismo)
    def calcular_pago(self):
        return self.get_salario() + self.bono
