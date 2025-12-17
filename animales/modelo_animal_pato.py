from modelo_animal import Animal


class Pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_pico):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_pico = tipo_pico


    def graznar(self):
        # Método modificado
        print(self.nombre, "grazna con su pico", self.tipo_pico)


    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo de pico:", self.tipo_pico)