MARCAS_MODELOS = { "Seat": ["Ibiza", "Leon", "Ateca", "Arona"], "Toyota": ["Corolla", "Yaris", "RAV4", "C-HR"] }

ventas = [
["Seat", "Ibiza", 2024, 2023, 18000], ["Seat", "Ibiza", 2024, 2024, 18500], ["Seat", "Ibiza", 2024, 2024, 19000],
["Seat", "Ibiza", 2025, 2024, 19500], ["Seat", "Ibiza", 2025, 2025, 20000], ["Seat", "Ibiza", 2025, 2025, 20200],
["Seat", "Ibiza", 2026, 2025, 20500], ["Seat", "Ibiza", 2026, 2026, 21000], ["Seat", "Ibiza", 2026, 2026, 21500],
["Seat", "Leon", 2024, 2024, 24000], ["Seat", "Leon", 2024, 2024, 24500], ["Seat", "Leon", 2024, 2023, 23800],
["Seat", "Leon", 2025, 2025, 25500], ["Seat", "Leon", 2025, 2025, 26000], ["Seat", "Leon", 2025, 2024, 25200],
["Seat", "Leon", 2026, 2026, 27000], ["Seat", "Leon", 2026, 2026, 27500], ["Seat", "Leon", 2026, 2025, 26800],
["Seat", "Ateca", 2024, 2024, 28000], ["Seat", "Ateca", 2025, 2025, 29500], ["Seat", "Ateca", 2026, 2026, 31000],
["Seat", "Arona", 2024, 2024, 21000], ["Seat", "Arona", 2025, 2025, 22000], ["Seat", "Arona", 2026, 2026, 23000],
["Toyota", "Corolla", 2024, 2024, 26000], ["Toyota", "Corolla", 2024, 2024, 26500], ["Toyota", "Corolla", 2024, 2023, 25800],
["Toyota", "Corolla", 2025, 2025, 27500], ["Toyota", "Corolla", 2025, 2025, 28000], ["Toyota", "Corolla", 2025, 2024, 27200],
["Toyota", "Corolla", 2026, 2026, 29000], ["Toyota", "Corolla", 2026, 2026, 29500], ["Toyota", "Corolla", 2026, 2025, 28800],
["Toyota", "Yaris", 2024, 2024, 20000], ["Toyota", "Yaris", 2025, 2025, 21000], ["Toyota", "Yaris", 2026, 2026, 22000],
["Toyota", "RAV4", 2024, 2024, 38000], ["Toyota", "RAV4", 2025, 2025, 39500], ["Toyota", "RAV4", 2026, 2026, 41000],
["Toyota", "C-HR", 2024, 2024, 31000], ["Toyota", "C-HR", 2025, 2025, 32500], ["Toyota", "C-HR", 2026, 2026, 34000]
]

def altaNuevaVenta():
    listaMostrar = []
    for marcas in MARCAS_MODELOS:
        listaMostrar.append(marcas)
    print(listaMostrar)
    while True:
        marca = input("Escribe el nombre de la marca :").capitalize()
        if marca in MARCAS_MODELOS:
            print(MARCAS_MODELOS[marca])
            while True:
                modelo = input("Escribe el nombre del modelo :").capitalize()
                if modelo in MARCAS_MODELOS[marca]:
                    break
                else:
                    print("Modelo incorrecto, intente de nuevo")
            break
        else:
            print("Esa marca no es válida")
    try:        
        anio_venta = int(input("Dime un año de venta: "))

        if not (2024 <= anio_venta <= 2026) or not anio_venta.is_integer():

            raise ValueError("El año debe estar entre 2024 y 2026 y ser un numero entero")
        
        anio_fabricacion = int(input("Dime un año de fabricación: "))

        if not (1990 <= anio_fabricacion <= anio_venta) or not anio_fabricacion.is_integer():
            raise ValueError("El año debe ser un entero entre 1990 y el año de la venta ")  
        
        precio = int(input("Dime el precio de la venta: "))
        if not (1000 <= precio <= 100000) or not precio.is_integer():
            raise ValueError("El precio no puede ser menor de 1000 ni mayor que 100000 y debe ser un número entero")
        
        venta = [marca,modelo,anio_venta,anio_fabricacion,precio]

        ventas.append(venta)
    except ValueError as e:
        print(e)
        print("no se ha podido realizar al venta")
def resumenMarcaModeloAnio():         
    registroVentas = {}

    for v in ventas:
        clave = f"{v[0]}_{v[1]}_{v[2]}"

        if clave not in registroVentas:

            registroVentas[clave] = [0,0]

        registroVentas[clave][0] += 1

        registroVentas[clave][1] += v[4]

    for claveR, valoresR in registroVentas.items():

        unidadesVendidas = valoresR[0]

        precioTotal = valoresR[1]
        
        print(f"Producto: {claveR} || unidades vendidas: {unidadesVendidas} Uds || Cantidad acumulada {precioTotal}€")
def resumenMarcaModelo():
    registroVentas = {}
    for v in ventas:
        clave = f"{v[0]}_{v[1]}"
        if clave not in registroVentas:
            registroVentas[clave] = [0,0]
        registroVentas[clave][0] += 1
        registroVentas[clave][1] += v[4]
    for claveR, valoresR in registroVentas.items():
        unidadesVendidas = valoresR[0]
        precioTotal = valoresR[1]
        print(f"Producto: {claveR} || unidades vendidas: {unidadesVendidas} Uds || Cantidad acumulada {precioTotal}€")
def resumenMarca():   
    registroVentas = {}
    for v in ventas:
        clave = f"{v[0]}"
        if clave not in registroVentas:
            registroVentas[clave] = [0,0]
        registroVentas[clave][0] += 1
        registroVentas[clave][1] += v[4]
    for claveR, valoresR in registroVentas.items():
        unidadesVendidas = valoresR[0]
        precioTotal = valoresR[1]
        print(f"Producto: {claveR} || unidades vendidas: {unidadesVendidas} Uds || Cantidad acumulada {precioTotal}€")
def main():
    while True:
        print("==========================================")
        print("SISTEMA DE GESTIÓN DE VENTAS")
        print("==========================================")
        print("1.- Dar de alta una nueva venta")
        print("2.- Resumen de ventas (Marca_Modelo_Año)")
        print("3.- Resumen de ventas (Marca_Modelo - Todos los años)")
        print("4.- Resumen de ventas (Marca - Todos los modelos y años)")
        print("5.- Salir del programa")
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
        match opcion:
            case "1":
                altaNuevaVenta()
            case "2":
                resumenMarcaModeloAnio()
            case "3":
                resumenMarcaModelo()
            case "4":
                resumenMarca()
            case "5":
                print("\n¡Saliendo del programa. ¡Hasta luego!\n")
                break     
            case _:
                print("\n[Error] Opción no válida. Por favor, ingrese un número del 1 al 5.\n")
main()