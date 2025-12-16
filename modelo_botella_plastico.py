from modelo_botella import Botella   # Importación de la clase padre


class Botella_plastico(Botella):
    # Clase hija que hereda de la clase Botella

    def reciclar_botella(self):
        # Método que indica que la botella será reciclada
        print("La botella se va a reciclar. Material:", self.material)


    def imprimir_info(self):
        # Método para mostrar la información completa
        super().imprimir_info()   # Información heredada

        print("El diseño es:", self.diseño)
        print("El material es:", self.material)
        print("El color es:", self.tinte)

        return "Informacion encontrada"


    def __init__(self, marca, capacidad, tapa, diseño, material, tinte):
        # Constructor de la clase hija
        super().__init__(marca, capacidad, tapa)

        self.diseño = diseño      # Diseño de la botella
        self.material = material  # Material plástico
        self.tinte = tinte        # Color o tinte
