# Clase hija

from modelo_vehiculo import Vehiculo


class Vehiculo_transporte(Vehiculo):
    # Clase que representa un vehículo de transporte

    def usar_puertas(self):
        # Método para mostrar la cantidad de puertas
        print("el vehiculo tiene", self.puertas, "puertas")


    def tener_llantas(self):
        # Método para mostrar la cantidad de llantas
        print("el vehiculo tiene", self.llantas, "llantas")


    def imprimir_info(self):
        # Método para imprimir la información completa
        super().imprimir_info()

        print("las puertas son:", self.puertas)
        print("las llantas son:", self.llantas)

        return "informacion encontrada"


    def __init__(self, marca, placa, color, puertas, llantas):
        # Constructor de la clase Vehiculo_transporte
        super().__init__(marca, placa, color)

        self.puertas = puertas   # Cantidad de puertas
        self.llantas = llantas   # Cantidad de llantas