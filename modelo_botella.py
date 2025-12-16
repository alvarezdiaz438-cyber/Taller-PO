class Botella:
    # Clase que representa una botella

    def imprimir_info(self):
        # Método para mostrar la información de la botella
        print("La marca es:", self.marca)
        print("La capacidad de la botella es:", self.capacidad)
        print("El tipo de tapa es:", self.tapa)


    def cerrar_tapa(self, dato_cantidad):
        # Método para cerrar la tapa de la botella
        print("Se usó la tapa:", self.tapa)
        print("Cantidad de tapas usadas:", dato_cantidad)
        return dato_cantidad


    def llenar_botella(self, capacidad):
        # Método para llenar la botella
        print("La botella se está llenando:", capacidad)
        print("Se va a usar la tapa:", self.tapa)


    def __init__(self, marca, capacidad, tapa):
        # Constructor de la clase Botella
        self.marca = marca        # Marca de la botella
        self.capacidad = capacidad  # Capacidad de la botella
        self.tapa = tapa          # Tipo de tapa