# PRACTICA WORKLOW ANÁLISIS DE DATOS
# QUÉ ES EL ANÁLISIS DE DATOS?
# PROCESO SISTEMÁTICO DE APLICAR TÉCNICAS DE CARGA, LIMPIEZA, ANÁLISIS ESTADÍSTICO DE DATOS
# EVALUAR Y APOYAR LA TOMA DE DECISIONES
#
#
# WORKFLOW DA:
# 1. CARGA DE DATOS -> 2. LIMPIEZA DE DATOS -> 3. ANÁLISIS -> 4. VISUALIZACIÓN 
#                               *
# (a)  determinar cuáles son los errores posibles / necesidades de análisis
#          ¿cuáles son las columnas importantes en la fase 3 del workflow?
#          identificar cuáles son los posibles errores presentes en esas columnas
#           -> formato de datos (numérico, real o entero, cadena de caracteres): astype
#           -> rango de datos (validación de acuerdo a los valores que se requieren)
#                 ej: edad de personas no admiten números negativos, rango de años, meses
#               iterar sobre el dataframe y analizar cada una de las columnas importantes
#
# (b)  determinar cómo se van a corregir
#           -> eliminación de filas con valores nulos:  dropna
#           -> eliminación de columnas nulas: drop
#           -> elminación de duplicados: drop_duplicated


# (1) cargar dataframe desde el archivo plano
# (2)  identificar los errores presentes, de acuerdo a su tipo
# (3)  corregirlos

# HACER EL EJERCICIO CON police.csv (columnas driver_age_raw (año), driver_age (edad en años))

import pandas as pd

#función propia para eliminar varias columnas nulas del dataframe:
def drop_columns(df:pd.DataFrame, columns_list):
    for col_name in columns_list:
        df.drop(col_name,inplace=True,axis=1)

#carga del dataset:
df_police = pd.read_csv("police.csv")
df_police.info()

#limpieza del dataset:
#limpieza de columnas con valores nulos:
cols = ["county_name","search_type"]
drop_columns(df_police,cols)
df_police.dropna(inplace=True)
df_police.info()

#renombrar columna "driver_age_raw":
df_police.rename(columns={"driver_age_raw":"birth_year"},inplace=True)
df_police.info()

#validar datos:
#conversion de formato:
# verificar python data types

#convertir estas dos columnas a entero
df_police = df_police.astype({"birth_year":"int64"})
df_police = df_police.astype({"driver_age":"int64"})

print(df_police.head(10)) #10 primeras filas del dataframe
print(df_police.tail(10)) #10 últimas filas del dataframe

#validar rango de valores de las columnas:
#iterar en el dataframe:

media_anio = df_police["birth_year"].mean()

# año de nacimiento (birth_year):
for i, row in df_police.iterrows():                          #invocamos la función iterrow para crear un iterador sobre las 
    if row["birth_year"] < 1900 or row["birth_year"] > 1987: #filas del dataframe: i, indice de la fila. item, info de la fila
                                                              #validar que el año corresponda a un mayor de edad
        #opción 1: asignar un valor que pueda corresponder al promedio
        df_police.loc[i,"birth_year"] = media_anio

        #opción 2: eliminar la columna:                                                            
        #df_police.drop(i)

# corregir edad (driver_age):

# obtener media de la columna:
media_edad = df_police["driver_age"].mean()

for i, item in df_police.iterrows():                          #invocamos la función iterrow para crear un iterador sobre las 
    if row["driver_age"] < 18 or row["driver_age"] > 70: #filas del dataframe: i, indice de la fila. item, info de la fila
                                                              #validar que el año corresponda a un mayor de edad
        #opción 1: asignar un valor que pueda corresponder al promedio
        df_police.loc[i,"driver_age"] = media_edad

        #opción 2: eliminar la columna:                                                            
        #df_police.drop(i)

# INTRODUCCIÓN A LA FASE 3 DEL WORKFLOW

# (a) SELECCIÓN DE UN SUBCONJUNTO DE FILAS DEL DATAFRAME
df_police_sub = df_police[ ["stop_date","stop_time","driver_gender","driver_age","violation_raw","is_arrested","drugs_related_stop"]  ]

# df_police_sub.info()
# print(df_police_sub.head(10))
# df_police_sub.to_json("police_inf2005.json")
# df_police_sub.to_xml("police_inf2005.xml")

# (b) FILTRADO DEL DATAFRAME (SOLO FILAS QUE CUMPLAN CONDICIONES SOBRE UNA O VARIAS COLUMNAS)
df_police_sub_under_40 = df_police_sub[ df_police_sub["driver_age"] < 40  ]
print(df_police_sub_under_40)
