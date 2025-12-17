# Clase hija

from modelo_vehiculo import Vehiculo


class Vehiculo_carga(Vehiculo):
    # Clase que representa un vehículo de carga

    def contar_pasajeros(self):
        # Método para mostrar la cantidad de pasajeros
        print("la cantidad de pasajeros es:", self.pasajeros)


    def consumir_combustible(self):
        # Método para mostrar el tipo de combustible
        print("el tipo de combustible es:", self.combustible)


    def imprimir_info(self):
        # Método para imprimir la información completa
        super().imprimir_info()

        print("la cantidad de pasajeros es:", self.pasajeros)
        print("el consumo de combustible es:", self.combustible)

        return "informacion encontrada"


    def __init__(self, marca, placa, color, pasajeros, combustible):
        # Constructor de la clase Vehiculo_carga
        super().__init__(marca, placa, color)

        self.pasajeros = pasajeros     # Número de pasajeros
        self.combustible = combustible # Tipo de combustible