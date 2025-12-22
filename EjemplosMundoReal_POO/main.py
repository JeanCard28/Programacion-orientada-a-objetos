from cliente import Cliente
from habitacion import Habitacion
from reserva import Reserva

def main():
    cliente1 = Cliente("Juan Pérez", "0102030405")
    habitacion1 = Habitacion(101, "Doble", 45)

    reserva1 = Reserva(cliente1, habitacion1, 3)

    print(reserva1.confirmar_reserva())
    print()
    print(reserva1.mostrar_resumen())

if __name__ == "__main__":
    main()
