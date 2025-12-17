from modelo_animal import Animal


class Escarabajo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, puede_volar):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.puede_volar = puede_volar


    def volar(self):
        # Método modificado
        if self.puede_volar:
            print(self.nombre, "está volando")
        else:
            print(self.nombre, "no puede volar")


    def mostrar_info(self):
        super().mostrar_info()
        print("Puede volar:", self.puede_volar)