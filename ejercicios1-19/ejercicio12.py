import math
peso = float(input("Dime tu peso(KG): "))
altura = float(input("Dime tu altura(metros)"))
imc = peso / pow(altura,2)
print("Su IMC es:",round(imc,2))