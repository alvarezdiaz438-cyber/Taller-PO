from modelo_animal import Animal


class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, raza, velocidad):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.raza = raza
        self.velocidad = velocidad


    def galopar(self):
        # Método modificado de forma sencilla
        print(self.nombre, "está galopando a una velocidad de", self.velocidad, "km/h")


    def relinchar(self):
        print(self.nombre, "está relinchando")


    def mostrar_info(self):
        super().mostrar_info()
        print("Raza:", self.raza)
        print("Velocidad:", self.velocidad)