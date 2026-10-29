EMPRESA_INFO = ("Tech Solutions S.L.","B-12345678","Madrid")
departamentos = [["Informatica",12],["Recursos Humanos",4]]
inventario_dict = {"Electronica": [["Televisor",450.0],["Movil",300.0]],"Hogar": [["Microondas",120.0]]}
def producto_mas_caro(inventario_dict : dict):
    producto = inventario_dict["Electronica"]
    for c, v in inventario_dict.items():
        for prod in v:
            print(prod[1], producto[1])
            if prod[f"{c}"] > producto[1]:
                producto = inventario_dict[c]
    return producto

def main():
    while True:
        print(f"DATOS DE EMPRESA: {EMPRESA_INFO[0]} - CIF {EMPRESA_INFO[1]} - {EMPRESA_INFO[2]}")
        print(f"=== GESTION INTERNA - {EMPRESA_INFO[0]} ===")
        print(f"1. añadir nuevo departamento")
        print(f"2. Imprimir: departamentos, numero de personas y el número total de empleados de la empresa")
        print(f"3. imprimir: inventario de productos y el nombre del producto con un precio mayor")
        print(f"4. salir")
        opcion = int(input("dime la opcion: "))
        match (opcion):
            case 1:
                departamento = input("Dime el nombre de departamento que quieres añadir").strip().title()
                existe = False
                for d in departamentos:  
                    if departamento in d:
                        print(f"Error: El departamento {departamento} ya existe")
                        existe = True
                        break
                if not existe:
                    numero_trabajadores = int(input("dime el número de trabajadores"))
                    departamentos.append([departamento, numero_trabajadores])
            case 2:
                total_empleados_empresa = 0
                for departamento in departamentos:
                    print(f"Departamento: {departamento[0]}- Numero de personas: {departamento[1]}")
                    total_empleados_empresa += departamento[1]
                print(f"TOTAL DE EMPLEADOS EN LA EMPRESA: {total_empleados_empresa}")
            case 3:
                print("--- INVENTARIO POR DEPARTAMENTOS ---")
                for c,v in inventario_dict.items():
                    print(f"Departamento: {c}")
                    for producto in v:
                        print(f"Producto: {producto[0]} - Precio: {producto[1]:.1f} €")
                producto_caro = producto_mas_caro(inventario_dict)
                print(f"El producto con el mayor precio es: {producto_caro[0]} con un precio de {producto_caro[1]}")
            #lo unico que no me sale es lo del producto más caro no se porque
main()