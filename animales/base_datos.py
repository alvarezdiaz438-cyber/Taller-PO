class Base_datos:
    def __init__(self):
        self.lista_animales = []

    def agregar_animal(self, animal):
        self.lista_animales.append(animal)
        print("animal agregado")

    def eliminar_por_posicion(self, posicion):
        if posicion >= 0 and posicion < len(self.lista_animales):
            self.lista_animales.pop(posicion)
            print("animal eliminado")
        else:
            print("posicion no valida")

    def mostrar_lista(self):
        if len(self.lista_animales) == 0:
            print("no hay animales")
        else:
            for i, animal in enumerate(self.lista_animales):
                print("posicion:", i)
                animal.mostrar_info()

    def cargar_datos_iniciales(self):
        from modelo_animal_caballo import Caballo
        from modelo_animal_cocodrilo import Cocodrilo
        from modelo_animal_escarabajo import Escarabajo
        from modelo_animal_pescado import Pescado
        from modelo_animal_pato import Pato

        self.lista_animales.append(
            Caballo("cassio", 5, "Pradera", "Hierba", "Grande", "Marrón", "Mustang", 60)
        )

        self.lista_animales.append(
            Cocodrilo("au", 12, "Pantano", "Carnívoro", "Grande", "Verde", 3000)
        )

        self.lista_animales.append(
            Escarabajo("bellona", 1, "Bosque", "Hojas", "Pequeño", "Negro", True)
        )

        self.lista_animales.append(
            Pescado("maicol", 2, "Arrecife", "Plancton", "Pequeño", "Naranja", "Salada")
        )

        self.lista_animales.append(
            Pato("travis", 3, "Lago", "Omnívoro", "Mediano", "Blanco", "Ancho")
        )