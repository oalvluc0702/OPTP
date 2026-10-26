ventas = [
    ("manzanas", 3, 2.7),
    ("plátanos", 1.5, 1.99),
    ("leche", 4, 1.10),
    ("pan", 2, 0.85),
    ("queso", 0.5, 12.50)
]
def calcularTotal(cantidad, precio):
    return round(cantidad*precio)

for venta in ventas:
    producto = venta[0]
    cantidad = venta[1]
    precio = venta[2]
    print(f"{producto}: {calcularTotal(cantidad,precio)}")
