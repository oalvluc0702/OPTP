import math
coste = float(input("Dime el precio de tu comida: "))
propina = int(input("Dime el porcentaje de propina que vas a dejar: "))
propina =  1 + (propina / 100)
precioTotal = coste*propina
print("El importe total son",round(precioTotal,2),"€")