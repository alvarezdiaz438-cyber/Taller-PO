from base_datos import Base_datos
db = Base_datos()
db.cargar_datos()

salir = False


from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico
from modelo_botella_vidrio import Botella_vidrio


while salir == False:

    print("opciones")
    print("1 guardar botella")
    print("2 borrar botella")
    print("3 ver lista")
    print("4 salir")

    op = int(input("opcion: "))

    if op == 1:
        t = input("tipo: ")

        m = input("marca: ")
        c = input("capacidad: ")
        tp = input("tapa: ")

        if t == "normal":
            b = Botella(m, c, tp)
            db.agregar_botella(b)

        elif t == "plastico":
            d = input("diseño: ")
            mat = input("material: ")
            ti = input("tinte: ")

            b = Botella_plastico(m, c, tp, d, mat, ti)
            db.agregar_botella(b)

        elif t == "vidrio":
            d = input("diseño: ")
            mat = input("material: ")
            ti = input("tinte: ")

            b = Botella_vidrio(m, c, tp, d, mat, ti)
            db.agregar_botella(b)

        else:
            print("tipo incorrecto")

    elif op == 2:
        ind = int(input("indice: "))
        db.borrar(ind)

    elif op == 3:
        db.listar()

    elif op == 4:
        print("fin")
        salir = True

    else:
        print("opcion no valida")