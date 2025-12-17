class Vehiculo:
    # Clase padre que representa un vehículo

    def imprimir_info(self):
        # Método para mostrar la información del vehículo
        print("la marca del vehiculo es:", self.marca)
        print("la placa del vehiculo es:", self.placa)
        print("el color del vehiculo es:", self.color)


    def arrancar_vehiculo(self):
        # Método para arrancar el vehículo
        print("el vehiculo esta arrancando:", self.marca)
        print("con placa:", self.placa)


    def aceleracion_frenado(self, velocidad):
        # Método para acelerar y frenar el vehículo
        print("el vehiculo", self.marca, "esta acelerando a", velocidad, "km/h")
        print("el vehiculo puede frenar segun la velocidad indicada")


    def mostrar_color(self):
        # Método para mostrar el color del vehículo
        print("el vehiculo", self.marca, "tiene color", self.color)


    def __init__(self, marca, placa, color):
        # Constructor de la clase Vehiculo
        self.marca = marca   # Marca del vehículo
        self.placa = placa   # Placa del vehículo
        self.color = color   # Color del vehículo