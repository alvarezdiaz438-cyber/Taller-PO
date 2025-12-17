from modelo_animal import Animal


class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, fuerza_mordida):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.fuerza_mordida = fuerza_mordida


    def atacar(self):
        # Método modificado
        print(self.nombre, "ataca con una fuerza de", self.fuerza_mordida, "PSI")


    def nadar(self):
        print(self.nombre, "está nadando")


    def mostrar_info(self):
        super().mostrar_info()
        print("Fuerza de mordida:", self.fuerza_mordida)