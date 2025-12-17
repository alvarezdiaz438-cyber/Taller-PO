from modelo_animal import Animal


class Pescado(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_agua):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_agua = tipo_agua


    def nadar(self):
        # Método modificado
        print(self.nombre, "está nadando en agua", self.tipo_agua)


    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo de agua:", self.tipo_agua)