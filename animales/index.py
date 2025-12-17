from base_datos import Base_datos
bd = Base_datos()
bd.cargar_datos_iniciales()

op = 0

from modelo_animal_caballo import Caballo
from modelo_animal_cocodrilo import Cocodrilo
from modelo_animal_escarabajo import Escarabajo
from modelo_animal_pescado import Pescado
from modelo_animal_pato import Pato


while op != 4:

    print("menu animales")
    print("1 agregar")
    print("2 eliminar")
    print("3 mostrar")
    print("4 salir")

    op = int(input("opcion: "))

    match op:

        case 1:
            tipo_a = input("tipo animal: ")

            n = input("nombre: ")
            e = int(input("edad: "))
            h = input("habitat: ")
            d = input("dieta: ")
            t = input("tamaño: ")
            c = input("color: ")

            if tipo_a == "caballo":
                r = input("raza: ")
                v = int(input("velocidad: "))
                nuevo = Caballo(n, e, h, d, t, c, r, v)
                bd.agregar_animal(nuevo)

            elif tipo_a == "cocodrilo":
                f = int(input("fuerza mordida: "))
                nuevo = Cocodrilo(n, e, h, d, t, c, f)
                bd.agregar_animal(nuevo)

            elif tipo_a == "escarabajo":
                alas = input("tiene alas (si/no): ")

                if alas == "si":
                    nuevo = Escarabajo(n, e, h, d, t, c, True)
                else:
                    nuevo = Escarabajo(n, e, h, d, t, c, False)

                bd.agregar_animal(nuevo)

            elif tipo_a == "pescado":
                agua = input("tipo de agua: ")
                nuevo = Pescado(n, e, h, d, t, c, agua)
                bd.agregar_animal(nuevo)

            elif tipo_a == "pato":
                pico = input("tipo pico: ")
                nuevo = Pato(n, e, h, d, t, c, pico)
                bd.agregar_animal(nuevo)

            else:
                print("tipo incorrecto")

        case 2:
            ind = int(input("indice: "))
            bd.eliminar_por_posicion(ind)

        case 3:
            bd.mostrar_lista()

        case 4:
            print("programa terminado")

        case _:
            print("opcion invalida")