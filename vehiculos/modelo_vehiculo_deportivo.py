# Clase hija

from modelo_vehiculo import Vehiculo


class Vehiculo_deportivo(Vehiculo):
    # Clase que representa un vehículo deportivo

    def prender_motor(self):
        # Método para mostrar el tipo de motor
        print("el tipo de motor es:", self.motor)


    def ver_luces(self):
        # Método para mostrar el tipo de luces
        print("las luces del vehiculo deportivo son", self.luces)


    def sistema_ventanas(self):
        # Método para mostrar el sistema de ventanas
        print("las ventanas del vehiculo deportivo son", self.ventana)


    def imprimir_info(self):
        # Método para imprimir la información completa
        super().imprimir_info()

        print("El motor es:", self.motor)
        print("Las luces son:", self.luces)
        print("Las ventanas son:", self.ventana)

        return "Informacion encontrada"


    def __init__(self, marca, placa, color, motor, luces, ventana):
        # Constructor de la clase Vehiculo_deportivo
        super().__init__(marca, placa, color)

        self.motor = motor    # Tipo de motor
        self.luces = luces    # Tipo de luces
        self.ventana = ventana  # Tipo de ventanas