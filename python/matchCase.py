print("1. wow")
print("2. hola")

while True:
    opcion = int(input("elige una opción: "))
    match opcion:
        case 1:
            print("has elegido wow")
        
        case 2:
            print("has elegido hola")
            
        case _:
            print("eres tonto o no sabes leer")
            break



