import os
# Parte 1
#1
import pandas as pd
from pprint import pprint
#2
nombre_archivo = "Ej 27 Pandas 1.xlsx"
nombre_hoja = "Alumnos"
datos = {}
#3
excel = pd.ExcelFile(nombre_archivo)
#4
df = pd.read_excel(excel,sheet_name=nombre_hoja,index_col=None)
df.fillna("")
print(df)
#5
datos[nombre_hoja] = df.to_dict(orient="records")
pprint(datos)
#6
for hoja, filas in datos.items():
    for alumno in filas:
        for propiedad, valores in alumno.items():
            pprint(f"{propiedad}: {valores}")
            
        print(f"---")
print("Parte 2")
print("--------------------------------------")
# Parte 2
# 1
datos_dict = df.to_dict(orient="dict")
pprint(datos_dict)

for columna, filas in datos_dict.items():
    for indice, valor in filas.items():
        pprint(f"{indice} : {valor}")
    print("------")
# 2
datos_index = df.to_dict(orient="index")
pprint(datos_index)

for indice, alumno in datos_index.items():
    for columna, valor in alumno.items():
        pprint(f"{columna}: {valor}")
    print("------------")

# 3
datos_list = df.to_dict(orient="list")
pprint(datos_list)

for columna, lista_valores in datos_list.items():
    for valor in lista_valores:
        pprint(valor)
# parte 3
# 1
df_indice = pd.read_excel(excel,sheet_name=nombre_hoja,index_col=0)
print(df_indice)
# 2
datos_dict_id = df_indice.to_dict(orient="dict")
pprint(datos_dict_id)
for columna, alumnos in datos_dict_id.items():
    for id_persona, valor in alumnos.items():
        print(f"{id_persona}:{valor}")
    print("---")
# 3
datos_index_id = df_indice.to_dict(orient="index")
pprint(datos_index_id)
for id_persona, datos_alumno in datos_index_id.items():
    for columna, valor in datos_alumno.items():
        pprint(f"{columna} {valor}")
