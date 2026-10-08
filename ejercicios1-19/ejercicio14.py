import math

print("1- Conversor de metros a centímetros")
print("2- Calcular área del círculo")
print("3- Cuenta del restaurante")
print("4- Calculadora IMC")
print("5- Mensaje de bienvenida")

opcion = int(input("Dime cual quieres ejecutar: "))

match opcion:
    case 1:
        metros = float(input("Dime la cantidad de metros que quieres convertir a centímetros: "))
        centimetros = metros * 100

        print(metros,"metros son:",centimetros,"Centímetros")
    case 2:
        radio = float(input("Díme cuál es el radio del círculo: "))
        area = math.pi * (radio ** 2)

        print("El área del círculo es:",round(area,2))
    case 3:
        coste = float(input("Dime el precio de tu comida: "))
        propina = int(input("Dime el porcentaje de propina que vas a dejar: "))
        propina =  1 + (propina / 100)
        precioTotal = coste*propina
        print("El importe total son",round(precioTotal,2),"€")
    case 4:
        peso = float(input("Dime tu peso(KG): "))
        altura = float(input("Dime tu altura(metros)"))
        imc = peso / pow(altura,2)
        print("Su IMC es:",round(imc,2))
    case 5:
        nombre = str(input("Dime tu nombre: "))
        apellido = str(input("Dime tu apellido: "))
        mensaje = f"Hola {nombre} {apellido} bienvenido!"
        print(mensaje)
    case _:
        print("No has seleccionado ninguna opción válida")


