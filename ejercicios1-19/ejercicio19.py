productos = ["manzanas", "plátanos", "naranjas", "kiwis", "fresas"]
info_tienda=("Frutería La Huerta", "Calle Mayor 12", "912345678",2010)
precios = {"manzanas": 1.50, "plátanos": 2.10, "naranjas": 1.20,"kiwis": 3.45, "fresas": 2.80}
def listar_precios():
    for k,v in precios.items():
        print(f"Fruta :{k} | {v} €")
def listar_frutas():
    print ("\n Frutas")
    for fruta in precios.keys():
         print(f"Fruta :{fruta}")
def listar_values():
    print("\n Precios")
    for precio in precios.values():
         print(f"Precios :{precio}")
def listarProductos():
    contador = 0
    for p in productos:
        print(f"{contador} | {p}")
        contador += 1
def formateador(texto):
    return texto.strip().lower()
def comparar_sin_tildes(precios: dict,texto: str):
    con_tilde = "áéíóú"
    sin_tilde = "aeiou"
    for con, sin in zip(con_tilde,sin_tilde):
        texto = texto.replace(con,sin)

    for clave in precios:
        clave_limpia = formateador(clave)
        for con, sin in zip(con_tilde, sin_tilde):
            clave_limpia = clave_limpia.replace(con, sin)
            
        if texto == clave_limpia:
            return clave
        
    return None
    
def gestion_productos():
    while True:
        print(" a) Consultar")
        print(" b) Añadir")
        print(" c) Modificar")
        print(" d) Eliminar")
        print(" e) Volver a atrás")
        opcion = formateador(input("Dime que opción quieres realizar: "))
        match (opcion):
            case "a":
                print(productos)
                print(f"hay almacenados: {len(productos)} productos")
            case "b":
                while True:
                    producto = formateador(input("Dime un nombre de un producto para agregarlo a la lista: "))
                
                    if producto in productos:
                        print("No puedes añadir un producto que ya existe")
                    else:
                        productos.append(producto)
                        break
            case "c":
                while True:
                    listarProductos()
                    try:
                        indice = int(input("Dime que índice quieres modificar: "))
                        nombreNuevo = formateador(input("Dime el nombre que quieres ponerle al elemento: "))
                        if nombreNuevo in productos:
                            print("No puedes ponerle el nombre de un producto que ya existe")
                        else:
                            productos[indice] = nombreNuevo
                            break
                    except ValueError:
                        print("Elige un número entero válido")
                    except IndexError:
                        print("Has intentado acceder a un índice no válido")
        
            case "d":
                listarProductos()
                try:
                    indice = int(input("Dime que índice quieres eliminar: "))
                    productos.pop(indice)
                except ValueError:
                    print("Elige un número entero válido")
                except IndexError:
                    print("Has intentado acceder a un índice no válido")

            case "e":
                break
            case _:
                print("No has elegido la opcion correcta \n")
def consulta_tienda():
    longitud = len(info_tienda)

    print(f"{info_tienda}")
    print(f"Hay una cantidad de: {longitud} elementos")
    for i in range(0, longitud):
        print(f"{info_tienda[i]}")
def gestion_precios():
    while True:
        print(" a) Consultar catálogo")
        print(" b) Ver solo nombres o precios")
        print(" c) Añadir o actualizar")
        print(" d) Eliminar")
        print(" e) Volver a atrás")      
        opcion = formateador(input("Dime que opción quieres realizar: "))

        match (opcion):
            case "a":
                listar_precios()
            case "b":
                listar_frutas()
                listar_values()
            case "c":
                fruta = formateador(input("Dime el nombre de la fruta: "))
                while True:
                    try:
                        precio = float(input("Dime el precio que va a tener: "))
                        break
                    except ValueError:
                        print("Pon un precio que tenga 2 decimales")
                precios[fruta] = precio
            case "d":
                fruta = formateador(input("Dime el nombre de la fruta: "))
                clave_real = comparar_sin_tildes(precios, fruta)
                if clave_real:
                    del precios[clave_real]
                    print(f"Se ha eliminado la fruta {clave_real}")
                else:
                    print(f"{fruta} no existe en el diccionario")
            case "e":
                break
            case _:
                print("No has elegido ninguna de las opcions disponibles")
                    
def main():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print(" 1) Gestión de productos")
        print(" 2) Consultar información de la tienda")
        print(" 3) Gestión de precios")
        print(" 4) Salir")
        try:
            opcion = int(input("Dime la opción: "))
        except ValueError:
            print("Por favor introduce un número entero válido")
            continue
        match (opcion):
            case 1:
                gestion_productos()
            case 2:
                consulta_tienda()
            case 3:
                gestion_precios()
            case 4:
                print("Saliendo del programa...")
                break
            case _:
                print("No has elegido la opcion correcta \n")


main()