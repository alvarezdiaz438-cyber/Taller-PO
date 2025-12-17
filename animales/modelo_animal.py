class Animal:
    # Clase padre Animal

    def mostrar_info(self):
        # Muestra la información general del animal
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Hábitat:", self.habitat)
        print("Dieta:", self.dieta)
        print("Tamaño:", self.tamaño)
        print("Color:", self.color)


    def alimentarse(self):
        # Método para la alimentación
        print(self.nombre, "se alimenta principalmente de", self.dieta)


    def moverse(self):
        # Método de movimiento
        print(self.nombre, "se mueve de un lugar a otro")


    def descansar(self):
        # Método para el descanso
        print(self.nombre, "está descansando tranquilamente")


    def sueño(self):
        # Método para dormir
        print(self.nombre, "se encuentra durmiendo")


    def comunicarse(self):
        # Método de comunicación
        print(self.nombre, "se comunica con otros animales")


    def interaccion_social(self):
        # Método de interacción social
        print(self.nombre, "interactúa con su grupo")


    def reproducirse(self):
        # Método de reproducción
        print(self.nombre, "se reproduce para mantener su especie")


    def adaptarse(self):
        # Método de adaptación
        print(self.nombre, "se adapta a su entorno:", self.habitat)


    def instinto(self):
        # Método instintivo
        print(self.nombre, "actúa siguiendo su instinto")


    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        # Constructor de la clase Animal
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color