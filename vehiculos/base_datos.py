class Base_datos:

    def __init__(self):
        
        self.lista_vehiculos = []

    def mostrar_lista(self):
    
        if self.lista_vehiculos == []:
            print("lista vacia")
        else:
            contador = 0
            for v in self.lista_vehiculos:
                print("indice:", contador)
                v.imprimir_info()
                contador = contador + 1

    def agregar_vehiculo(self, obj):
        # agregar vehiculo
        self.lista_vehiculos.append(obj)
        print("vehiculo guardado")

    def eliminar_por_posicion(self, pos):
        # eliminar segun indice
        if pos >= 0 and pos < len(self.lista_vehiculos):
            self.lista_vehiculos.pop(pos)
            print("vehiculo eliminado")
        else:
            print("indice incorrecto")

    def cargar_datos_iniciales(self):
        
        from modelo_vehiculo import Vehiculo
        from modelo_vehiculo_deportivo import Vehiculo_deportivo
        from modelo_vehiculo_carga import Vehiculo_carga
        from modelo_vehiculo_transporte import Vehiculo_transporte

        v1 = Vehiculo("Toyota", "ABC123", "Blanco")
        v2 = Vehiculo_deportivo("Ferrari", "F999", "Rojo", "V8", "LED", "Electricas")
        v3 = Vehiculo_carga("Chevrolet", "C456", "Gris", 3, "Diesel")
        v4 = Vehiculo_transporte("Mercedes", "T777", "Azul", 4, 6)

        self.lista_vehiculos.append(v1)
        self.lista_vehiculos.append(v2)
        self.lista_vehiculos.append(v3)
        self.lista_vehiculos.append(v4)