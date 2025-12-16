from modelo_botella import Botella   # Se importa la clase padre


class Botella_vidrio(Botella):
    # Definición de la clase hija

    def reutilizar_botella(self):
        # Método que indica que la botella se puede reutilizar
        print("La botella se va a reutilizar. Material:", self.material)


    def imprimir_info(self):
        # Método que imprime la información de la botella
        super().imprimir_info()   # Información heredada de la clase padre

        print("El diseño es:", self.diseño)
        print("El material es:", self.material)
        print("El color es:", self.tinte)

        return "Informacion encontrada"


    def __init__(self, marca, capacidad, tapa, diseño, material, tinte):
        # Constructor de la clase
        super().__init__(marca, capacidad, tapa)

        self.diseño = diseño      # Diseño de la botella
        self.material = material  # Material de la botella
        self.tinte = tinte        # Tinte del vidrio