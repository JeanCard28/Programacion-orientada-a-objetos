from modelos.empleado import Empleado
from modelos.empleado_tiempo_completo import EmpleadoTiempoCompleto
from servicios.gestion_empleados import GestionEmpleados

# Crear instancias de las clases
empleado1 = Empleado("Juan", 500)
empleado2 = EmpleadoTiempoCompleto("María", 800, 200)

# Servicio de gestión
gestion = GestionEmpleados()

# Demostración del funcionamiento
gestion.mostrar_pago(empleado1)
gestion.mostrar_pago(empleado2)
