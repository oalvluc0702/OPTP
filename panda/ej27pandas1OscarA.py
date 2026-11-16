import os
#1
import pandas as pd
#2
nombre_archivo = "Ej 27 Pandas 1 Datos.xlsx"
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
print(datos)
#6


    
