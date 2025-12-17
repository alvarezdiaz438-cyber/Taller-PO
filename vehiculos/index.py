from base_datos import Base_datos
bd = Base_datos()
bd.cargar_datos_iniciales()

op = 0


from modelo_vehiculo import Vehiculo
from modelo_vehiculo_deportivo import Vehiculo_deportivo
from modelo_vehiculo_carga import Vehiculo_carga
from modelo_vehiculo_transporte import Vehiculo_transporte


while op != 4:

    print("menu vehiculos")
    print("1 agregar")
    print("2 eliminar")
    print("3 mostrar")
    print("4 salir")

    op = int(input("opcion: "))

    match op:

        case 1:
            tipo_v = input("tipo: ")

            m = input("marca: ")
            p = input("placa: ")
            c = input("color: ")

            if tipo_v == "normal":
                nuevo = Vehiculo(m, p, c)
                bd.agregar_vehiculo(nuevo)

            elif tipo_v == "deportivo":
                mot = input("motor: ")
                luz = input("luces: ")
                ven = input("ventanas: ")

                nuevo = Vehiculo_deportivo(m, p, c, mot, luz, ven)
                bd.agregar_vehiculo(nuevo)

            elif tipo_v == "carga":
                pas = input("pasajeros: ")
                comb = input("combustible: ")

                nuevo = Vehiculo_carga(m, p, c, pas, comb)
                bd.agregar_vehiculo(nuevo)

            elif tipo_v == "transporte":
                puer = input("puertas: ")
                llan = input("llantas: ")

                nuevo = Vehiculo_transporte(m, p, c, puer, llan)
                bd.agregar_vehiculo(nuevo)

            else:
                print("tipo incorrecto")

        case 2:
            ind = int(input("indice: "))
            bd.eliminar_por_posicion(ind)

        case 3:
            bd.mostrar_lista()

        case 4:
            print("fin del programa")

        case _:
            print("opcion invalida")