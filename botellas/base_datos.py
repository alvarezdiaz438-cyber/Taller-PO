class Base_datos:

    def __init__(self):
        # aqui se guardan las botellas
        self.botellas = []

    def agregar_botella(self, b):
        # guardar botella
        self.botellas.append(b)
        print("registro guardado")

    def listar(self):
        # mostrar botellas
        if self.botellas == []:
            print("no hay registros")
        else:
            i = 0
            for x in self.botellas:
                print("pos:", i)
                x.imprimir_info()
                i = i + 1

    def borrar(self, indice):
        # borrar por indice
        if indice >= 0 and indice < len(self.botellas):
            self.botellas.pop(indice)
            print("registro eliminado")
        else:
            print("indice incorrecto")

    def cargar_datos(self):
        # imports al final
        from modelo_botella import Botella
        from modelo_botella_plastico import Botella_plastico
        from modelo_botella_vidrio import Botella_vidrio

        x = Botella("coca_cola", "1.5l", "especial")
        y = Botella_plastico("pepsi", "2.5l", "comun", "redondo", "plastico", "sin tinte")
        z = Botella_vidrio("kola roman", "1.5l", "comun", "cubo", "vidrio", "roja")

        self.botellas.append(x)
        self.botellas.append(y)
        self.botellas.append(z)