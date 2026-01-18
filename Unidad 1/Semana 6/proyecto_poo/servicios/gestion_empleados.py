class GestionEmpleados:
    def mostrar_pago(self, empleado):
        # Polimorfismo: no importa el tipo de empleado
        print(f"Empleado: {empleado.get_nombre()}")
        print(f"Pago total: ${empleado.calcular_pago()}")
        print("--------------------------")