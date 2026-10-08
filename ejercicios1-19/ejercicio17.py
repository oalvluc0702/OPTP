frutas = ["manzana",
          "plátano",
          "naranja"]
while True:
    print("1- Ver lista completa")
    print("2- Ver un elemento por índice")
    print("3- Añadir elemento")
    print("4- Modificar Elemento")
    print("5- Borrar Elemento")
    print("6- Salir")

    opcion = int(input("Escoge un número: "))

    match opcion:
        case 1:
            print(frutas)
        case 2:
            posicion = int(input("dime un índice para ver: "))
            print(frutas[posicion])
        case 3:
            frutaAñadir = str(input("Dime la fruta que quieres añadir: "))
            frutas.append(frutaAñadir)
        case 4:
            frutaModificar = str(input("Dime la fruta que quieres añadir por otra: "))
            while True:
                posicion = int(input("dime un índice para modificar: "))
                confirmacion = int(input(f"{frutas[posicion]} Seguro que quieres modificar esa fruta? 1. si 2.no 3. volver: "))
                if confirmacion == 1: 
                    frutas[posicion] = frutaModificar
                    break
                if confirmacion == 3: break
        case 5:
            while True:
                posicion = int(input("dime un índice para borrar: "))
                confirmacion = int(input(f"{frutas[posicion]} Seguro que quieres borrar esa fruta? 1. si 2.no 3. volver: "))
                if confirmacion == 1: 
                    frutas.pop(posicion)
                    break
                if confirmacion == 3: break
        case 6:
            print("saliendo del programa...")
            break