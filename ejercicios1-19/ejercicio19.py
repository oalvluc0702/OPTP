productos = ["manzanas", "plátanos", "naranjas", "kiwis", "fresas"]
info_tienda=("Frutería La Huerta", "Calle Mayor 12", "912345678",2010)
precios = {"manzanas": 1.50, "plátanos": 2.10, "naranjas": 1.20,"kiwis": 3.45, "fresas": 2.80}
def listarProductos():
    contador = 0
    for p in productos:
        print(f"{contador} | {p}")

def gestion_productos():
    print("\n a) Consultar")
    print("\n b) Añadir")
    print("\n c) Modificar")
    print("\n d) Eliminar")
    opcion = input("Dime que opción quieres realizar")

    match (opcion):
        case "a":
            print(f"hay almacenados {len(productos)} productos")
        case "b":
            while True:
                producto = input("Dime un nombre de un producto para agregarlo a la lista")
            
                if productos.__contains__(producto):
                    print("No puedes añadir un producto que ya existe")
                else:
                    productos.append(producto)
                    break
        case "c":
            listarProductos()
            indice = int(input("Dime que índice quieres modificar: "))
            nombreNuevo = input("Dime el nombre que quieres ponerle al elemento: ")
            productos[indice] = nombreNuevo
        case "d":
            listarProductos()
            indice = int(input("Dime que índice quieres eliminar: "))
            productos.pop(indice)
