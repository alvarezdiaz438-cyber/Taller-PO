# ===== Clase padre =====
class Botella:

    # Constructor
    def __init__(self, marca, capacidad, tapa):
        self.marca = marca
        self.capacidad = capacidad
        self.tapa = tapa


    # Método para imprimir la información de la botella
    def imprimir_info(self):
        print("La marca es:", self.marca)
        print("La capacidad de la botella es:", self.capacidad)
        print("El tipo de tapa es:", self.tapa)


    # Método para llenar la botella
    def llenar_botella(self, capacidad):
        print("La botella se está llenando:", capacidad)
        print("Se va a usar la tapa:", self.tapa)


    # Método para cerrar la tapa
    def cerrar_tapa(self, dato_cantidad):
        print("Se usó la tapa:", self.tapa)
        print("Cantidad de tapas usadas:", dato_cantidad)
        return dato_cantidad